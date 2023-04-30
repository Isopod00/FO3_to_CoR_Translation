# Author: Anthony Brogni
# Last Changed: May 2023
""" This file is for creating typed simplification rules from the untyped rules we have found with Search_For_Simplification_Rules.py. """

import pickle
import z3  # pip install z3-solver

import Typed_Testing
import Search_For_Simplification_Rules
from COR_Expressions import *
from Typed_COR_Expressions import *

# Takes an untyped COR expression and applies all valid types to it
def make_homogeneous_formula_typed(formula):
    match formula:
        case UniversalRelation():
            for set1 in ['P', 'Q', 'R', 'S']:
                for set2 in ['P', 'Q', 'R', 'S']:
                    yield Typed_UniversalRelation(set1, set2)
        case EmptyRelation():
            for set1 in ['P', 'Q', 'R', 'S']:
                for set2 in ['P', 'Q', 'R', 'S']:
                    yield Typed_EmptyRelation(set1, set2)
        case IdentityRelation():
            for set1 in ['P', 'Q', 'R', 'S']:
                for set2 in ['P', 'Q', 'R', 'S']:
                    yield Typed_IdentityRelation(set1, set2)
        case Relation(letter=l):
            for set1 in ['P', 'Q', 'R', 'S']:
                for set2 in ['P', 'Q', 'R', 'S']:
                    yield Typed_Relation(l, set1, set2)
        case Complement(argument=arg):
            for subformula in make_homogeneous_formula_typed(arg):
                yield Typed_Complement(subformula)
        case Converse(argument=arg):
            for subformula in make_homogeneous_formula_typed(arg):
                yield Typed_Converse(subformula)
        case Union(argument1=arg1, argument2=arg2):
            for subformula1 in make_homogeneous_formula_typed(arg1):
                for subformula2 in make_homogeneous_formula_typed(arg2):
                    try:
                        yield Typed_Union(subformula1, subformula2)
                    except:
                        pass
        case Intersection(argument1=arg1, argument2=arg2):
            for subformula1 in make_homogeneous_formula_typed(arg1):
                for subformula2 in make_homogeneous_formula_typed(arg2):
                    try:
                        yield Typed_Intersection(subformula1, subformula2)
                    except:
                        pass
        case Dagger(argument1=arg1, argument2=arg2):
            for subformula1 in make_homogeneous_formula_typed(arg1):
                for subformula2 in make_homogeneous_formula_typed(arg2):
                    try:
                        yield Typed_Dagger(subformula1, subformula2)
                    except:
                        pass
        case Composition(argument1=arg1, argument2=arg2):
            for subformula1 in make_homogeneous_formula_typed(arg1):
                for subformula2 in make_homogeneous_formula_typed(arg2):
                    try:
                        yield Typed_Composition(subformula1, subformula2)
                    except:
                        pass
 
 
# Takes an untyped COR expression and applies the specified type to it (type is an ordered pair)
def give_type(formula, type):
    set1 = type[0]
    set2 = type[1]
    match formula:
        case UniversalRelation():
            yield Typed_UniversalRelation(set1, set2)
        case EmptyRelation():
            yield Typed_EmptyRelation(set1, set2)
        case IdentityRelation():
            yield Typed_IdentityRelation(set1, set2)
        case Relation(letter=l):
            yield Typed_Relation(l, set1, set2)
        case Complement(argument=arg):
            for subformula in give_type(arg, type):
                yield Typed_Complement(subformula)
        case Converse(argument=arg):
            for subformula in give_type(arg, type):
                yield Typed_Converse(subformula)
        case Union(argument1=arg1, argument2=arg2):
            for subformula1 in give_type(arg1, type):
                for subformula2 in give_type(arg2, type):
                    yield Typed_Union(subformula1, subformula2)
        case Intersection(argument1=arg1, argument2=arg2):
            for subformula1 in give_type(arg1, type):
                for subformula2 in give_type(arg2, type):
                    yield Typed_Intersection(subformula1, subformula2)
        case Dagger(argument1=arg1, argument2=arg2):
            for set in ['P', 'Q', 'R', 'S']:
                for subformula1 in give_type(arg1, (set1, set)):
                    for subformula2 in give_type(arg2, (set, set2)):
                        yield Typed_Dagger(subformula1, subformula2)
        case Composition(argument1=arg1, argument2=arg2):
            for set in ['P', 'Q', 'R', 'S']:
                for subformula1 in give_type(arg1, (set1, set)):
                    for subformula2 in give_type(arg2, (set, set2)):
                        yield Typed_Composition(subformula1, subformula2)
        
        
def make_rules_typed():
    # Load the rule dictionary from file
    with open('cor_dict.pickle', 'rb') as file:
        cor_dict = pickle.load(file)
        
    typed_rules_dict = dict()
        
    for lhs in cor_dict:
        rhs = cor_dict[lhs]
        typed_lhs = list(make_homogeneous_formula_typed(lhs))
        for formula in typed_lhs:
            typed_rhs = list(give_type(rhs, formula.type()))
            for formula2 in typed_rhs:
                first_translated = formula.translate('x', 'y')
                second_translated = formula2.translate('x', 'y')
                s = z3.Solver()
                try:
                    s.add(z3.Not(Typed_Testing.typed_asZ3(first_translated) == Typed_Testing.typed_asZ3(second_translated)))
                    s.set("timeout", 500)
                    z3result = s.check()
                    if z3result == z3.unsat:
                        typed_rules_dict[formula] = formula2
                        print(formula, " -> ", formula2)
                except:
                    pass
                    
    # Save the new typed rule dictionary to file
    with open('typed_cor_dict.pickle', 'wb') as file:
        pickle.dump(typed_rules_dict, file, protocol=pickle.HIGHEST_PROTOCOL)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__": 
    #make_rules_typed()
    
    with open('typed_cor_dict.pickle', 'rb') as file:
        typed_cor_dict = pickle.load(file)
    Search_For_Simplification_Rules.print_rule_dictionary(typed_cor_dict, True, "Typed_COR_Rules.txt")
    Search_For_Simplification_Rules.generate_code_from_cor_rules(typed_cor_dict, "Typed_Simplify.py", True)
