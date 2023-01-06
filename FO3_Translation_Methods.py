# Authors: Sebastiaan Joosten, Anthony Brogni

from COR_Expressions import *
from FO3_Expressions import *
from List_Methods import *


def T_Good_Dash(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    match expression:
        case ForAll(argument=arg, variable=var):
            lists = T_Good_ForAll(arg)
            return n_ary_AND([ForAll(var, n_ary_OR([term for term in terms])) for terms in lists])
        case ThereExists(argument=arg, variable=var):
            lists = T_Good_ThereExists(arg)
            return n_ary_OR([ThereExists(var, n_ary_AND([term for term in terms])) for terms in lists])
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
            lists = T_Good_ForAll(arg)
            return [[n_ary_AND([ForAll(var, n_ary_OR([term for term in terms])) for terms in lists])]]
        case ThereExists(argument=arg, variable=var):
            lists = T_Good_ThereExists(arg)
            return [[n_ary_OR([ThereExists(var, n_ary_AND([term for term in terms])) for terms in lists])]]
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
            lists = T_Good_ForAll(arg)
            return [[n_ary_AND([ForAll(var, n_ary_OR([term for term in terms])) for terms in lists])]]
        case ThereExists(argument=arg, variable=var):
            lists = T_Good_ThereExists(arg)
            return [[n_ary_OR([ThereExists(var, n_ary_AND([term for term in terms])) for terms in lists])]]
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
            lhs_list = [term for term in terms if var not in term.free_variables()]  # does NOT depend on the variable
            rhs_list = [term for term in terms if var in term.free_variables()]  # DOES depend on the variable
            lhs = T_Nice(n_ary_AND(lhs_list))
            rhs = make_ThereExists(var, T_Nice(n_ary_AND(rhs_list)))
            return make_AND(lhs, rhs)
        case ForAll(argument=arg, variable=var):  # ForAll Case
            terms = arg.getAsOrList()
            lhs_list = [term for term in terms if var not in term.free_variables()]  # does NOT depend on the variable
            rhs_list = [term for term in terms if var in term.free_variables()]  # DOES depend on the variable
            lhs = T_Nice(n_ary_OR(lhs_list))
            rhs = make_ForAll(var, T_Nice(n_ary_OR(rhs_list)))
            return make_OR(lhs, rhs)
        case _:  # This case is only reached if expression is an atomic (or negated atomic) term
            return expression


def n_ary_AND(expressions_list):
    """ This is a function for computing the n-ary logical AND of n elements. Input is a list of elements. """
    answer = tt()
    for term in expressions_list:
        answer = make_AND(answer, term)
    return answer


def n_ary_OR(expressions_list):
    """ This is a function for computing the n-ary logical OR of n elements. Input is a list of elements. """
    answer = ff()
    for term in expressions_list:
        answer = make_OR(answer, term)
    return answer


def final_translation(expression, var1, var2):
    """ This method computes the final step of the translation from FO3 into COR! """
    match expression:
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == arg1:
            return Composition(Intersection(Relation(l), IdentityRelation()), UniversalRelation())
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == arg1:
            return Composition(UniversalRelation(), Intersection(Relation(l), IdentityRelation()))
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == var2:
            return Relation(l)
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == var1:
            return Converse(Relation(l))
        case ff():
            return EmptyRelation()
        case tt():
            return UniversalRelation()
        case Equals(argument1=arg1, argument2=arg2) if arg1 == arg2:  # If the variables are the same
            return UniversalRelation()
        case Equals(argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == var2:
            return IdentityRelation()
        case Equals(argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == var1:
            return Converse(IdentityRelation())
        case OR(argument1=arg1, argument2=arg2):
            return Union(final_translation(arg1, var1, var2), final_translation(arg2, var1, var2))
        case AND(argument1=arg1, argument2=arg2):
            return Intersection(final_translation(arg1, var1, var2), final_translation(arg2, var1, var2))
        case Negation(argument=arg):
            return Complement(final_translation(arg, var1, var2))
        case ThereExists(argument=arg, variable=v):
            and_list = arg.getAsAndList()
            lhs = [term for term in and_list if var1 in term.free_variables()] if var1 != v else []
            rhs = [term for term in and_list if term not in lhs]
            return Composition(final_translation(n_ary_AND(lhs), var1, v), final_translation(n_ary_AND(rhs), v, var2))
        case ForAll(argument=arg, variable=v):
            or_list = arg.getAsOrList()
            lhs = [term for term in or_list if var1 in term.free_variables()] if var1 != v else []
            rhs = [term for term in or_list if term not in lhs]
            return Dagger(final_translation(n_ary_OR(lhs), var1, v), final_translation(n_ary_OR(rhs), v, var2))


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = ForAll('x', ThereExists('y', Predicate('A', 'x', 'y')))

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form
    print("\nGood FO3 Translation:", T_Good_Dash(negation_normal(test_expression)))  # Good FO3 Term
    print("Nice FO3 Translation:", T_Nice(T_Good_Dash(negation_normal(test_expression))))  # Nice FO3 Term
    print("\nFinal Translation:", final_translation(T_Nice(T_Good_Dash(negation_normal(test_expression))), 'x', 'y'))
