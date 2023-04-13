# Authors: Sebastiaan J. C. Joosten, Anthony Brogni
# Last Changed: March 2023
""" This file is for the random generation of typed FO3 expressions and for automated testing of our typed translation process using z3! """

import random

import z3  # pip install z3-solver

from Typed_FO3_Translation import *


# size parameter must be >= 1
def generate_random_typed_FO3(size, allowed_variables):
    """ This method generates a random typed FO3 expression with the specified size (depth of expression tree) """
    if size == 1:
        # Restrict the choices that can be made to allow our expression to grow to the specified size
        choice = random.randint(0, 3)
    elif size == 2:
        choice = random.randint(4, 6)
    else:
        choice = random.randint(4, 8)
    match choice:
        case 0:  # True
            return tt()
        case 1:  # False
            return ff()
        case 2:  # Equals
            var1 = allowed_variables[random.randint(0, 2)]
            random.shuffle(allowed_variables)
            # This ensures that both variables will come from the same set
            var2 = [var for var in allowed_variables if var.set == var1.set].pop()
            return Equals(var1, var2)
        case 3:  # Predicate
            letter_choice = ['A', 'B', 'C'][random.randint(0, 2)]
            var1, var2 = allowed_variables[random.randint(0, 2)], allowed_variables[random.randint(0, 2)]
            return Predicate(letter_choice, var1, var2)
        case 4:  # ForAll
            var = Typed_Variable(['x', 'y', 'z'][random.randint(0, 2)], ['Q', 'R', 'S', 'T'][random.randint(0, 3)])
            new_allowed_variables = allowed_variables.copy()
            new_allowed_variables[random.randint(0, 2)] = var
            return ForAll(var, generate_random_typed_FO3(size - 1, new_allowed_variables))
        case 5:  # ThereExists
            var = Typed_Variable(['x', 'y', 'z'][random.randint(0, 2)], ['Q', 'R', 'S', 'T'][random.randint(0, 3)])
            new_allowed_variables = allowed_variables.copy()
            new_allowed_variables[random.randint(0, 2)] = var
            return ThereExists(var, generate_random_typed_FO3(size - 1, new_allowed_variables))
        case 6:  # Negation
            return Negation(generate_random_typed_FO3(size - 1, allowed_variables))
        case 7:  # OR
            size_other = random.randint(1, size - 1)
            return OR(generate_random_typed_FO3(size_other, allowed_variables),
                      generate_random_typed_FO3(size - size_other, allowed_variables))
        case 8:  # AND
            size_other = random.randint(1, size - 1)
            return AND(generate_random_typed_FO3(size_other, allowed_variables),
                       generate_random_typed_FO3(size - size_other, allowed_variables))


def random_typed_FO3_tester(attempts, size):
    """ This automated testing method will run the specified number of attempts while counting how many are succesful
    and displaying the results to the terminal. Each attempt entails generating a random FO3 expression with the
    specified size and then beginning our forwards and backwards translation processes,
    using z3 to verify the equivalence of the original FO3 term and the result. """
    successes = 0
    for attempt in range(attempts):
        # Generate 3 random variables
        x = Typed_Variable(['x', 'y', 'z'][random.randint(0, 2)], ['Q', 'R', 'S', 'T'][random.randint(0, 3)])
        y = Typed_Variable(['x', 'y', 'z'][random.randint(0, 2)], ['Q', 'R', 'S', 'T'][random.randint(0, 3)])
        z = Typed_Variable(['x', 'y', 'z'][random.randint(0, 2)], ['Q', 'R', 'S', 'T'][random.randint(0, 3)])

        test = make_typed_FO3_expression_closed(generate_random_typed_FO3(size, [x, y, z]))
        return_value = test_typed_with_z3(test)
        if return_value < 0:
            print('WARNING: TEST FAILED!')
            return False  # This is just for initial testing purposes
        else:
            successes += return_value
    print(f'{successes}/{attempts} were successful without timing out! That is {100 * successes / attempts}% accuracy')
    return True


def typed_asZ3(expression):
    """ This method computes the z3 representation of an FO3 formula """
    match expression:
        case tt():
            return True
        case ff():
            return False
        case ForAll(argument=arg, variable=var):
            return z3.ForAll([z3.Const(str(var), z3.DeclareSort(var.set))], typed_asZ3(arg))
        case ThereExists(argument=arg, variable=var):
            return z3.Exists([z3.Const(str(var), z3.DeclareSort(var.set))], typed_asZ3(arg))
        case AND(argument1=arg1, argument2=arg2):
            return z3.And(typed_asZ3(arg1), typed_asZ3(arg2))
        case OR(argument1=arg1, argument2=arg2):
            return z3.Or(typed_asZ3(arg1), typed_asZ3(arg2))
        case Predicate(letter=a, argument1=arg1, argument2=arg2):
            return z3.Function(a, z3.DeclareSort(arg1.set), z3.DeclareSort(arg2.set), z3.BoolSort())(
                z3.Const(str(arg1), z3.DeclareSort(arg1.set)), z3.Const(str(arg2), z3.DeclareSort(arg2.set)))
        case Negation(argument=arg):
            return z3.Not(typed_asZ3(arg))
        case Equals(argument1=arg1, argument2=arg2):
            return z3.Const(str(arg1), z3.DeclareSort(arg1.set)) == z3.Const(str(arg2), z3.DeclareSort(arg2.set))


def test_typed_with_z3(fo3_expression) -> int:
    """ This method uses z3 to test the equivalence of the orginal expression with the result of our fowards and
    backwards translation process, returning True if the two expressions are proven to be equivalent and False
    otherwise. """
    # Test expression must be a closed formula
    print("\nOriginal Expression:   ", fo3_expression)  # Original expression
    nnf = negation_normal(fo3_expression)
    print("Negation Normal Form:  ", nnf)  # Negation Normal Form
    first_nice = FO3_Translation_Methods.T_Nice(nnf)
    print("Nice FO3 Translation:", first_nice)
    good = FO3_Translation_Methods.T_Good_Dash(first_nice)
    print("Good FO3 Translation:  ", good)  # Good FO3 Term
    nice = FO3_Translation_Methods.T_Nice(good)
    print("Nice FO3 Translation:  ", nice)  # Nice FO3 Term
    final = typed_final_translation(nice, Typed_Variable('x', "Left"), Typed_Variable('y', "Right"))
    print("\nFinal Translation:   ", final)
    back = FO3_Translation_Methods.T_Nice(ForAll(Typed_Variable('a', 'A'), ForAll(Typed_Variable('b', 'B'), final.translate('a', 'b'))))
    print("Something that should be equivalent to the original:", back)
    s = z3.Solver()
    s.add(z3.Not(typed_asZ3(fo3_expression) == typed_asZ3(back)))
    s.set("timeout", 1000)  # If this returns an error, update the z3 module
    z3result = s.check()
    if z3result == z3.sat:
        print("\nZ3 found a bug! (this is bad!)")
        print(s.model())
        print("\nZ3 lhs: ", typed_asZ3(fo3_expression))
        print("\nZ3 rhs: ", typed_asZ3(back))
        print("\nZ3 constraint: ", z3.Not(typed_asZ3(fo3_expression) == typed_asZ3(back)))
        return -1
    elif z3result == z3.unsat:
        print("\nZ3 proved that the round-trip returned something equivalent (this is good!)")
        return 1
    else:
        print("\nZ3 timed out and returned ", z3result)
        return 0
        # TODO: if Z3 times out, we should try with a finite sort instead,
        # Here's how to get a finite sort of three elements:
        # S, (a, b, c) = z3.EnumSort('round', ['a','b','c'])


def make_typed_FO3_expression_closed(expression):
    """ This method takes any FO3 expression and makes it closed by applying universal quantifiers (ForAll) to any
     free variables. """
    closed_expression = expression
    for variable in expression.free_variables():
        closed_expression = ForAll(variable, closed_expression)
    return closed_expression


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    for n in range(1, 25):
        if random_typed_FO3_tester(n, n):
            pass
        else:
            break
