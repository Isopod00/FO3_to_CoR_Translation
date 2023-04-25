# Author: Anthony Brogni
# Last Changed: May 2023
""" This file is for creating typed simplification rules from the untyped rules we have found with Search_For_Simplification_Rules.py. """

from COR_Expressions import *
from Typed_COR_Expressions import *

# Takes an untyped COR expression and applies types to it
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
                    yield Typed_Relation(set1, set2)
        case Complement(argument=arg):
            yield Typed_Complement(make_homogeneous_formula_typed(arg))
        case Converse(argument=arg):
            yield Typed_Converse(make_homogeneous_formula_typed(arg))
        case Union(argument1=arg1, argument2=arg2):
            yield Typed_Union(make_homogeneous_formula_typed(arg1), make_homogeneous_formula_typed(arg2))
        case Intersection(argument1=arg1, argument2=arg2):
            yield Typed_Intersection(make_homogeneous_formula_typed(arg1), make_homogeneous_formula_typed(arg2))
        case Dagger(argument1=arg1, argument2=arg2):
            yield Typed_Dagger(make_homogeneous_formula_typed(arg1), make_homogeneous_formula_typed(arg2))
        case Composition(argument1=arg1, argument2=arg2):
            yield Typed_Composition(make_homogeneous_formula_typed(arg1), make_homogeneous_formula_typed(arg2))
        

# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__": 
    print([str(formula) for formula in make_homogeneous_formula_typed(UniversalRelation())])
