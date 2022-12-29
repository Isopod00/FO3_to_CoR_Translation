# Authors: Sebastiaan Joosten, Anthony Brogni

import random

import z3  # pip install z3-solver

from FO3_Translation_Methods import *

SortForEverything = z3.DeclareSort('SomeSort')


def asZ3(expression):
    """ This method computes the z3 representation of an FO3 formula """
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


def generate_random_COR(current_depth, max_depth):
    """ This method generates a random COR expression with the specified maximum depth """
    if current_depth >= max_depth:
        choice = random.randint(0, 4)
    else:
        choice = random.randint(0, 9)
    match choice:
        case 0:
            return UniversalRelation()
        case 1:
            return EmptyRelation()
        case 2:
            return IdentityRelation()
        case 3:
            choice2 = random.randint(0, 25)
            return Converse(Relation(chr(choice2 + 65)))
        case 4:
            choice2 = random.randint(0, 25)
            return Relation(chr(choice2 + 65))
        case 5:
            return Complement(generate_random_COR(current_depth + 1, max_depth))
        case 6:
            return Union(generate_random_COR(current_depth + 1, max_depth),
                         generate_random_COR(current_depth + 1, max_depth))
        case 7:
            return Intersection(generate_random_COR(current_depth + 1, max_depth),
                                generate_random_COR(current_depth + 1, max_depth))
        case 8:
            return Composition(generate_random_COR(current_depth + 1, max_depth),
                               generate_random_COR(current_depth + 1, max_depth))
        case 9:
            return Dagger(generate_random_COR(current_depth + 1, max_depth),
                          generate_random_COR(current_depth + 1, max_depth))


def random_COR_tester(attempts, max_depth):
    """ This automated testing method will run the specified number of attempts while counting how many are succesful
    and displaying the results to the terminal. Each attempt entails generating a random COR expression with the
    specified maximum depth, converting that random expression into an FO3 expression, and then beginning our forwards
    and backwards translation processes, using z3 to verify the equivalence of the original FO3 term and the result. """
    successes = 0
    for attempt in range(attempts):
        test = generate_random_COR(0, max_depth)
        print('Generated COR term:', test)
        test = test.translate('x', 'y')
        if test_with_z3(test):
            successes += 1
        else:
            print('WARNING: TEST FAILED!')
            return  # TODO: We don't need to keep this return but it helps for now
    print(f'{successes} / {attempts} were successful! That is {100 * successes / attempts}% accuracy')


def test_with_z3(fo3_expression) -> bool:
    """ This method uses z3 to test the equivalence of the orginal expression with the result of our fowards and
    backwards translation process, returning True if the two expressions are proven to be equivalent and False
     otherwise. """
    print("Original Expression:", fo3_expression)  # Original expression
    nnf = negation_normal(fo3_expression)
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
    s.add(z3.Not(asZ3(fo3_expression) == asZ3(back)))
    s.set("timeout", 600)  # If this returns an error, update z3!
    z3result = s.check()
    if z3result == z3.sat:
        print("\nZ3 found a bug! (this is bad!)")
        print(s.model())
        print("\nZ3 lhs: ", asZ3(fo3_expression))
        print("\nZ3 rhs: ", asZ3(back))
        print("\nZ3 constraint: ", z3.Not(asZ3(fo3_expression) == asZ3(back)))
        return False
    elif z3result == z3.unsat:
        print("\nZ3 proved that the round-trip returned something equivalent (this is good!)")
        return True
    else:
        print("\nZ3 returned ", z3result)
        return False
        # TODO: if Z3 times out, we should try with a finite sort instead,
        # Here's how to get a finite sort of three elements:
        # S, (a, b, c) = z3.EnumSort('round', ['a','b','c'])


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    random_COR_tester(200, 1)
