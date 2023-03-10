# Author: Anthony Brogni
# Last Changed: March 2023

import multiprocessing
from timeit import default_timer
import z3  # pip install z3-solver
import numpy  # pip install numpy

import Testing
from FO3_Expressions import *
import FO3_Translation_Methods

# Searches for simplification rules for a given size by utilizing the specified number of cpu cores
def look_for_simplification_rules(size, cpu_cores):
    print(f"A search for simplification rules of size {size} has started (using {cpu_cores} logical processors)")
    start = default_timer()
        
    fo3_results = open("FO3_Rules.txt", "r+", encoding="utf8")
    cor_results = open("COR_Rules.txt", "r+", encoding="utf8")
    fo3_rules_found_so_far = set(fo3_results.readlines())
    cor_rules_found_so_far = set(cor_results.readlines())
    
    formulas = list(Testing.generate_all_FO3_formulas(size))
    equal_chunks = numpy.array_split(numpy.array(formulas), cpu_cores)  # equal_chunks will be a list of numpy arrays

    with multiprocessing.Pool(cpu_cores) as pool:
        results = []
        for array in equal_chunks:
            results.append(pool.apply_async(compute_chunk, args=(list(array), size)))  # convert the numpy arrays to lists
        pool.close()
        pool.join()

    final_fo3_result = set()
    final_cor_result = set()
    for result in results:
        final_fo3_result = final_fo3_result.union(result.get()[0])
        final_cor_result = final_cor_result.union(result.get()[1])
    final_fo3_result = final_fo3_result.difference(fo3_rules_found_so_far)
    final_cor_result = final_cor_result.difference(cor_rules_found_so_far)
    for string in final_fo3_result:
        fo3_results.write(string)  
    for string in final_cor_result:
        cor_results.write(string)
       
    fo3_results.close()
    cor_results.close()
    print(f"The search for simplification rules of size {size} finished in {default_timer() - start} seconds!")

# Processes one chunk of a list of FO3 formulas and returns two sets: the FO3 simplification rules found and the COR simplification rules found
def compute_chunk(formulas, size):
    fo3_result = set()
    cor_result = set()
    
    for first in formulas:
        for second_size in range(1, size):
            for second in Testing.generate_all_FO3_formulas(second_size):
                if isinstance(second, Equals) and second.argument1 == second.argument2:
                    second = tt()  # x=x is always True

                rule = str(first) + " == " + str(second) + "\n"
                s = z3.Solver()
                s.add(z3.Not(Testing.asZ3(first) == Testing.asZ3(second)))
                s.set("timeout", 500)
                z3result = s.check()
                if z3result == z3.unsat:
                    fo3_result.add(rule)
                    
                    cor_first = str(FO3_Translation_Methods.final_translation(first, 'x', 'y'))
                    cor_second = str(FO3_Translation_Methods.final_translation(second, 'x', 'y'))
                    if cor_first != cor_second:
                        cor_rule = cor_first + " == " + cor_second + "\n"
                        if "None" not in cor_rule:
                            cor_result.add(cor_rule)
            
    return fo3_result, cor_result
        
# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    look_for_simplification_rules(2, 6)
    