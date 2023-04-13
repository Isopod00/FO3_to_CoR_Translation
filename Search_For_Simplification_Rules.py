# Author: Anthony Brogni
# Last Changed: March 2023

import multiprocessing
from timeit import default_timer

import numpy  # pip install numpy
import z3  # pip install z3-solver
import pickle # save/load python objects from a file

import Testing
from FO3_Expressions import *
import COR_Expressions

import Simplify

# Searches for simplification rules for a given size by utilizing the specified number of cpu cores
def look_for_simplification_rules(size, cpu_cores, timeout=3600):
    print(f"A search for simplification rules of size {size} has started (using {cpu_cores} logical processors)")
    start = default_timer()  # Time how long this takes

    # Load the rule dictionary from file
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
        
    known_cor_rules = set(str(formula) for formula in cor_dict)

    # Generate ALL formulas of the specified size and split this list into equally-sized chunks
    formulas = [formula for formula in list(Testing.generate_all_COR_formulas(size)) if not is_already_simplifiable(formula, known_cor_rules)]
    print(f"Searching {len(formulas)} formulas of this size.")
    equal_chunks = numpy.array_split(numpy.array(formulas), cpu_cores)  # equal_chunks will be a list of numpy arrays

    # Create our pool of tasks
    with multiprocessing.Pool(cpu_cores) as pool:
        results = []
        for array in equal_chunks:
            results.append(pool.apply_async(compute_chunk, args=(list(array), size, timeout)))  # convert the numpy arrays to lists
        pool.close()
        pool.join()

    # Construct the sets which will contain the final answers
    final_cor_result = set()
    for result in results:
        final_cor_result = final_cor_result.union(result.get())

    # Add the final answers to the rule dictionary
    for rule in final_cor_result:
        if str(rule[0]) not in known_cor_rules:
            cor_dict[rule[0]] = rule[1]
        
    # Save the rule dictionary to file
    with open('cor_dict.pickle', 'wb') as file:
        pickle.dump(cor_dict, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"The search for simplification rules of size {size} finished in {default_timer() - start} seconds!")


def is_already_simplifiable(expression, known_rules):
    match expression:
        case COR_Expressions.Relation(letter=l):
            return False
        case COR_Expressions.UniversalRelation():
            return False
        case COR_Expressions.EmptyRelation():
            return False
        case COR_Expressions.IdentityRelation():
            return False
        case COR_Expressions.Complement(argument=arg):
            return str(expression) in known_rules or is_already_simplifiable(arg, known_rules)
        case COR_Expressions.Converse(argument=arg):
            return str(expression) in known_rules or is_already_simplifiable(arg, known_rules)
        case COR_Expressions.Union(argument1=arg1, argument2=arg2):
            return str(expression) in known_rules or is_already_simplifiable(arg1, known_rules) or is_already_simplifiable(arg2, known_rules)
        case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
            return str(expression) in known_rules or is_already_simplifiable(arg1, known_rules) or is_already_simplifiable(arg2, known_rules)
        case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
            return str(expression) in known_rules or is_already_simplifiable(arg1, known_rules) or is_already_simplifiable(arg2, known_rules)
        case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
            return str(expression) in known_rules or is_already_simplifiable(arg1, known_rules) or is_already_simplifiable(arg2, known_rules)
        
        
def simplify(expression):
    match expression:
        case COR_Expressions.Relation(letter=l):
            return expression
        case COR_Expressions.UniversalRelation():
            return expression
        case COR_Expressions.EmptyRelation():
            return expression
        case COR_Expressions.IdentityRelation():
            return expression
        case COR_Expressions.Complement(argument=arg):
            return Simplify.simplify(COR_Expressions.Complement(Simplify.simplify(arg)))
        case COR_Expressions.Converse(argument=arg):
            return Simplify.simplify(COR_Expressions.Converse(Simplify.simplify(arg)))
        case COR_Expressions.Union(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Union(simplify(arg1), simplify(arg2)))
        case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Intersection(simplify(arg1), simplify(arg2)))
        case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Dagger(simplify(arg1), simplify(arg2)))
        case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
            return Simplify.simplify(COR_Expressions.Composition(simplify(arg1), simplify(arg2)))
        


# Processes one chunk of a list of formulas and returns a set of the COR simplification rules found
def compute_chunk(formulas, size, timeout=3600):
    cor_result = set()
    
    start = default_timer()
    
    # Load the rule dictionary from file
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
    known_cor_rules = set(str(formula) for formula in cor_dict)

    for first in formulas:
        for second_size in range(1, size):
            for second in [formula for formula in Testing.generate_all_COR_formulas(second_size) if not is_already_simplifiable(formula, known_cor_rules)]:
                
                # Return what we've found if we've been searching for longer than the timeout
                if default_timer() - start >= timeout:
                    return cor_result

                first_translated = first.translate('x', 'y')
                second_translated = second.translate('x', 'y')

                s = z3.Solver()
                s.add(z3.Not(Testing.asZ3(first_translated) == Testing.asZ3(second_translated)))
                s.set("timeout", 500)
                z3result = s.check()
                if z3result == z3.unsat:
                    cor_result.add((first, second))

    return cor_result


def print_rule_dictionary(write_to_txt_file=False):
    # Load the rule dictionary from file
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
        
    if not write_to_txt_file:
        print("COR Rules: ")
        for key in cor_dict:
            print(str(key) + " -> " + str(cor_dict[key]))
    else:
        cor_rules = open("COR_Rules.txt", "w+", encoding="utf_8")
        for key in cor_dict:
            cor_rules.write(str(key) + " -> " + str(cor_dict[key]) + "\n")
            
            
def add_tabs_to_string(string, tab_level):
    return ("\n" + ("\t" * tab_level) + string)
            
            
def generate_helper(first, second, me, boundVars, accumulator, tab_level, arg2=[]) -> str:
    """ Creates Python code for a single cor rule and returns it as a string """
    match first:
        case COR_Expressions.Relation(letter=l):
            if l in boundVars:
                accumulator += add_tabs_to_string(f"case _ if str({l})==str({me}):", tab_level)
            else:
                accumulator += add_tabs_to_string(f"case _:", tab_level)
                accumulator += add_tabs_to_string(f"{l} = {me}", tab_level+1)
            if len(arg2) == 0:
                return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level+1) 
            else:
                arg = arg2.pop()
                return accumulator + add_tabs_to_string(f"match arg{len(arg2)+2}:", tab_level+1) + generate_helper(arg, second, f'arg{len(arg2)+2}', boundVars + [l], "", tab_level+2,arg2)
        case COR_Expressions.UniversalRelation():
            accumulator += add_tabs_to_string("case COR_Expressions.UniversalRelation():", tab_level)
            if len(arg2) == 0:
                return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level+1) 
            else:
                arg = arg2.pop()
                return accumulator + add_tabs_to_string(f"match arg{len(arg2)+2}:", tab_level+1) + generate_helper(arg, second, f'arg{len(arg2)+2}', boundVars, "", tab_level+2,arg2)
        case COR_Expressions.EmptyRelation():
            accumulator += add_tabs_to_string("case COR_Expressions.EmptyRelation():", tab_level)
            if len(arg2) == 0:
                return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level+1) 
            else:
                arg = arg2.pop()
                return accumulator + add_tabs_to_string(f"match arg{len(arg2)+2}:", tab_level+1) + generate_helper(arg, second, f'arg{len(arg2)+2}', boundVars, "", tab_level+2,arg2)
        case COR_Expressions.IdentityRelation():
            accumulator += add_tabs_to_string("case COR_Expressions.IdentityRelation:", tab_level)
            if len(arg2) == 0:
                return accumulator + add_tabs_to_string("return " + second.object_representation(), tab_level+1) 
            else:
                arg = arg2.pop()
                return accumulator + add_tabs_to_string(f"match arg{len(arg2)+2}:", tab_level+1) + generate_helper(arg, second, f'arg{len(arg2)+2}', boundVars, "", tab_level+2,arg2)
        case COR_Expressions.Complement(argument=arg):
            accumulator += add_tabs_to_string("case COR_Expressions.Complement(argument=arg):", tab_level)
            accumulator += add_tabs_to_string("match arg:", tab_level+1)
            return generate_helper(arg,second,'arg', boundVars, accumulator, tab_level+2, arg2)
        case COR_Expressions.Converse(argument=arg):
            accumulator += add_tabs_to_string("case COR_Expressions.Converse(argument=arg):", tab_level)
            accumulator += add_tabs_to_string("match arg:", tab_level+1)
            return generate_helper(arg,second,'arg', boundVars, accumulator, tab_level+2, arg2)
        case COR_Expressions.Union(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"case COR_Expressions.Union(argument1=arg1, argument2=arg{len(arg2)+2}):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            return generate_helper(arg1,second, 'arg1', boundVars, accumulator, tab_level+2, arg2+[argLater])
        case COR_Expressions.Intersection(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"case COR_Expressions.Intersection(argument1=arg1, argument2=arg{len(arg2)+2}):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            return generate_helper(arg1, second, 'arg1', boundVars, accumulator, tab_level+2, arg2+[argLater])
        case COR_Expressions.Dagger(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"case COR_Expressions.Dagger(argument1=arg1, argument2=arg{len(arg2)+2}):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            return generate_helper(arg1, second, 'arg1', boundVars, accumulator, tab_level+2, arg2+[argLater])
        case COR_Expressions.Composition(argument1=arg1, argument2=argLater):
            accumulator += add_tabs_to_string(f"case COR_Expressions.Composition(argument1=arg1, argument2=arg{len(arg2)+2}):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            return generate_helper(arg1, second, 'arg1', boundVars, accumulator, tab_level+2, arg2+[argLater])
    
def group_by_prefix(lst):
    groups = {}
    for item in lst:
        prefix, remainder = (item[0],item[1:])
        if prefix in groups:
            groups[prefix].append(remainder)
        else:
            groups[prefix]=[remainder]
    for group in groups:
        if len(groups[group])>1: groups[group]=group_by_prefix(groups[group])
        else: groups[group] = groups[group][0]
    return groups
def write_grouped_code(python_code, groups):
    for group in groups:
        if group[-2:] == '_:': continue
        python_code.write(group+'\n')
        if isinstance(groups[group], dict):
            write_grouped_code(python_code, groups[group])
        else:
            for line in groups[group]:
                python_code.write(line+'\n')
    for group in groups:
        if group[-2:] != '_:': continue
        python_code.write(group+'\n')
        if isinstance(groups[group], dict):
            write_grouped_code(python_code, groups[group])
        else:
            for line in groups[group]:
                python_code.write(line+'\n')
def generate_code_from_cor_rules(cor_dict):
    """ Generates Python code from a dictionary of cor rules """
    # Create a new .py file to write to
    python_code = open("Simplify.py", "w+", encoding="utf_8")
    code = []
    for first in cor_dict:
        second = cor_dict[first]
        code.append(generate_helper(first, second, "expression", [], "\n\tmatch expression:", 2).split('\n'))
    code = group_by_prefix(code)
    python_code.write("import COR_Expressions" + "\n")
    python_code.write("\ndef simplify(expression):")
    write_grouped_code(python_code, code)
    # python_code.write(f'\n\t# {first} = {second}')
    python_code.write("\n\treturn None # The given expression was unable to be simplified")
    # Close the file when done
    python_code.close()
    

# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    # look_for_simplification_rules(2, 6)
    # look_for_simplification_rules(3, 6)
    # look_for_simplification_rules(4, 6)
    
    print_rule_dictionary(True)
    
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
    generate_code_from_cor_rules(cor_dict)
