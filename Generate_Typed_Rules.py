# Author: Anthony Brogni
# Last Changed: May 2023
""" This file is for creating typed simplification rules from the untyped rules we have found with Search_For_Simplification_Rules.py. """

import pickle
import z3  # pip install z3-solver

import Typed_Testing
import Typed_Simplify
import Search_For_Simplification_Rules
from COR_Expressions import *
from Typed_COR_Expressions import *


def make_homogeneous_formula_typed(formula):
    """ Takes an untyped COR expression and applies all valid types to it """
    for i in give_type(formula, ('P', 'P')):
        yield i
    for i in give_type(formula, ('P', 'Q')):
        yield i


def give_type(formula, type):
    """ Takes an untyped COR expression and applies the specified type to it (type is an ordered pair) """
    set1 = type[0]
    set2 = type[1]
    match formula:
        case UniversalRelation():
            yield Typed_UniversalRelation(set1, set2)
        case EmptyRelation():
            yield Typed_EmptyRelation(set1, set2)
        case IdentityRelation():
            if set1 == set2:
                yield Typed_IdentityRelation(set1, set2)
        case Relation(letter=l):
            yield Typed_Relation(l, set1, set2)
        case Complement(argument=arg):
            for subformula in give_type(arg, type):
                yield Typed_Complement(subformula)
        case Converse(argument=arg):
            for subformula in give_type(arg, (type[1], type[0])):
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
        for first in typed_lhs:
            typed_rhs = list(give_type(rhs, first.type()))
            for second in typed_rhs:
                first_translated = first.translate('x', 'y')
                second_translated = second.translate('x', 'y')
                s = z3.Solver()
                s.set("timeout", 100)
                z3result = s.check(z3.Not(Typed_Testing.typed_asZ3(
                    first_translated) == Typed_Testing.typed_asZ3(second_translated)))
                if z3result == z3.unsat:
                    typed_rules_dict[first] = second
                    print(f'quickly found: {first} = {second}')
                elif z3result == z3.sat:
                    print(f'refuted: {first} = {second}')
                else:
                    q = ('Stuck at: ' + str(first) + ' -> ' + str(second))
                    print('reverting to enum univ')
                    s.set("timeout", 6000)

                    fallback_enum, (_, _, _, _) = z3.EnumSort(
                        f'univ', ['SA', 'SB', 'SC', 'SD'])
                    assert isinstance(fallback_enum, z3.SortRef)
                    z3result = s.check(z3.Not(Typed_Testing.typed_asZ3(
                        first_translated, fallback_enum) == Typed_Testing.typed_asZ3(second_translated, fallback_enum)))
                    if z3result == z3.unsat:
                        print(q+'\nGoing into slow mode...')
                        s = z3.Solver()
                        s.set("timeout", 60000)
                        z3result = s.check(z3.Not(Typed_Testing.typed_asZ3(
                            first_translated) == Typed_Testing.typed_asZ3(second_translated)))
                        if z3result == z3.unsat:
                            print('successful rule found by using more time!')
                            typed_rules_dict[first] = second
                        elif z3result == z3.sat:
                            print('successful refutation found by using more time!')
                        else:
                            raise Exception("Z3 does not know the answer!\n"+q)
                    elif z3result == z3.sat:
                        # this happens quite a lot
                        print('counter example found for a small universe')
                    else:
                        q = ('Stuck at: ' + str(first) + ' -> ' + str(second))
                        raise Exception(
                            "Z3 times out even in the finite case!\n"+q)

    # Save the new typed rule dictionary to file
    with open('typed_cor_dict.pickle', 'wb') as file:
        pickle.dump(typed_rules_dict, file, protocol=pickle.HIGHEST_PROTOCOL)


def delete_generalizable_rules():
    new_dict = dict()

    # Load the rule dictionary from file
    with open('typed_cor_dict.pickle', 'rb') as file:
        typed_cor_dict = pickle.load(file)

    for lhs in typed_cor_dict:
        rule_applied = Typed_Simplify.simplify(lhs)[0]
        if rule_applied is not None:
            # Only keep it if the rule applied matches lhs
            if rule_applied.split(" =")[0] == str(lhs):
                new_dict[lhs] = typed_cor_dict[lhs]
            else:
                print("Deleted Rule:", str(lhs) +
                      " = " + str(typed_cor_dict[lhs]))
                print("Rule Used Instead Was:", rule_applied)
        else:
            raise Exception("rule_applied should not be None. lhs =", lhs)

    # Save the new typed rule dictionary to file
    with open('typed_cor_dict.pickle', 'wb') as file:
        pickle.dump(new_dict, file, protocol=pickle.HIGHEST_PROTOCOL)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    # Make typed versions of our homogeneous rules
    make_rules_typed()

    # Delete all generalizable rules
    delete_generalizable_rules()
    with open('typed_cor_dict.pickle', 'rb') as file:
        typed_cor_dict = pickle.load(file)
    Search_For_Simplification_Rules.print_rule_dictionary(
        typed_cor_dict, "Typed_COR_Rules.txt")
    Search_For_Simplification_Rules.generate_code_from_cor_rules(
        typed_cor_dict, "Typed_Simplify.py", True)
    delete_generalizable_rules()
    with open('typed_cor_dict.pickle', 'rb') as file:
        typed_cor_dict = pickle.load(file)
    Search_For_Simplification_Rules.print_rule_dictionary(
        typed_cor_dict, "Typed_COR_Rules.txt")
    Search_For_Simplification_Rules.generate_code_from_cor_rules(
        typed_cor_dict, "Typed_Simplify.py", True, True)
    delete_generalizable_rules()
    with open('typed_cor_dict.pickle', 'rb') as file:
        typed_cor_dict = pickle.load(file)
    Search_For_Simplification_Rules.print_rule_dictionary(
        typed_cor_dict, "Typed_COR_Rules.txt")
    Search_For_Simplification_Rules.generate_code_from_cor_rules(
        typed_cor_dict, "Typed_Simplify.py", True)
