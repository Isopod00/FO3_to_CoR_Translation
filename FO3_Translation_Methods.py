# Authors: Sebastiaan Joosten, Anthony Brogni

from COR_Expressions import *
from FO3_Expressions import *


def list_union(list1, list2):
    """ Computes the mathematical 'union' of two python lists """
    answer = list1
    for term in list2:
        if term not in list1:
            answer.append(term)
    return answer


def T_Good_Dash(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    match expression:
        case ForAll(argument=arg, variable=var):
            terms = T_Good_ForAll(arg)
            return big_AND(terms, var)
        case ThereExists(argument=arg, variable=var):
            terms = T_Good_ThereExists(arg)
            return big_OR(terms, var)
        case AND(argument1=arg1, argument2=arg2):
            return AND(T_Good_Dash(arg1), T_Good_Dash(arg2))
        case OR(argument1=arg1, argument2=arg2):
            return OR(T_Good_Dash(arg1), T_Good_Dash(arg2))
        case _:
            return expression


def T_Good_ThereExists(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    match expression:
        case ForAll(argument=arg, variable=var):
            terms = T_Good_ForAll(arg)
            return [[big_AND(terms, var)]]
        case ThereExists(argument=arg, variable=var):
            terms = T_Good_ThereExists(arg)
            return [[big_OR(terms, var)]]
        case AND(argument1=arg1, argument2=arg2):
            answer = []
            for list1 in T_Good_ThereExists(arg1):
                for list2 in T_Good_ThereExists(arg2):
                    answer.append(list_union(list1, list2))
            return answer
        case OR(argument1=arg1, argument2=arg2):
            return list_union(T_Good_ThereExists(arg1), (T_Good_ThereExists(arg2)))
        case _:
            return [[expression]]


def T_Good_ForAll(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    match expression:
        case ForAll(argument=arg, variable=var):
            terms = T_Good_ForAll(arg)
            return [[big_AND(terms, var)]]
        case ThereExists(argument=arg, variable=var):
            terms = T_Good_ThereExists(arg)
            return [[big_OR(terms, var)]]
        case AND(argument1=arg1, argument2=arg2):
            return list_union(T_Good_ForAll(arg1), (T_Good_ForAll(arg2)))
        case OR(argument1=arg1, argument2=arg2):
            answer = []
            for list1 in T_Good_ForAll(arg1):
                for list2 in T_Good_ForAll(arg2):
                    answer.append(list_union(list1, list2))
            return answer
        case _:
            return [[expression]]


def T_Nice(expression):
    """ Translation function for translating "good" FO3 terms into "nice" FO3 terms """
    match expression:
        case ff() | tt():
            return expression
        case OR(argument1=arg1, argument2=arg2):  # OR Case
            return OR(T_Nice(arg1), T_Nice(arg2))
        case AND(argument1=arg1, argument2=arg2):  # AND Case
            return AND(T_Nice(arg1), T_Nice(arg2))
        case ThereExists(argument=arg, variable=var):  # ThereExists Case
            terms = arg.getAsAndList()
            lhs_list = [term for term in terms if var not in term.depends_on()]  # does NOT depend on the variable
            rhs_list = [term for term in terms if var in term.depends_on()]  # DOES depend on the variable
            lhs = T_Nice(n_ary_AND(lhs_list))
            rhs = make_ThereExists(var, T_Nice(n_ary_AND(rhs_list)))
            return make_AND(lhs, rhs)
        case ForAll(argument=arg, variable=var):  # ForAll Case
            terms = arg.getAsOrList()
            lhs_list = [term for term in terms if var not in term.depends_on()]  # does NOT depend on the variable
            rhs_list = [term for term in terms if var in term.depends_on()]  # DOES depend on the variable
            lhs = T_Nice(n_ary_OR(lhs_list))
            rhs = make_ForAll(var, T_Nice(n_ary_OR(rhs_list)))
            return make_OR(lhs, rhs)
        case _:  # This case is only reached if expression is an atomic (or negated atomic) term
            return expression


def big_AND(terms, variable):
    """ This method helps compute the n-ary logical AND of n elements for the GOOD translation.
    (This is a SPECIALIZED version of n-ary AND) Input is a set of frozensets. """
    answer = tt()
    for term in terms:
        modified_term = ff()
        for predicate in term:
            modified_term = make_OR(modified_term, predicate)
        answer = make_AND(answer, ForAll(variable, modified_term))
    return answer


def big_OR(terms, variable):
    """ This method helps compute the n-ary logical OR of n elements for the GOOD translation.
     (This is a specialized version of n-ary OR) Input is a set of frozensets. """
    answer = ff()
    for term in terms:
        modified_term = tt()
        for predicate in term:
            modified_term = make_AND(modified_term, predicate)
        answer = make_OR(answer, ThereExists(variable, modified_term))
    return answer


def n_ary_AND(expressions_list):
    """ This is a function for computing the n-ary logical AND of n elements. Input is a list. """
    answer = tt()
    for term in expressions_list:
        answer = make_AND(answer, term)
    return answer


def n_ary_OR(expressions_list):
    """ This is a function for computing the n-ary logical OR of n elements. Input is a list. """
    answer = ff()
    for term in expressions_list:
        answer = make_OR(answer, term)
    return answer


def final_translation(expression, var1, var2):
    """ This method computes the final step of the translation from FO3 into COR! """
    match expression:
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 or arg2 == var2:
            return Relation(l)
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 or arg2 == var1:
            return Converse(Relation(l))
        case ff():
            return EmptyRelation()
        case tt():
            return UniversalRelation()
        case Equals():
            return IdentityRelation()
        case OR(argument1=arg1, argument2=arg2):
            return Union(final_translation(arg1, var1, var2), final_translation(arg2, var1, var2))
        case AND(argument1=arg1, argument2=arg2):
            return Intersection(final_translation(arg1, var1, var2), final_translation(arg2, var1, var2))
        case Negation(argument=arg):
            return Complement(final_translation(arg, var1, var2))
        case ThereExists(argument=arg, variable=v) if isinstance(arg, AND):
            return Composition(final_translation(arg.argument1, var1, v), final_translation(arg.argument2, v, var2))
        case ThereExists(argument=arg, variable=v) if not isinstance(arg, AND):
            if var1 in arg.depends_on():
                return Composition(final_translation(arg, var1, v), UniversalRelation())
            elif var2 in arg.depends_on():
                return Composition(UniversalRelation(), final_translation(arg, v, var2))
        case ForAll(argument=arg, variable=v) if isinstance(arg, OR):
            return Dagger(final_translation(arg.argument1, var1, v), final_translation(arg.argument2, v, var2))
        case ForAll(argument=arg, variable=v) if not isinstance(arg, OR):
            if var1 in arg.depends_on():
                return Dagger(final_translation(arg, var1, v), EmptyRelation())
            elif var2 in arg.depends_on():
                return Dagger(EmptyRelation(), final_translation(arg, v, var2))


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = ForAll('x', ThereExists('y', OR(Predicate('A', 'x', 'y'), Predicate('B', 'x', 'z'))))

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form
    print("\nGood FO3 Translation:", T_Good_Dash(negation_normal(test_expression)))  # Good FO3 Term
    print("Nice FO3 Translation:", T_Nice(T_Good_Dash(negation_normal(test_expression))))  # Nice FO3 Term
    print("\nFinal Translation:", final_translation(T_Nice(T_Good_Dash(negation_normal(test_expression)))))
