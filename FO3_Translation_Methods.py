# Authors: Sebastiaan Joosten, Anthony Brogni

from COR_Expressions import *
from FO3_Expressions import *


def T_Good_Dash(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_Good_ForAll(expression.argument)
        return big_AND(terms, expression.variable)
    elif isinstance(expression, ThereExists):
        terms = T_Good_ThereExists(expression.argument)
        return big_OR(terms, expression.variable)
    elif isinstance(expression, AND):
        return AND(T_Good_Dash(expression.argument1), T_Good_Dash(expression.argument2))
    elif isinstance(expression, OR):
        return OR(T_Good_Dash(expression.argument1), T_Good_Dash(expression.argument2))
    else:
        return expression


def T_Good_ThereExists(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_Good_ForAll(expression.argument)
        return {frozenset([big_AND(terms, expression.variable)])}
    elif isinstance(expression, ThereExists):
        terms = T_Good_ThereExists(expression.argument)
        return {frozenset([big_OR(terms, expression.variable)])}
    elif isinstance(expression, AND):
        answer = set()
        for set1 in T_Good_ThereExists(expression.argument1):
            for set2 in T_Good_ThereExists(expression.argument2):
                answer.add(set1.union(set2))
        return answer
    elif isinstance(expression, OR):
        return T_Good_ThereExists(expression.argument1).union(T_Good_ThereExists(expression.argument2))
    else:
        return {frozenset([expression])}


def T_Good_ForAll(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_Good_ForAll(expression.argument)
        return {frozenset([big_AND(terms, expression.variable)])}
    elif isinstance(expression, ThereExists):
        terms = T_Good_ThereExists(expression.argument)
        return {frozenset([big_OR(terms, expression.variable)])}
    elif isinstance(expression, AND):
        return T_Good_ForAll(expression.argument1).union(T_Good_ForAll(expression.argument2))
    elif isinstance(expression, OR):
        answer = set()
        for set1 in T_Good_ForAll(expression.argument1):
            for set2 in T_Good_ForAll(expression.argument2):
                answer.add(set1.union(set2))
        return answer
    else:
        return {frozenset([expression])}


def T_Nice(expression):
    """ Translation function for translating "good" FO3 terms into "nice" FO3 terms """
    if isinstance(expression, tt) or isinstance(expression, ff):
        return expression

    if isinstance(expression, OR):  # OR Case
        return OR(T_Nice(expression.argument1), T_Nice(expression.argument2))

    elif isinstance(expression, AND):  # AND Case
        return AND(T_Nice(expression.argument1), T_Nice(expression.argument2))

    elif isinstance(expression, ThereExists):  # ThereExists Case
        terms = expression.argument.getAsAndList()
        var = expression.variable
        lhs_list = [term for term in terms if var not in term.depends_on()]  # does NOT depend on the variable
        rhs_list = [term for term in terms if var in term.depends_on()]  # DOES depend on the variable
        lhs = T_Nice(n_ary_AND(lhs_list))
        rhs = make_ThereExists(var, T_Nice(n_ary_AND(rhs_list)))
        return make_AND(lhs, rhs)

    elif isinstance(expression, ForAll):  # ForAll Case
        terms = expression.argument.getAsOrList()
        var = expression.variable
        lhs_list = [term for term in terms if var not in term.depends_on()]  # does NOT depend on the variable
        rhs_list = [term for term in terms if var in term.depends_on()]  # DOES depend on the variable
        lhs = T_Nice(n_ary_OR(lhs_list))
        rhs = make_ForAll(var, T_Nice(n_ary_OR(rhs_list)))
        return make_OR(lhs, rhs)

    else:  # This case is only reached if expression is an atomic (or negated atomic) term
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


def final_translation(expression):
    """ This method computes the final step of the translation from FO3 into COR! """
    match expression:
        case Predicate():
            return Relation(expression.letter)
        case ff():
            return EmptyRelation()
        case tt():
            return UniversalRelation()
        case Equals():
            return IdentityRelation()
        case OR():
            return Union(final_translation(expression.argument1), final_translation(expression.argument2))
        case AND():
            return Intersection(final_translation(expression.argument1), final_translation(expression.argument2))
        case Negation():
            return Complement(final_translation(expression.argument))
        case ThereExists():
            argument = expression.argument
            argument = AND(argument, tt()) if not isinstance(argument, AND) else argument
            return Composition(final_translation(argument.argument1), final_translation(argument.argument2))
        case ForAll():
            argument = expression.argument
            argument = OR(argument, ff()) if not isinstance(argument, OR) else argument
            return Dagger(final_translation(argument.argument1), final_translation(argument.argument2))


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = ForAll('x', ThereExists('y', OR(Predicate('A', 'x', 'y'), Predicate('B', 'x', 'z'))))

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form
    print("\nGood FO3 Translation:", T_Good_Dash(negation_normal(test_expression)))  # Good FO3 Term
    print("Nice FO3 Translation:", T_Nice(T_Good_Dash(negation_normal(test_expression))))  # Nice FO3 Term
    print("\nFinal Translation:", final_translation(T_Nice(T_Good_Dash(negation_normal(test_expression)))))
