# Authors: Sebastiaan J. C. Joosten, Anthony Brogni
# Last Changed: March 2023
""" This file is for the random generation of (untyped) FO3 expressions and for automated testing of our translation process using z3! """

import random

from timeit import default_timer
import z3  # pip install z3-solver
import pickle # save/load python objects from a file

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
            return z3.Const(arg1, SortForEverything) == z3.Const(arg2, SortForEverything)


# size parameter must be >= 1
def generate_random_FO3(size):
    """ This method generates a random FO3 expression with the specified size (depth of expression tree) """
    if size == 1:
        # Restrict the choices that can be made to allow our expression to grow to the specified size
        choice = random.randint(0, 3)
    elif size == 2:
        choice = random.randint(4, 6)
    else:
        choice = random.randint(4, 8)
    match choice:
        case 0:
            return tt()
        case 1:
            return ff()
        case 2:
            var1, var2 = ['x', 'y', 'z'][random.randint(0, 2)], ['x', 'y', 'z'][random.randint(0, 2)]
            return Equals(var1, var2)
        case 3:
            letter_choice = ['A', 'B', 'C'][random.randint(0, 2)]
            var1, var2 = ['x', 'y', 'z'][random.randint(0, 2)], ['x', 'y', 'z'][random.randint(0, 2)]
            return Predicate(letter_choice, var1, var2)
        case 4:
            var = ['x', 'y', 'z'][random.randint(0, 2)]
            return ForAll(var, generate_random_FO3(size - 1))
        case 5:
            var = ['x', 'y', 'z'][random.randint(0, 2)]
            return ThereExists(var, generate_random_FO3(size - 1))
        case 6:
            return Negation(generate_random_FO3(size - 1))
        case 7:
            size_other = random.randint(1, size - 2) # endpoint is included
            return OR(generate_random_FO3(size_other),
                      generate_random_FO3(size - size_other))
        case 8:
            size_other = random.randint(1, size - 2) # endpoint is included
            return AND(generate_random_FO3(size_other),
                       generate_random_FO3(size - size_other))


def is_normal_enough(formula):
    v = formula.depends_on()
    if 'y' in v and 'x' not in v: return False
    if 'z' in v and 'y' not in v: return False
    # TODO: Filter out formulas that are simplifiable (check the rules we currently know)
    return True


def generate_all_FO3_formulas_filtered(size):
    return [formula for formula in generate_all_FO3_formulas(size) if is_normal_enough(formula)]


# size parameter must be >= 1
def generate_all_FO3_formulas(size):
    """ This method generates ALL FO3 expressions with the specified size (depth of expression tree) """
    if size == 1:
        # Restrict the choices that can be made to allow our expression to grow to the specified size
        choices = range(0, 4)
    elif size == 2:
        choices = range(4, 7)
    else:
        choices = range(4, 8)
    for choice in choices:
        match choice:
            case 0:
                yield tt()
            case 1:
                yield ff()
            case 2:
                for var1 in ['x', 'y', 'z']:
                    for var2 in ['x', 'y', 'z']:
                        yield Equals(var1, var2)
            case 3:
                for letter_choice in ['A', 'B', 'C']:
                    for var1 in ['x', 'y', 'z']:
                        for var2 in ['x', 'y', 'z']:
                            yield Predicate(letter_choice, var1, var2)
            case 4:
                for var in ['x', 'y', 'z']:
                    for formula in generate_all_FO3_formulas(size - 1):
                        yield ForAll(var, formula)
            case 5:
                for var in ['x', 'y', 'z']:
                    for formula in generate_all_FO3_formulas(size - 1):
                        yield ThereExists(var, formula)
            case 6:
                for formula in generate_all_FO3_formulas(size - 1):
                    yield Negation(formula)
            case 7:
                for size_other in range(1, size-1): # endpoint is excluded
                    for formula in generate_all_FO3_formulas(size_other):
                        for formula2 in generate_all_FO3_formulas(size - size_other):
                            yield OR(formula, formula2)
            case 8:
                for size_other in range(1, size-1): # endpoint is excluded
                    for formula in generate_all_FO3_formulas(size_other):
                        for formula2 in generate_all_FO3_formulas(size - size_other):
                            yield AND(formula, formula2)


# size parameter must be >= 1
def generate_all_COR_formulas(size):
    """ This method generates ALL COR expressions with the specified size (depth of expression tree) """
    if size == 1:
        # Restrict the choices that can be made to allow our expression to grow to the specified size
        choices = range(0, 4)
    elif size == 2:
        choices = range(4, 6)
    else:
        choices = range(4, 9)
    for choice in choices:
        match choice:
            case 0:
                yield UniversalRelation()
            case 1:
                yield EmptyRelation()
            case 2:
                yield IdentityRelation()
            case 3:
                for letter_choice in ['A', 'B', 'C']:
                    yield Relation(letter_choice)
            case 4:
                for formula in generate_all_COR_formulas(size - 1):
                    yield Complement(formula)
            case 5:
                for formula in generate_all_COR_formulas(size - 1):
                    yield Converse(formula)
            case 6:
                for size_other in range(1, size-1): # endpoint is excluded
                    for formula in generate_all_COR_formulas(size_other):
                        for formula2 in generate_all_COR_formulas(size - size_other):
                            yield Dagger(formula, formula2)
            case 7:
                for size_other in range(1, size-1): # endpoint is excluded
                    for formula in generate_all_COR_formulas(size_other):
                        for formula2 in generate_all_COR_formulas(size - size_other):
                            yield Composition(formula, formula2)
            case 8:
                for size_other in range(1, size-1): # endpoint is excluded
                    for formula in generate_all_COR_formulas(size_other):
                        for formula2 in generate_all_COR_formulas(size - size_other):
                            yield Union(formula, formula2)
            case 9:
                for size_other in range(1, size-1): # endpoint is excluded
                    for formula in generate_all_COR_formulas(size_other):
                        for formula2 in generate_all_COR_formulas(size - size_other):
                            yield Intersection(formula, formula2)


def make_FO3_expression_closed(expression):
    """ This method takes any FO3 expression and makes it closed by applying universal quantifiers (ForAll) to any
     free variables. """
    closed_expression = expression
    for variable in expression.free_variables():
        closed_expression = ForAll(variable, closed_expression)
    return closed_expression


def random_FO3_tester(attempts, size):
    """ This automated testing method will run the specified number of attempts while counting how many are succesful
    and displaying the results to the terminal. Each attempt entails generating a random FO3 expression with the
    specified size and then beginning our forwards and backwards translation processes,
    using z3 to verify the equivalence of the original FO3 term and the result. """
    successes = 0
    for attempt in range(attempts):
        test = make_FO3_expression_closed(generate_random_FO3(size))
        return_value = test_with_z3(test)
        if return_value < 0:
            print('WARNING: TEST FAILED!')
            return False  # This is just for initial testing purposes
        else:
            successes += return_value
    print(f'{successes}/{attempts} were successful without timing out! That is {100 * successes / attempts}% accuracy')
    return True


def test_with_z3(fo3_expression) -> int:
    """ This method uses z3 to test the equivalence of the orginal expression with the result of our fowards and
    backwards translation process, returning True if the two expressions are proven to be equivalent and False
    otherwise. """
    # Test expression must be a closed formula
    print("\nOriginal Expression: ", fo3_expression)  # Original expression
    nnf = negation_normal(fo3_expression)
    print("Negation Normal Form:", nnf)  # Negation Normal Form
    first_nice = T_Nice(nnf)
    print("Nice FO3 Translation:", first_nice)
    good = T_Good_Dash(first_nice)
    print("Good FO3 Translation:", good)  # Good FO3 Term
    nice = T_Nice(good)
    print("Nice FO3 Translation:", nice)  # Nice FO3 Term
    final = final_translation(nice, 'x', 'y')
    print("Final Translation:   ", final)
    back = ForAll('a', ForAll('b', final.translate('a', 'b')))
    print("Something that should be equivalent to the original:", back)
    s = z3.Solver()
    s.add(z3.Not(asZ3(fo3_expression) == asZ3(back)))
    s.set("timeout", 1000)  # If this returns an error, update the z3 module
    z3result = s.check()
    if z3result == z3.sat:
        print("\nZ3 found a bug! (this is bad!)")
        print(s.model())
        print("\nZ3 lhs: ", asZ3(fo3_expression))
        print("\nZ3 rhs: ", asZ3(back))
        print("\nZ3 constraint: ", z3.Not(asZ3(fo3_expression) == asZ3(back)))
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


def translation_speed_test(number, size, generate_new_terms=False):
    results = open("translation_speed_test_results.txt", "w+", encoding="utf8")
    
    # Generate random FO3 terms and save them to a file
    if generate_new_terms:
        list = []
        for num in range(number):
            list.append(make_FO3_expression_closed(generate_random_FO3(size)))
        with open('size_20_fo3_formulas.pickle', 'wb') as file:
            pickle.dump(list, file, protocol=pickle.HIGHEST_PROTOCOL)
    
    # Read FO3 terms from a file and translate them
    with open('size_20_fo3_formulas.pickle', 'rb') as file:
        formulas = pickle.load(file)
    start = default_timer()  # Time how long this takes
    for formula in formulas:
        translation = final_translation(T_Nice(T_Good_Dash(T_Nice(negation_normal(formula)))), 'x', 'y')
        results.write(str(formula) + " -> " + str(translation) + "\n")
    results.write(f"\nFinished translation {number} random size={size} FO3 formulas in {default_timer() - start} seconds!")


if __name__ == "__main__":
    for n in range(1, 25):
        if random_FO3_tester(n, n):
            pass
        else:
            break
