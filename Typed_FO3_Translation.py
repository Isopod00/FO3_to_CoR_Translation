# Authors: Anthony Brogni, Sebastiaan J. C. Joosten
# Last Changed: January 2023
""" This file stores the final_translation method for translating heterogeneous/typed FO3 expressions into COR. """

import FO3_Translation_Methods

from Typed_COR_Expressions import *


# For this method, var1 and var2 are Typed_Variable objects
def typed_final_translation(expression, var1, var2):
    """ This method computes the final step of the translation from (heterogeneous/typed) FO3 into COR! """
    match expression:
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == arg1:
            return make_typed_Composition(make_typed_Intersection(Typed_Relation(l, arg1.set, arg2.set),
                                                                  Typed_IdentityRelation(arg1.set, arg2.set)),
                                          Typed_UniversalRelation(var1.set, var2.set))
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == arg1:
            return make_typed_Composition(Typed_UniversalRelation(var1.set, var2.set),
                                          make_typed_Intersection(Typed_Relation(l, arg1.set, arg2.set),
                                                                  Typed_IdentityRelation(arg1.set, arg2.set)))
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == var2:
            return Typed_Relation(l, arg1.set, arg2.set)
        case Predicate(letter=l, argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == var1:
            return Typed_Converse(Typed_Relation(l, arg1.set, arg2.set))
        case ff():
            return Typed_EmptyRelation(var1.set, var2.set)
        case tt():
            return Typed_UniversalRelation(var1.set, var2.set)
        case Equals(argument1=arg1, argument2=arg2) if arg1 == arg2:  # If the variables are the same
            return Typed_UniversalRelation(var1.set, var2.set)
        case Equals(argument1=arg1, argument2=arg2) if arg1 == var1 and arg2 == var2:
            return Typed_IdentityRelation(arg1.set, arg2.set)
        case Equals(argument1=arg1, argument2=arg2) if arg1 == var2 and arg2 == var1:
            return Typed_Converse(Typed_IdentityRelation(arg1.set, arg2.set))
        case OR(argument1=arg1, argument2=arg2):
            return make_typed_Union(typed_final_translation(arg1, var1, var2),
                                    typed_final_translation(arg2, var1, var2))
        case AND(argument1=arg1, argument2=arg2):
            return make_typed_Intersection(typed_final_translation(arg1, var1, var2),
                                           typed_final_translation(arg2, var1, var2))
        case Negation(argument=arg):
            return Typed_Complement(typed_final_translation(arg, var1, var2))
        case ThereExists(argument=arg, variable=v):
            and_list = arg.getAsAndList()
            lhs = [term for term in and_list if var1 in term.free_variables()
                   ] if var1 != v else []
            rhs = [term for term in and_list if var2 in term.free_variables(
            )] if var2 != v and var1 != var2 else []
            # These terms depend only on v!
            remainder = [term for term in and_list if term not in lhs + rhs]
            lhs_translated = typed_final_translation(
                FO3_Translation_Methods.n_ary_AND(lhs), var1, v)
            rhs_translated = typed_final_translation(
                FO3_Translation_Methods.n_ary_AND(rhs), v, var2)
            remainder_translated = make_typed_Intersection(
                typed_final_translation(
                    FO3_Translation_Methods.n_ary_AND(remainder), v, v),
                Typed_IdentityRelation(v.set, v.set))
            return make_typed_Composition(lhs_translated, make_typed_Composition(remainder_translated, rhs_translated))
        case ForAll(argument=arg, variable=v):
            or_list = arg.getAsOrList()
            lhs = [term for term in or_list if var1 in term.free_variables()
                   ] if var1 != v else []
            rhs = [term for term in or_list if var2 in term.free_variables(
            )] if var2 != v and var1 != var2 else []
            # These terms depend only on v!
            remainder = [term for term in or_list if term not in lhs + rhs]
            lhs_translated = typed_final_translation(
                FO3_Translation_Methods.n_ary_OR(lhs), var1, v)
            rhs_translated = typed_final_translation(
                FO3_Translation_Methods.n_ary_OR(rhs), v, var2)
            remainder_translated = make_typed_Union(
                typed_final_translation(
                    FO3_Translation_Methods.n_ary_OR(remainder), v, v),
                Typed_Complement(Typed_IdentityRelation(v.set, v.set)))
            return Typed_Dagger(lhs_translated, Typed_Dagger(remainder_translated, rhs_translated))
        case _:
            raise Exception(
                f'Types not Compatible! Expression: {expression} var1: {var1} var2: {var2}')


if __name__ == "__main__":
    x = Typed_Variable('x', 'A')
    y = Typed_Variable('y', 'B')
    z = Typed_Variable('y', 'C')
    w = Typed_Variable('w', 'D')

    test_expression = ThereExists(x, ThereExists(
        y, ThereExists(z, ThereExists(w, Predicate("P", x, w)))))

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(
        test_expression))  # Negation Normal Form
    print("\nGood FO3 Translation:",
          FO3_Translation_Methods.T_Good_Dash(negation_normal(test_expression)))  # Good FO3 Term
    print("Nice FO3 Translation:", FO3_Translation_Methods.T_Nice(
        FO3_Translation_Methods.T_Good_Dash(negation_normal(test_expression))))  # Nice FO3 Term
    print("\nFinal Translation:", typed_final_translation(
        FO3_Translation_Methods.T_Nice(
            FO3_Translation_Methods.T_Good_Dash(negation_normal(test_expression))),
        Typed_Variable('x', "Left"), Typed_Variable('y', "Right")))
