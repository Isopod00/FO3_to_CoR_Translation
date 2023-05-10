# Author: Anthony Brogni
# Last Changed: May 2023
""" The code in this file is for finding all possible COR simplification rules up to a specified size. We utilize multiprocessing across multiple cores to make the search faster. """
from tqdm import tqdm
import multiprocessing
from timeit import default_timer
import random

import multiset  # pip install multiset
import numpy  # pip install numpy
import z3  # pip install z3-solver
import pickle # save/load python objects from a file

import Testing
from FO3_Expressions import *
import COR_Expressions
import Typed_COR_Expressions

import Simplify
import Typed_Simplify

def look_for_simplification_rules(size, cpu_cores1, timeout=3600):
    """ This method searches for simplification rules of a given size by utilizing the specified number of cpu cores """
    global cor_dict

    print(f"A search for simplification rules of size {size} has started (using {cpu_cores1} logical processors)")
    start = default_timer()  # Time how long this takes
        
    # Generate ALL formulas of the specified size and split this list into equally-sized chunks
    formulas = [formula for formula in list(Testing.generate_all_COR_formulas(size))
                 if (not is_already_simplifiable(formula))
                 and alphabetical_order_check(str(formula))]
    print(f"Searching {len(formulas)} formulas of this size.")
    equal_chunks = numpy.array_split(numpy.array(formulas), len(formulas))  # equal_chunks will be a list of numpy arrays
    random.shuffle(equal_chunks)  # for more accurate time measurement

    results = []

    if cpu_cores1 == 1:
        # Using single-core for the progress bar:
        for array in tqdm(equal_chunks):
            results.append(compute_chunk(list(array), size, timeout))
    else:
        # Create our pool of tasks
        with multiprocessing.Pool(cpu_cores1) as pool:
            for array in equal_chunks:
                results.append(pool.apply_async(compute_chunk, args=(list(array), size, timeout)))  # convert the numpy arrays to lists
            pool.close()
            pool.join()
            for i in range(len(results)):
                results[i] = results[i].get()

    # Construct the sets which will contain the final answers
    final_cor_result = set()
    for result in results:
        final_cor_result = final_cor_result.union(result)
    for (l,r) in final_cor_result:
        cor_dict[l]=r

    # Save the rule dictionary to file
    with open('cor_dict.pickle', 'wb') as file:
        pickle.dump(cor_dict, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"The search for simplification rules of size {size} finished in {default_timer() - start} seconds!")


def alphabetical_order_check(string):
    """ Prevent generating duplicate rules by only allowing rules with relations in alphabetical order """
    next_letter = ord('A')
    for char in string:
        if ord(char) == next_letter:
            next_letter += 1
        elif (ord(char) in [ord('A'), ord('B'), ord('C')]) and (ord(char) > next_letter):
            return False
    return True # This rule passed the test!


def is_already_simplifiable(formula, typed=False) -> bool:
    """ If a formula is already simplifiable, then we don't need to consider it again. """
    return (not (str(simplify(formula)) == str(formula))) if not typed else (not (str(simplify_typed(formula)) == str(formula)))
        

def simplify(expression):
    """ Simplify a COR expression using the code we have generated in Simplify.py """
    match expression:
        case COR_Expressions.Complement(argument=arg):
            return Simplify.simplify(COR_Expressions.Complement(simplify(arg)))
        case COR_Expressions.Converse(argument=arg):
            return Simplify.simplify(COR_Expressions.Converse(simplify(arg)))
        case COR_Expressions.Union(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Union(simplify(arg1), simplify(arg2)))
        case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Intersection(simplify(arg1), simplify(arg2)))
        case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Dagger(simplify(arg1), simplify(arg2)))
        case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Composition(simplify(arg1), simplify(arg2)))
        case _:
            return expression
        

def simplify_typed(expression):
    """ Simplify a typed COR expression using the code we have generated in Typed_Simplify.py """
    match expression:
        case Typed_COR_Expressions.Typed_Complement(argument=arg):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Complement(simplify_typed(arg)))
        case Typed_COR_Expressions.Typed_Converse(argument=arg):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Converse(simplify_typed(arg)))
        case Typed_COR_Expressions.Typed_Union(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Union(simplify_typed(arg1), simplify_typed(arg2)))
        case Typed_COR_Expressions.Typed_Intersection(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Intersection(simplify_typed(arg1), simplify_typed(arg2)))
        case Typed_COR_Expressions.Typed_Dagger(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Dagger(simplify_typed(arg1), simplify_typed(arg2)))
        case Typed_COR_Expressions.Typed_Composition(argument1=arg1, argument2=arg2):
            return Typed_Simplify.simplify(Typed_COR_Expressions.Typed_Composition(simplify_typed(arg1), simplify_typed(arg2)))
        case _:
            return expression
        

def fully_simplify(expression, typed=False):
    """ This FULLY simplifies a COR expression by continuing to call simplify() until it cannot be simplified any further. """
    while True:
        possibly_simplified = simplify(expression) if not typed else simplify_typed(expression)
        if str(possibly_simplified) == str(expression):
            break # Fully simplified!
        else:
            expression = possibly_simplified
    return expression


def compute_single(pair):
    first,second=pair
    first_translated = first.translate('x', 'y')
    second_translated = second.translate('x', 'y')

    s = z3.Solver()
    s.set("timeout", 100)
    z3result = s.check(z3.Not(Testing.asZ3(first_translated) == Testing.asZ3(second_translated)))
    if z3result == z3.unsat:
        return [(first, second)]
    elif z3result == z3.sat:
        return []
    else:
        q=('Stuck at: ' + str(first) + ' -> ' + str(second))
        enum,(_,_,_,_) = z3.EnumSort('univ',['SA','SB','SC','SD'])
        s.set("timeout", 6000)
        z3result = s.check(z3.Not(Testing.asZ3(first_translated,enum) == Testing.asZ3(second_translated,enum)))
        if z3result == z3.unsat:
            print(q+'\nGoing into slow mode...')
            s = z3.Solver()
            s.set("timeout", 60000)
            z3result = s.check(z3.Not(Testing.asZ3(first_translated) == Testing.asZ3(second_translated)))
            if z3result == z3.unsat:
                print('successful rule found by using more time!')
                return [(first, second)]
            elif z3result == z3.sat:
                print('successful refutation found by using more time!')
                return []
            else:
                raise Exception("Z3 does not know the answer!\n"+q)
        elif z3result == z3.sat:
            return [] # counter example found for a small universe, this happens quite a lot
        else:
            q=('Stuck at: ' + str(first) + ' -> ' + str(second))
            raise Exception("Z3 times out even in the finite case!\n"+q)

# Processes one chunk of a list of formulas and returns a set of the COR simplification rules found
def compute_chunk(formulas, size, cpu_cores, timeout=3600):
    """ This is simply a helper function for enabling multiprocessing. """
    
    pairs = ((first,second)
              for first in formulas
              for vars_used in [set(char for char in str(first) if ord(char) in [ord('A'), ord('B'), ord('C')])]
              for second_size in range(size)
              for second in Testing.generate_all_COR_formulas(second_size)
              if not is_already_simplifiable(second)
                 and set(char for char in str(second) if ord(char) in [ord('A'), ord('B'), ord('C')]).issubset(vars_used)
            )
    return set(result for pair in pairs for result in compute_single(pair))



def print_rule_dictionary(cor_dict, write_to_txt_file=False, filename=""):
    """ This will print out the dictionary of stored rules. Set the parameter to True for printing to a .txt or False for printing to the terminal. """
        
    if not write_to_txt_file:
        for key in cor_dict:
            print(str(key) + " -> " + str(cor_dict[key]))
    else:
        cor_rules = open(filename, "w+", encoding="utf_8")
        for key in cor_dict:
            cor_rules.write(str(key) + " -> " + str(cor_dict[key]) + "\n")
            
            
def add_tabs_to_string(string, tab_level):
    """ This is a helper function for adding a newline and the specified number of tabs to a string. """
    return ("\n" + ("\t" * tab_level) + string)
           
def recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, typed, arg2=[]):
            if len(arg2) == 0:
                if not typed:
                    return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level+1)
                else:
                    return accumulator + add_tabs_to_string("return " + second.object_representation("expression.type()[0]", "expression.type()[1]"), tab_level+1)
            else:
                (arg2Name,arg) = arg2.pop()
                if not typed:
                    return accumulator + generate_helper(arg, second, arg2Name, boundVars, "", tab_level+1, arg2)
                else:
                    return accumulator + generate_helper_typed(arg, second, arg2Name, boundVars, "", tab_level+1, arg2)

            
def generate_helper_typed(first, second, me, boundVars, accumulator, tab_level, arg2=[]) -> str:
    """ Generates Python code for a typed simplification rule and returns it as a string """
    match first:
        case Typed_COR_Expressions.Typed_Relation(letter=l, set1=s1, set2=s2):
            if l in boundVars:
                accumulator += add_tabs_to_string(f"if str({l})==str({me}):", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return " + second.object_representation("expression.type()[0]", "expression.type()[1]"), tab_level+1)
                else:
                    (arg2Name,arg) = arg2.pop()
                    return accumulator +  generate_helper_typed(arg, second, arg2Name, boundVars + [l], "", tab_level+1, arg2)
            else:
                accumulator += add_tabs_to_string(f"{l} = {me}", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return " + second.object_representation("expression.type()[0]", "expression.type()[1]"), tab_level)
                else:
                    (arg2Name,arg) = arg2.pop()
                    return accumulator +  generate_helper_typed(arg, second, arg2Name, boundVars + [l], "", tab_level, arg2)
        case Typed_COR_Expressions.Typed_UniversalRelation(set1=s1, set2=s2):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_UniversalRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, True, arg2)
        case Typed_COR_Expressions.Typed_EmptyRelation(set1=s1, set2=s2):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_EmptyRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, True, arg2)
        case Typed_COR_Expressions.Typed_IdentityRelation(set1=s1, set2=s2):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_IdentityRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, True, arg2)
        case Typed_COR_Expressions.Typed_Complement(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Complement):", tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper_typed(arg,second,'arg', boundVars, accumulator, tab_level+1, arg2)
        case Typed_COR_Expressions.Typed_Converse(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Converse):", tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper_typed(arg,second,'arg', boundVars, accumulator, tab_level+1, arg2)
        case Typed_COR_Expressions.Typed_Union(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Union):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1,second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
        case Typed_COR_Expressions.Typed_Intersection(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Intersection):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
        case Typed_COR_Expressions.Typed_Dagger(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Dagger):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
        case Typed_COR_Expressions.Typed_Composition(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, Typed_COR_Expressions.Typed_Composition):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper_typed(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
            
            
def generate_helper(first, second, me, boundVars, accumulator, tab_level, arg2=[]) -> str:
    """ Generates Python code for a simplification rule and returns it as a string """
    match first:
        case COR_Expressions.Relation(letter=l):
            if l in boundVars:
                accumulator += add_tabs_to_string(f"if str({l})==str({me}):", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level+1)
                else:
                    (arg2Name,arg) = arg2.pop()
                    return accumulator +  generate_helper(arg, second, arg2Name, boundVars + [l], "", tab_level+1, arg2)
            else:
                accumulator += add_tabs_to_string(f"{l} = {me}", tab_level)
                if len(arg2) == 0:
                    return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level)
                else:
                    (arg2Name,arg) = arg2.pop()
                    return accumulator +  generate_helper(arg, second, arg2Name, boundVars + [l], "", tab_level, arg2)
        case COR_Expressions.UniversalRelation():
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.UniversalRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, False, arg2)
        case COR_Expressions.EmptyRelation():
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.EmptyRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, False, arg2)
        case COR_Expressions.IdentityRelation():
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.IdentityRelation):", tab_level)
            return recurse_generate_helper_Symbol(first, second, me, boundVars, accumulator, tab_level, False, arg2)
        case COR_Expressions.Complement(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Complement):", tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper(arg,second,'arg', boundVars, accumulator, tab_level+1, arg2)
        case COR_Expressions.Converse(argument=arg):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Converse):", tab_level) + add_tabs_to_string(f"arg = {me}.argument", tab_level+1)
            return generate_helper(arg,second,'arg', boundVars, accumulator, tab_level+1, arg2)
        case COR_Expressions.Union(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Union):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1,second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
        case COR_Expressions.Intersection(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Intersection):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
        case COR_Expressions.Dagger(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Dagger):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
        case COR_Expressions.Composition(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"if isinstance({me}, COR_Expressions.Composition):", tab_level) + add_tabs_to_string(f'lhs{tab_level}, rhs{tab_level} = {me}.argument1, {me}.argument2', tab_level+1)
            return generate_helper(arg1, second, f'lhs{tab_level}', boundVars, accumulator, tab_level+1, arg2+[(f'rhs{tab_level}',argLater)])
    
    
def group_by_prefix(lst):
    """ This method helps us generate prettier code by grouping rules with similar prefixes. """
    groups = {}
    for item in lst:
        try:
            prefix, remainder = (item[0],item[1:])
        except:
            continue
        if prefix in groups:
            groups[prefix].append(remainder)
        else:
            groups[prefix]=[remainder]
    for group in groups:
        if len(groups[group])>1: groups[group]=group_by_prefix(groups[group])
        else: groups[group] = groups[group][0]
    return groups


def write_grouped_code(python_code, groups):
    """ This method helps us generate prettier code by grouping rules with similar prefixes. """
    return_level = 999 # Arbitrarily Large Number
    for group in groups:
        tab_level = len(group.split('\t'))
        if tab_level < return_level:
            return_level = 999 # Arbitrarily Large Number
            python_code.write(group+'\n')
        if isinstance(groups[group], dict):
            write_grouped_code(python_code, groups[group])
        else:
            for line in groups[group]:
                tab_level = len(line.split('\t'))
                if tab_level < return_level:
                    return_level = 999 # Arbitrarily Large Number
                    python_code.write(line+'\n')
                    if "return" in line:
                        return_level = len(line.split('\t'))
                
                
def generate_code_from_cor_rules(cor_dict, filename, typed):
    """ Generates Python code in the file Simplify.py from a dictionary of simplification rules """
    # Create a new .py file to write to
    python_code = open(filename, "w+", encoding="utf_8")
    code = []
    for first in cor_dict:
        vars_first = multiset.Multiset(char for char in str(first) if ord(char) in [ord('A'), ord('B'), ord('C')])
        second = cor_dict[first]
        vars_second = multiset.Multiset(char for char in str(second) if ord(char) in [ord('A'), ord('B'), ord('C')])
        if vars_second.issubset(vars_first):
            code.append(generate_helper_typed(first, second, "expression", [], "", 1).split('\n')
                        if typed
                         else generate_helper(first, second, "expression", [], "", 1).split('\n')
            )
    code = group_by_prefix(code)
    if not typed:
        python_code.write("import COR_Expressions" + "\n")
    else:
        python_code.write("import Typed_COR_Expressions" + "\n")
    python_code.write("\ndef simplify(expression):")
    write_grouped_code(python_code, code)
    python_code.write("\n\treturn expression # The given expression was unable to be simplified")
    # Close the file when done
    python_code.close()
    

# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__": 
    try:
        with open('cor_dict.pickle', 'rb') as file:
            cor_dict = pickle.load(file)
    except FileNotFoundError:
        cor_dict = {}
        print("No cor_dict.pickle file found. Using an empty dictionary (and probably creating one later)...")
    
    #look_for_simplification_rules(0, 6)
    #look_for_simplification_rules(1, 6)
    #look_for_simplification_rules(2, 6)
    #look_for_simplification_rules(3, 6)
    
    print_rule_dictionary(cor_dict, True, "COR_Rules.txt")
    generate_code_from_cor_rules(cor_dict, "Simplify.py", False)
