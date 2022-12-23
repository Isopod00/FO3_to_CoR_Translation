# Authors: Sebastiaan Joosten, Anthony Brogni

import z3  # pip install z3-solver

from FO3_Translation_Methods import *

SortForEverything = z3.DeclareSort('SomeSort')


def asZ3(expression):
    match expression:
        case tt():
            return True
        case ff():
            return False
        case ForAll():
            return z3.ForAll([z3.Const(expression.variable, SortForEverything)], asZ3(expression.argument))
        case ThereExists():
            return z3.Exists([z3.Const(expression.variable, SortForEverything)], asZ3(expression.argument))
        case AND():
            return z3.And(asZ3(expression.argument1), asZ3(expression.argument2))
        case OR():
            return z3.Or(asZ3(expression.argument1), asZ3(expression.argument2))
        case Predicate():
            return z3.Function(expression.letter, SortForEverything, SortForEverything, z3.BoolSort())(
                z3.Const(expression.argument1, SortForEverything), z3.Const(expression.argument2, SortForEverything))
        case Negation():
            return z3.Not(asZ3(expression.argument))
        case Equals():
            return z3.Function("Equals", SortForEverything, SortForEverything, z3.BoolSort())(
                z3.Const(expression.argument1, SortForEverything), z3.Const(expression.argument2, SortForEverything))


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    # Test expression must be a closed formula
    test_expression = ForAll('z', ForAll('x', AND(ThereExists('y', Predicate('A', 'x', 'y')),Predicate('A', 'z', 'y'))))
    print("Original Expression:", test_expression)  # Original expression
    nnf = negation_normal(test_expression)
    print("Negation Normal Form:", nnf)  # Negation Normal Form
    good = T_Good_Dash(nnf)
    print("\nGood FO3 Translation:", good)  # Good FO3 Term
    nice = T_Nice(good)
    print("Nice FO3 Translation:", nice)  # Nice FO3 Term
    final = final_translation(nice)
    print("\nFinal Translation:", final)
    back = ForAll('a', ForAll('b', final.translate('a', 'b')))
    print("\nSomething that should be equivalent to the original: ", back)
    s = z3.Solver()
    s.add(z3.Not(asZ3(test_expression) == asZ3(back)))
    s.set("timeout", 600)  # If this returns an error, update z3!
    z3result = s.check()
    if z3result == z3.sat:
        print("\nZ3 found a bug! (this is bad!)")
        print(s.model())
        print("\nZ3 lhs: ", asZ3(test_expression))
        print("\nZ3 rhs: ", asZ3(back))
        print("\nZ3 constraint: ", z3.Not(asZ3(test_expression) == asZ3(back)))
    elif z3result == z3.unsat:
        print("\nZ3 proved that the round-trip returned something equivalent (this is good!)")
    else:
        print("\nZ3 returned ", z3result)
        # TODO: if Z3 times out, we should try with a finite sort instead,
        # Here's how to get a finite sort of three elements:
        # S, (a, b, c) = z3.EnumSort('round', ['a','b','c'])
