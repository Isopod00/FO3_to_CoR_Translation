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
        case ForAll(argument=arg, variable=var):
            return z3.ForAll([z3.Const(var, SortForEverything)], asZ3(arg))
        case ThereExists(argument=arg, variable=var):
            return z3.Exists([z3.Const(var, SortForEverything)], asZ3(arg))
        case AND(argument1=arg1, argument2=arg2):
            return z3.And(asZ3(arg1), asZ3(arg2))
        case OR(argument1=arg1, argument2=arg2):
            return z3.Or(asZ3(arg1), asZ3(arg2))
        case Predicate(letter=a, argument1=arg1, argument2=arg2):
            return z3.Function(a, SortForEverything, SortForEverything, z3.BoolSort())(
                z3.Const(arg1, SortForEverything), z3.Const(arg2, SortForEverything))
        case Negation(argument=arg):
            return z3.Not(asZ3(arg))
        case Equals(argument1=arg1, argument2=arg2):
            return z3.Function("Equals", SortForEverything, SortForEverything, z3.BoolSort())(
                z3.Const(arg1, SortForEverything), z3.Const(arg2, SortForEverything))


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    # Test expression must be a closed formula
    test_expression = OR(ForAll('z', OR(Negation(Predicate('A', 'x', 'z')), Negation(Predicate('B', 'z', 'y')))), AND(Predicate('C', 'y', 'x'), Equals('x', 'y')))
    print("Original Expression:", test_expression)  # Original expression
    nnf = negation_normal(test_expression)
    print("Negation Normal Form:", nnf)  # Negation Normal Form
    good = T_Good_Dash(nnf)
    print("\nGood FO3 Translation:", good)  # Good FO3 Term
    nice = T_Nice(good)
    print("Nice FO3 Translation:", nice)  # Nice FO3 Term
    final = final_translation(nice, 'x', 'y')
    print("\nFinal Translation:", final)
    back = final.translate('x', 'y')
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
