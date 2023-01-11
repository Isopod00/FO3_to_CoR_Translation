import FO3_Translation_Methods
from Typed_COR_Expressions import *


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


# For this method, var1 and var2 are Typed_Variable objects
def typed_final_translation(expression, var1, var2):
    """ This method computes the final step of the translation from FO3 into COR! """
    match expression:
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == arg1:
            return Typed_Composition(
                Typed_Intersection(Typed_Relation(l, var1.set, var2.set), Typed_IdentityRelation(var1.set, var2.set)),
                Typed_UniversalRelation(var1.set, var2.set))
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == arg1:
            return Typed_Composition(Typed_UniversalRelation(var1.set, var2.set),
                                     Typed_Intersection(Typed_Relation(l, var1.set, var2.set),
                                                        Typed_IdentityRelation(var1.set, var2.set)))
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == var2:
            return Typed_Relation(l, var1.set, var2.set)
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == var1:
            return Typed_Converse(Typed_Relation(l, var1.set, var2.set))
        case ff():
            return Typed_EmptyRelation(var1.set, var2.set)
        case tt():
            return Typed_UniversalRelation(var1.set, var2.set)
        case Equals(argument1=arg1, argument2=arg2) if arg1 == arg2:  # If the variables are the same
            return Typed_UniversalRelation(var1.set, var2.set)
        case Equals(argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == var2:
            return Typed_IdentityRelation(var1.set, var2.set)
        case Equals(argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == var1:
            return Typed_Converse(Typed_IdentityRelation(var1.set, var2.set))
        case OR(argument1=arg1, argument2=arg2):
            return Typed_Union(typed_final_translation(arg1, var1, var2), typed_final_translation(arg2, var1, var2))
        case AND(argument1=arg1, argument2=arg2):
            return Typed_Intersection(typed_final_translation(arg1, var1, var2),
                                      typed_final_translation(arg2, var1, var2))
        case Negation(argument=arg):
            return Typed_Complement(typed_final_translation(arg, var1, var2))
        case ThereExists(argument=arg, variable=v):
            and_list = arg.getAsAndList()
            lhs = [term for term in and_list if var1 in term.free_variables()] if var1 != v else []
            rhs = [term for term in and_list if term not in lhs]
            return Typed_Composition(typed_final_translation(n_ary_AND(lhs), var1, v),
                                     typed_final_translation(n_ary_AND(rhs), v, var2))
        case ForAll(argument=arg, variable=v):
            or_list = arg.getAsOrList()
            lhs = [term for term in or_list if var1 in term.free_variables()] if var1 != v else []
            rhs = [term for term in or_list if term not in lhs]
            return Typed_Dagger(typed_final_translation(n_ary_OR(lhs), var1, v),
                                typed_final_translation(n_ary_OR(rhs), v, var2))
        case _:
            raise Exception("Types not compatible")


if __name__ == "__main__":
    x = Typed_Variable('x', 'Q')
    y = Typed_Variable('y', 'S')

    test_expression = ForAll(x, ThereExists(y, Predicate('A', x, y)))

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form
    print("\nGood FO3 Translation:",
          FO3_Translation_Methods.T_Good_Dash(negation_normal(test_expression)))  # Good FO3 Term
    print("Nice FO3 Translation:", FO3_Translation_Methods.T_Nice(
        FO3_Translation_Methods.T_Good_Dash(negation_normal(test_expression))))  # Nice FO3 Term
    print("\nFinal Translation:", typed_final_translation(
        FO3_Translation_Methods.T_Nice(FO3_Translation_Methods.T_Good_Dash(negation_normal(test_expression))), x, y))
