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


def generate_random_FO3(max_depth):
    """ This recursive method generates a random FO3 expression with the specified maximum depth """
    if max_depth <= 0:
        # Restrict the choices that can be made if the maximum depth has been reached
        choice = random.randint(0, 3)
    else:
        choice = random.randint(0, 8)
    match choice:
        case 0:
            return tt()
        case 1:
            return ff()
        case 2:
            var1 = ['x', 'y', 'z'][random.randint(0, 2)]
            # This code ensures we don't get the same variable twice
            var2 = var1
            while var2 == var1:
                var2 = ['x', 'y', 'z'][random.randint(0, 2)]
            return Equals(var1, var2)
        case 3:
            letter_choice = chr(random.randint(0, 25) + 65)
            var1 = ['x', 'y', 'z'][random.randint(0, 2)]
            # This code ensures we don't get the same variable twice
            var2 = var1
            while var2 == var1:
                var2 = ['x', 'y', 'z'][random.randint(0, 2)]
            return Predicate(letter_choice, var1, var2)
        case 4:
            return Negation(generate_random_FO3(max_depth - 1))
        case 5:
            return OR(generate_random_FO3(max_depth - 1),
                      generate_random_FO3(max_depth - 1))
        case 6:
            return AND(generate_random_FO3(max_depth - 1),
                       generate_random_FO3(max_depth - 1))
        case 7:
            var = ['x', 'y', 'z'][random.randint(0, 2)]
            return ForAll(var, generate_random_FO3(max_depth - 1))
        case 8:
            var = ['x', 'y', 'z'][random.randint(0, 2)]
            return ThereExists(var, generate_random_FO3(max_depth - 1))


def make_FO3_expression_closed(expression):
    """ This method takes any FO3 expression and makes it closed by applying universal quantifiers (ForAll) to any
     free variables. """
    closed_expression = expression
    for variable in expression.free_variables():
        closed_expression = ForAll(variable, closed_expression)
    return closed_expression


def random_FO3_tester(attempts, max_depth):
    """ This automated testing method will run the specified number of attempts while counting how many are succesful
    and displaying the results to the terminal. Each attempt entails generating a random FO3 expression with the
    specified maximum depth and then beginning our forwards and backwards translation processes,
    using z3 to verify the equivalence of the original FO3 term and the result. """
    successes = 0
    for attempt in range(attempts):
        test = make_FO3_expression_closed(generate_random_FO3(max_depth))
        print('Generated closed FO3 term:', test)
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
    # Test expression must be a closed formula
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
    random_FO3_tester(200, 0)
