# Author: Anthony Brogni
# Last Changed: March 2023

import multiprocessing
from timeit import default_timer

import numpy  # pip install numpy
import z3  # pip install z3-solver
import pickle # save/load python objects from a file

import FO3_Translation_Methods
import Testing
from FO3_Expressions import *


# Searches for simplification rules for a given size by utilizing the specified number of cpu cores
def look_for_simplification_rules(size, cpu_cores, cor=True):
    print(f"A search for simplification rules of size {size} has started (using {cpu_cores} logical processors)")
    start = default_timer()  # Time how long this takes

    # Load the rule dictionaries from files
    with open('fo3_dict.pickle', 'rb') as file:
        fo3_dict = pickle.load(file)
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
        
    known_fo3_rules = set(str(formula) for formula in fo3_dict)
    known_cor_rules = set(str(formula) for formula in cor_dict)

    # Generate ALL formulas of the specified size and split this list into equally-sized chunks
    if cor:
        formulas = [formula for formula in list(Testing.generate_all_COR_formulas(size)) if str(formula) not in known_cor_rules]
    else:
        formulas = [formula for formula in list(Testing.generate_all_FO3_formulas_filtered(size)) if str(formula) not in known_fo3_rules]
    print(f"Searching {len(formulas)} formulas of this size.")
    equal_chunks = numpy.array_split(numpy.array(formulas), cpu_cores)  # equal_chunks will be a list of numpy arrays

    # Create our pool of tasks
    with multiprocessing.Pool(cpu_cores) as pool:
        results = []
        for array in equal_chunks:
            if cor:
                results.append(pool.apply_async(compute_chunk_cor, args=(list(array), size)))  # convert the numpy arrays to lists
            else:
                results.append(pool.apply_async(compute_chunk, args=(list(array), size)))  # convert the numpy arrays to lists
        pool.close()
        pool.join()

    # Construct the sets which will contain the final answers
    final_fo3_result = set()
    final_cor_result = set()
    for result in results:
        final_fo3_result = final_fo3_result.union(result.get()[0])  # First part of the tuple is the FO3 results
        final_cor_result = final_cor_result.union(result.get()[1])  # Second part of the tuple is the COR results

    # Add the final answers to the rule dictionaries
    for rule in final_fo3_result:
        if str(rule[0]) not in known_fo3_rules:
            fo3_dict[rule[0]] = rule[1]
    for rule in final_cor_result:
        if str(rule[0]) not in known_cor_rules:
            cor_dict[rule[0]] = rule[1]
        
    # Save the rule dictionaries to files
    with open('fo3_dict.pickle', 'wb') as file:
        pickle.dump(fo3_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
    with open('cor_dict.pickle', 'wb') as file:
        pickle.dump(cor_dict, file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"The search for simplification rules of size {size} finished in {default_timer() - start} seconds!")


# Processes one chunk of a list of FO3 formulas and returns two sets: the FO3 simplification rules found and the COR simplification rules found
def compute_chunk(formulas, size):
    fo3_result = set()
    cor_result = set()
    
    # Load the rule dictionary from file
    with open('fo3_dict.pickle', 'rb') as file:
        fo3_dict = pickle.load(file)
    known_fo3_rules = set(str(formula) for formula in fo3_dict)

    for first in formulas:
        for second_size in range(1, size):
            for second in [formula for formula in Testing.generate_all_FO3_formulas_filtered(second_size) if str(formula) not in known_fo3_rules]:

                s = z3.Solver()
                s.add(z3.Not(Testing.asZ3(first) == Testing.asZ3(second)))
                s.set("timeout", 500)
                z3result = s.check()
                if z3result == z3.unsat:
                    fo3_result.add((first, second))

                    cor_first = FO3_Translation_Methods.final_translation(first, 'x', 'y')
                    cor_second = FO3_Translation_Methods.final_translation(second, 'x', 'y')
                    first_string = str(cor_first)
                    second_string = str(cor_second)
                    if "None" not in first_string and "None" not in second_string and first_string != second_string:
                        cor_result.add((cor_first, cor_second))

    return fo3_result, cor_result


# Processes one chunk of a list of COR formulas and returns two sets: the FO3 simplification rules found and the COR simplification rules found
def compute_chunk_cor(formulas, size):
    fo3_result = set()
    cor_result = set()
    
    # Load the rule dictionary from file
    with open('fo3_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
    known_cor_rules = set(str(formula) for formula in cor_dict)

    for first in formulas:
        for second_size in range(1, size):
            for second in [formula for formula in Testing.generate_all_COR_formulas(second_size) if str(formula) not in known_cor_rules]:

                first_translated = first.translate('x', 'y')
                second_translated = second.translate('x', 'y')

                s = z3.Solver()
                s.add(z3.Not(Testing.asZ3(first_translated) == Testing.asZ3(second_translated)))
                s.set("timeout", 500)
                z3result = s.check()
                if z3result == z3.unsat:
                    cor_result.add((first, second))
                    if str(first_translated) != str(second_translated):
                        fo3_result.add((first_translated, second_translated))
                    

    return fo3_result, cor_result


def print_rule_dictionaries(write_to_txt_file=False):
    # Load the rule dictionaries from files
    with open('fo3_dict.pickle', 'rb') as file:
        fo3_dict = pickle.load(file)
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
        
    if not write_to_txt_file:
        print("COR Rules: ")
        for key in cor_dict:
            print(str(key) + " -> " + str(cor_dict[key]))
        print("\nFO3 Rules: ")
        for key in fo3_dict:
            print(str(key) + " -> " + str(fo3_dict[key]))
    else:
        cor_rules = open("COR_Rules.txt", "w+", encoding="utf_8")
        for key in cor_dict:
            cor_rules.write(str(key) + " -> " + str(cor_dict[key]) + "\n")
        fo3_rules = open("FO3_Rules.txt", "w+", encoding="utf_8")
        for key in fo3_dict:
            fo3_rules.write(str(key) + " -> " + str(fo3_dict[key]) + "\n")

# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    look_for_simplification_rules(2, 6)
    look_for_simplification_rules(3, 6)
    look_for_simplification_rules(4, 6)
    print_rule_dictionaries(True)
