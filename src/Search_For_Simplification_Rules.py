# Author: Anthony Brogni
# Last Changed: May 2023

""" The code in this file is for finding all possible COR simplification rules up to a specified size.
We utilize multiprocessing across multiple cores to make the search faster. """

from tqdm import tqdm
import multiprocessing
from timeit import default_timer
import random

import multiset  # pip install multiset
import numpy  # pip install numpy
import z3  # pip install z3-solver
import pickle  # save/load python objects from a file

import Testing
from FO3_Expressions import *
import COR_Expressions
import Typed_COR_Expressions

import Simplify
import Typed_Simplify


def look_for_simplification_rules(size, cpu_cores1, timeout=3600):
    """ This method searches for simplification rules of a given size by utilizing the specified number of cpu cores """
    global cor_dict

    print(
        f"A search for simplification rules of size {size} has started (using {cpu_cores1} logical processors)")
    start = default_timer()  # Time how long this takes

    # Generate ALL formulas of the specified size and split this list into equally-sized chunks
    formulas = [formula for formula in list(Testing.generate_all_COR_formulas(size))
                if (not is_already_simplifiable(formula))
                and alphabetical_order_check(str(formula))]
    print(f"Searching {len(formulas)} formulas of this size.")
    random.shuffle(formulas)  # for more accurate time measurement
    equal_chunks = enumerate(map(list, numpy.array_split(numpy.array(
        formulas), len(formulas))))  # equal_chunks will be a list of numpy arrays

    results = []

    if cpu_cores1 == 1:
        # Using single-core for the progress bar:
        for array in tqdm(equal_chunks):
            results.append(compute_chunk(list(array), size, timeout))
    else:
        # Create our pool of tasks
        with multiprocessing.Pool(cpu_cores1) as pool:
            for array in equal_chunks:
                # convert the numpy arrays to lists
                results.append(pool.apply_async(
                    compute_chunk, args=(array, size, timeout)))
            pool.close()
            pool.join()
            for i in range(len(results)):
                results[i] = results[i].get()

    # Construct the sets which will contain the final answers
    final_cor_result = set()
    for result in results:
        final_cor_result = final_cor_result.union(result)
    for (l, r) in final_cor_result:
        cor_dict[l] = r

    # Save the rule dictionary to file
    with open('src/cor_dict.pickle', 'wb') as file:
        pickle.dump(cor_dict, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(
        f"The search for simplification rules of size {size} finished in {default_timer() - start} seconds!")


def alphabetical_order_check(string):
    """ Prevent generating duplicate rules by only allowing rules with relations in alphabetical order """
    next_letter = ord('A')
    for char in string:
        if ord(char) == next_letter:
            next_letter += 1
        elif (ord(char) in [ord('A'), ord('B'), ord('C')]) and (ord(char) > next_letter):
            return False
    return True  # This rule passed the test!


def is_already_simplifiable(formula, typed=False) -> bool:
    """ If a formula is already simplifiable, then we don't need to consider it again. """
    return (not (str(simplify(formula)) == str(formula))) if not typed else (not (str(simplify_typed(formula)) == str(formula)))


def simplify(expression):
    """ Simplify a COR expression using the code we have generated in src/Simplify.py """
    match expression:
        case COR_Expressions.Complement(argument=arg):
            return Simplify.simplify(COR_Expressions.Complement(simplify(arg)))[1]
        case COR_Expressions.Converse(argument=arg):
            return Simplify.simplify(COR_Expressions.Converse(simplify(arg)))[1]
        case COR_Expressions.Union(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Union(simplify(arg1), simplify(arg2)))[1]
        case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Intersection(simplify(arg1), simplify(arg2)))[1]
        case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Dagger(simplify(arg1), simplify(arg2)))[1]
        case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Composition(simplify(arg1), simplify(arg2)))[1]
        case _:
            return expression


def simplify_typed(expression):
    """ Simplify a typed COR expression using the code we have generated in src/Typed_Simplify.py """
    match expression:
        case Typed_COR_Expressions.Typed_Complement(argument=arg):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Complement(simplify_typed(arg)))[1]
        case Typed_COR_Expressions.Typed_Converse(argument=arg):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Converse(simplify_typed(arg)))[1]
        case Typed_COR_Expressions.Typed_Union(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Union(simplify_typed(arg1), simplify_typed(arg2)))[1]
        case Typed_COR_Expressions.Typed_Intersection(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Intersection(simplify_typed(arg1), simplify_typed(arg2)))[1]
        case Typed_COR_Expressions.Typed_Dagger(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Dagger(simplify_typed(arg1), simplify_typed(arg2)))[1]
        case Typed_COR_Expressions.Typed_Composition(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Composition(simplify_typed(arg1), simplify_typed(arg2)))[1]
        case _:
            return expression


def fully_simplify(expression, typed=False):
    """ This FULLY simplifies a COR expression by continuing to call simplify() until it cannot be simplified any further. """
    while True:
        possibly_simplified = simplify(
            expression) if not typed else simplify_typed(expression)
        if str(possibly_simplified) == str(expression):
            break  # Fully simplified!
        else:
            expression = possibly_simplified
    return expression


def compute_single(pair, fallback_enum):
    first, second = pair
    first_translated = first.translate('x', 'y')
    second_translated = second.translate('x', 'y')

    s = z3.Solver()
    s.set("timeout", 100)
    z3result = s.check(z3.Not(Testing.asZ3(first_translated)
                       == Testing.asZ3(second_translated)))
    if z3result == z3.unsat:
        return [(first, second)]
    elif z3result == z3.sat:
        return []
    else:
        q = ('Stuck at: ' + str(first) + ' -> ' + str(second))
        print('reverting to enum univ')
        s.set("timeout", 6000)

        z3result = s.check(z3.Not(Testing.asZ3(
            first_translated, fallback_enum) == Testing.asZ3(second_translated, fallback_enum)))
        if z3result == z3.unsat:
            print(q+'\nGoing into slow mode...')
            s = z3.Solver()
            s.set("timeout", 60000)
            z3result = s.check(
                z3.Not(Testing.asZ3(first_translated) == Testing.asZ3(second_translated)))
            if z3result == z3.unsat:
                print('successful rule found by using more time!')
                return [(first, second)]
            elif z3result == z3.sat:
                print('successful refutation found by using more time!')
                return []
            else:
                raise Exception("Z3 does not know the answer!\n"+q)
        elif z3result == z3.sat:
            return []  # counter example found for a small universe, this happens quite a lot
        else:
            q = ('Stuck at: ' + str(first) + ' -> ' + str(second))
            raise Exception("Z3 times out even in the finite case!\n"+q)


def compute_chunk(workpacket, size, timeout=3600):
    """ Processes one chunk of a list of formulas and returns a set of the COR simplification rules found. """

    (jobid, formulas) = workpacket
    fallback_enum, (_, _, _, _) = z3.EnumSort(
        f'univ{jobid}', ['SA', 'SB', 'SC', 'SD'])
    assert isinstance(fallback_enum, z3.SortRef)
    pairs = []
    for first in formulas:
        vars_first = multiset.Multiset(char for char in str(
            first) if ord(char) in [ord('A'), ord('B'), ord('C')])
        for second_size in range(size):
            for second in Testing.generate_all_COR_formulas(second_size):
                vars_second = multiset.Multiset(char for char in str(
                    second) if ord(char) in [ord('A'), ord('B'), ord('C')])
                if not is_already_simplifiable(second) and vars_second.issubset(vars_first):
                    pairs.append((first, second))
    return set(result for pair in pairs for result in compute_single(pair, fallback_enum))


def print_rule_dictionary(cor_dict, filename=None):
    """ This will print out the dictionary of stored rules. Set the parameter to True for printing to a .txt or False for printing to the terminal. """

    if filename == None:
        for key in cor_dict:
            print(str(key) + " -> " + str(cor_dict[key]))
    else:
        cor_rules = open(filename, "w+", encoding="utf_8")
        for key in cor_dict:
            cor_rules.write(str(key) + " -> " + str(cor_dict[key]) + "\n")


def add_tabs_to_string(string, tab_level):
    """ This is a helper function for adding a newline and the specified number of tabs to a string. """
    return ("\n" + ("\t" * tab_level) + string)


def recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, typed, arg2, rule):
    if len(arg2) == 0:
        if not typed:
            return accumulator + add_tabs_to_string("return (\"" + rule + "\", " + second.object_representation() + ")", tab_level+1)
        else:
            return accumulator + add_tabs_to_string("return (\"" + rule + "\", " + second.object_representation("expression.type()[0]", "expression.type()[1]") + ")", tab_level+1)
    else:
        (arg2Name, arg) = arg2.pop()
        if not typed:
            return accumulator + generate_helper(arg, second, arg2Name, boundVars, "", tab_level+1, arg2, rule)
        else:
            return accumulator + generate_helper_typed(arg, second, arg2Name, boundVars, "", tab_level+1, arg2, rule)


def generate_helper_typed(first, second, me, boundVars, accumulator, tab_level, arg2, rule) -> str:
    """ Generates Python code for a typed simplification rule and returns it as a string """
    t1 = first.type()[0]
    t2 = first.type()[1]
    if t1 in boundVars:
        accumulator += add_tabs_to_string(
            f"if {t1}=={me}.type()[0]:", tab_level)
        tab_level += 1
    else:
        accumulator += add_tabs_to_string(f"{t1} = {me}.type()[0]", tab_level)
        boundVars.append(t1)
    if t2 in boundVars:
        accumulator += add_tabs_to_string(
            f"if {t2}=={me}.type()[1]:", tab_level)
        tab_level += 1
    else:
        accumulator += add_tabs_to_string(f"{t2} = {me}.type()[1]", tab_level)
        boundVars.append(t2)
    match first:
        case Typed_COR_Expressions.Typed_Relation(letter=l, set1=s1, set2=s2):
            if l in boundVars:
                accumulator += add_tabs_to_string(
                    f"if str({l})==str({me}):", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return (\"" + rule + "\", " + second.object_representation("expression.type()[0]", "expression.type()[1]") + ")", tab_level+1)
                else:
                    (arg2Name, arg) = arg2.pop()
                    return accumulator + generate_helper_typed(arg, second, arg2Name, boundVars + [l], "", tab_level+1, arg2, rule)
            else:
                accumulator += add_tabs_to_string(f"{l} = {me}", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return (\"" + rule + "\", " + second.object_representation("expression.type()[0]", "expression.type()[1]") + ")", tab_level)
                else:
                    (arg2Name, arg) = arg2.pop()
                    return accumulator + generate_helper_typed(arg, second, arg2Name, boundVars + [l], "", tab_level, arg2, rule)
        case Typed_COR_Expressions.Typed_UniversalRelation(set1=s1, set2=s2):
            accumulator += add_tabs_to_string(
                f"if isinstance({me}, Typed_COR_Expressions.Typed_UniversalRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, True, arg2, rule)
        case Typed_COR_Expressions.Typed_EmptyRelation(set1=s1, set2=s2):
            accumulator += add_tabs_to_string(
                f"if isinstance({me}, Typed_COR_Expressions.Typed_EmptyRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, True, arg2, rule)
        case Typed_COR_Expressions.Typed_IdentityRelation(set1=s1, set2=s2):
            accumulator += add_tabs_to_string(
                f"if isinstance({me}, Typed_COR_Expressions.Typed_IdentityRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, True, arg2, rule)
        case Typed_COR_Expressions.Typed_Complement(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Complement):",
                                              tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper_typed(arg, second, 'arg', boundVars, accumulator, tab_level+1, arg2, rule)
        case Typed_COR_Expressions.Typed_Converse(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Converse):",
                                              tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper_typed(arg, second, 'arg', boundVars, accumulator, tab_level+1, arg2, rule)
        case Typed_COR_Expressions.Typed_Union(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Union):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)
        case Typed_COR_Expressions.Typed_Intersection(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Intersection):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)
        case Typed_COR_Expressions.Typed_Dagger(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Dagger):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)
        case Typed_COR_Expressions.Typed_Composition(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Composition):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)


def generate_helper(first, second, me, boundVars, accumulator, tab_level, arg2, rule) -> str:
    """ Generates Python code for a simplification rule and returns it as a string """
    match first:
        case COR_Expressions.Relation(letter=l):
            if l in boundVars:
                accumulator += add_tabs_to_string(
                    f"if str({l})==str({me}):", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return (\"" + rule + "\", " + second.object_representation() + ")", tab_level+1)
                else:
                    (arg2Name, arg) = arg2.pop()
                    return accumulator + generate_helper(arg, second, arg2Name, boundVars + [l], "", tab_level+1, arg2, rule)
            else:
                accumulator += add_tabs_to_string(f"{l} = {me}", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return (\"" + rule + "\", " + second.object_representation() + ")", tab_level)
                else:
                    (arg2Name, arg) = arg2.pop()
                    return accumulator + generate_helper(arg, second, arg2Name, boundVars + [l], "", tab_level, arg2, rule)
        case COR_Expressions.UniversalRelation():
            accumulator += add_tabs_to_string(
                f"if isinstance({me}, COR_Expressions.UniversalRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, False, arg2, rule)
        case COR_Expressions.EmptyRelation():
            accumulator += add_tabs_to_string(
                f"if isinstance({me}, COR_Expressions.EmptyRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, False, arg2, rule)
        case COR_Expressions.IdentityRelation():
            accumulator += add_tabs_to_string(
                f"if isinstance({me}, COR_Expressions.IdentityRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, False, arg2, rule)
        case COR_Expressions.Complement(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Complement):",
                                              tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper(arg, second, 'arg', boundVars, accumulator, tab_level+1, arg2, rule)
        case COR_Expressions.Converse(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Converse):",
                                              tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper(arg, second, 'arg', boundVars, accumulator, tab_level+1, arg2, rule)
        case COR_Expressions.Union(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Union):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)
        case COR_Expressions.Intersection(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Intersection):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)
        case COR_Expressions.Dagger(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Dagger):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)
        case COR_Expressions.Composition(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Composition):", tab_level) + add_tabs_to_string(
                f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}', argLater)], rule)


def group_by_prefix(lst):
    """ This method helps us generate prettier code by grouping rules with similar prefixes. """
    groups = {}
    for item in lst:
        try:
            prefix, remainder = (item[0], item[1:])
        except:
            continue
        if prefix in groups:
            groups[prefix].append(remainder)
        else:
            groups[prefix] = [remainder]
    for group in groups:
        if len(groups[group]) > 1:
            groups[group] = group_by_prefix(groups[group])
        else:
            groups[group] = groups[group][0]
    return groups


def write_grouped_code(python_code, groups):
    """ This method helps us generate prettier code by grouping rules with similar prefixes. """
    return_level = 999  # Arbitrarily Large Number
    for group in groups:
        tab_level = len(group.split('\t'))
        if tab_level < return_level:
            return_level = 999  # Arbitrarily Large Number
            python_code.write(group+'\n')
        if isinstance(groups[group], dict):
            write_grouped_code(python_code, groups[group])
        else:
            for line in groups[group]:
                tab_level = len(line.split('\t'))
                if tab_level < return_level:
                    return_level = 999  # Arbitrarily Large Number
                    python_code.write(line+'\n')
                    if "return" in line:
                        return_level = len(line.split('\t'))


def generate_code_from_cor_rules(cor_dict, filename, typed, reverse=False):
    """ Generates Python code in the file src/Simplify.py from a dictionary of simplification rules """
    # Create a new .py file to write to
    python_code = open(filename, "w+", encoding="utf_8")
    code = []
    for first in cor_dict:
        vars_first = multiset.Multiset(char for char in str(
            first) if ord(char) in [ord('A'), ord('B'), ord('C')])
        second = cor_dict[first]
        vars_second = multiset.Multiset(char for char in str(
            second) if ord(char) in [ord('A'), ord('B'), ord('C')])
        if vars_second.issubset(vars_first):
            code.append(generate_helper_typed(first, second, "expression", [], "", 1, [], str(first) + " = " + str(second)).split('\n')
                        if typed
                        else generate_helper(first, second, "expression", [], "", 1, [], str(first) + " = " + str(second)).split('\n')
                        )
    code = group_by_prefix(reversed(code) if reverse else code)
    if not typed:
        python_code.write("import COR_Expressions" + "\n")
    else:
        python_code.write("import Typed_COR_Expressions" + "\n")
    python_code.write("\ndef simplify(expression):")
    write_grouped_code(python_code, code)
    python_code.write(
        "\n\treturn (None, expression) # The given expression was unable to be simplified")
    # Close the file when done
    python_code.close()


def delete_generalizable_rules():
    global cor_dict
    new_dict = dict()

    for lhs in cor_dict:
        rule_applied = Simplify.simplify(lhs)[0]
        if rule_applied is not None:
            # Only keep it if the rule applied matches lhs
            if rule_applied.split(" =")[0] == str(lhs):
                new_dict[lhs] = cor_dict[lhs]
            else:
                print("Deleted Rule:", str(lhs) + " = " + str(cor_dict[lhs]))
                print("Rule Used Instead Was:", rule_applied)
        else:
            raise Exception("rule_applied should not be None. lhs =", lhs)

    # Save the new typed rule dictionary to file
    with open('src/cor_dict.pickle', 'wb') as file:
        pickle.dump(new_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
    cor_dict = new_dict


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    try:
        with open('src/cor_dict.pickle', 'rb') as file:
            cor_dict = pickle.load(file)
    except FileNotFoundError:
        cor_dict = {}
        print("No src/cor_dict.pickle file found. Using an empty dictionary (and probably creating one later)...")

    delete_generalizable_rules()

    # look_for_simplification_rules(1, 6)
    # look_for_simplification_rules(2, 6)
    # look_for_simplification_rules(3, 6)

    print_rule_dictionary(cor_dict, "src/COR_Rules.txt")
    generate_code_from_cor_rules(cor_dict, "src/Simplify.py", False)
