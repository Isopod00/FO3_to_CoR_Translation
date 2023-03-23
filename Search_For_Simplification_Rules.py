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


# Searches for simplification rules for a given size by utilizing the specified number of cpu cores
def look_for_simplification_rules(size, cpu_cores, timeout=3600):
    print(f"A search for simplification rules of size {size} has started (using {cpu_cores} logical processors)")
    start = default_timer()  # Time how long this takes

    # Load the rule dictionary from file
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
        
    known_cor_rules = set(str(formula) for formula in cor_dict)

    # Generate ALL formulas of the specified size and split this list into equally-sized chunks
    formulas = [formula for formula in list(Testing.generate_all_COR_formulas(size)) if str(formula) not in known_cor_rules]
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

    # Add the final answers to the rule dictionaries
    for rule in final_cor_result:
        if str(rule[0]) not in known_cor_rules:
            cor_dict[rule[0]] = rule[1]
        
    # Save the rule dictionaries to files
    with open('cor_dict.pickle', 'wb') as file:
        pickle.dump(cor_dict, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"The search for simplification rules of size {size} finished in {default_timer() - start} seconds!")


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
            for second in [formula for formula in Testing.generate_all_COR_formulas(second_size) if str(formula) not in known_cor_rules]:
                
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


def print_rule_dictionaries(write_to_txt_file=False):
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
            
            
def generate_helper(first, me, accumulator, returnval, tab_level) -> str:
    """ Creates Python code for a single cor rule and returns it as a string """
    match first:
        case COR_Expressions.Relation(letter=l):
            accumulator += add_tabs_to_string(f"case _:", tab_level)
            accumulator += add_tabs_to_string(f"{l} = {me}", tab_level+1)
            return accumulator + add_tabs_to_string(returnval, tab_level+1)
        case COR_Expressions.UniversalRelation():
            accumulator += add_tabs_to_string("case COR_Expressions.UniversalRelation():", tab_level)
            return accumulator + add_tabs_to_string(returnval, tab_level+1)
        case COR_Expressions.EmptyRelation():
            accumulator += add_tabs_to_string("case COR_Expressions.EmptyRelation():", tab_level)
            return accumulator + add_tabs_to_string(returnval, tab_level+1)
        case COR_Expressions.IdentityRelation():
            accumulator += add_tabs_to_string("case COR_Expressions.IdentityRelation:", tab_level)
            return accumulator + add_tabs_to_string(returnval, tab_level+1)
        case COR_Expressions.Complement(argument=arg):
            accumulator += add_tabs_to_string("case COR_Expressions.Complement(argument=arg):", tab_level)
            accumulator += add_tabs_to_string("match arg:", tab_level+1)
            return generate_helper(arg,'arg', accumulator, returnval, tab_level+2)
        case COR_Expressions.Converse(argument=arg):
            accumulator += add_tabs_to_string("case COR_Expressions.Converse(argument=arg):", tab_level)
            accumulator += add_tabs_to_string("match arg:", tab_level+1)
            return generate_helper(arg,'arg', accumulator, returnval, tab_level+2)
        case COR_Expressions.Union(argument1=arg1, argument2=arg2):
            accumulator += add_tabs_to_string("case COR_Expressions.Union(argument1=arg1, argument2=arg2):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            returnval = generate_helper(arg2,'arg2','match arg2:',returnval,tab_level+4)
            return generate_helper(arg1,'arg1', accumulator, returnval, tab_level+2)
        case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):
            accumulator += add_tabs_to_string("case COR_Expressions.Intersection(argument1=arg1, argument2=arg2):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            returnval = generate_helper(arg2,'arg2','match arg2:',returnval,tab_level+4)
            return generate_helper(arg1,'arg1', accumulator, returnval, tab_level+2)
        case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):
            accumulator += add_tabs_to_string("case COR_Expressions.Dagger(argument1=arg1, argument2=arg2):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            returnval = generate_helper(arg2,'arg2','match arg2:',returnval,tab_level+4)
            return generate_helper(arg1,'arg1', accumulator, returnval, tab_level+2)
        case COR_Expressions.Composition(argument1=arg1, argument2=arg2):
            accumulator += add_tabs_to_string("case COR_Expressions.Composition(argument1=arg1, argument2=arg2):", tab_level)
            accumulator += add_tabs_to_string("match arg1:", tab_level+1)
            returnval = generate_helper(arg2,'arg2','match arg2:',returnval,tab_level+4)
            return generate_helper(arg1,'arg1', accumulator, returnval, tab_level+2)
    
            
def generate_code_from_cor_rules():
    """ Generates Python code from a dictionary of cor rules """
    # Load the COR Rules dictionary
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
    # Create a new .py file to write to
    python_code = open("Simplify.py", "w+", encoding="utf_8")
    python_code.write("import COR_Expressions" + "\n")
    python_code.write("def simplify(expression):" + "\n\t")
    python_code.write("match expression:")
    for first in cor_dict:
        second = cor_dict[first]
        python_code.write(f'\n\t\t# {first} = {second}')
        python_code.write(generate_helper(first, "expression", "", "return " + second.object_representation(), 2))
    python_code.write("\n\t\tcase _:\n\t\t\treturn expression") # Case for if the expression cannot be simplified
    # Close the file when done
    python_code.close()
    

# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    look_for_simplification_rules(2, 6)
    look_for_simplification_rules(3, 6)
    #look_for_simplification_rules(4, 6, timeout=10)
    print_rule_dictionaries(True)
    generate_code_from_cor_rules()

