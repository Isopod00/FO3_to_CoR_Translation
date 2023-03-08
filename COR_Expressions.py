# Authors: Sebastiaan J. C. Joosten, Anthony Brogni
# Last Changed: March 2023
""" This file contains everything you need to build (untyped) mathematical COR objects in Python. """

from FO3_Expressions import *


class UniversalRelation:
    """ This class describes the COR mathematical symbol T (universal relation) """

    def __str__(self) -> str:
        return 'T'

    def translate(self, arg1, arg2) -> tt:
        return tt()


class EmptyRelation:
    """ This class describes the COR mathematical symbol 𝟎 (empty relation) """

    def __str__(self) -> str:
        return '𝟎'

    def translate(self, arg1, arg2) -> ff:
        return ff()


class IdentityRelation:
    """ This class describes the COR mathematical symbol 𝟏 (identity relation) """

    def __str__(self) -> str:
        return '𝟏'

    # This is assuming the relations we are discussing contain pairs (arg1, arg2)
    def translate(self, arg1, arg2) -> Equals:
        return Equals(arg1, arg2)


class Converse:
    """ This class describes the converse of a relation (R⁻¹), which is all (b, a) such that (a, b) ∈ R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻¹'

    def translate(self, arg1, arg2):
        return self.argument.translate(arg2, arg1)


class Complement:
    """ This class describes the complement of a relation (R⁻ ) which is all (a, b) not in R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻'

    def translate(self, arg1, arg2) -> Negation:
        return Negation(self.argument.translate(arg1, arg2))


class Union:
    """This class describes the union between two relations arg1 and arg2, which can be any relations """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∪ ({self.argument2})'

    def translate(self, arg1, arg2) -> OR:
        return make_OR(self.argument1.translate(arg1, arg2), self.argument2.translate(arg1, arg2))


class Intersection:
    """This class describes the intersection between two relations arg1 and arg2, which can be any relations """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∩ ({self.argument2})'

    def translate(self, arg1, arg2) -> AND:
        return make_AND(self.argument1.translate(arg1, arg2), self.argument2.translate(arg1, arg2))


class Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, y) | (x, z) ∈ arg1 ∧ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∘ ({self.argument2})'

    # This is assuming that argument1 contains pairs (arg1, newvar) and argument2 contains pairs (newvar, arg2)
    def translate(self, arg1, arg2) -> ThereExists:
        fresh = [var for var in ['x', 'y', 'z'] if var not in [arg1, arg2]]
        newvar = fresh.pop()
        return ThereExists(newvar,
                           make_AND(self.argument1.translate(arg1, newvar), self.argument2.translate(newvar, arg2)))


class Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) † ({self.argument2})'

    # This is assuming that argument1 contains pairs (arg1, newvar) and argument2 contains pairs (newvar, arg2)
    def translate(self, arg1, arg2) -> ForAll:
        fresh = [var for var in ['x', 'y', 'z'] if var not in [arg1, arg2]]
        newvar = fresh.pop()
        return ForAll(newvar, make_OR(self.argument1.translate(arg1, newvar), self.argument2.translate(newvar, arg2)))


class Relation:
    """ This class represents a single relation denoted by the letter argument """

    def __init__(self, letter):
        self.letter = letter

    def __str__(self) -> str:
        return self.letter

    # This is assuming the relations we are discussing contain pairs (arg1, arg2)
    def translate(self, arg1, arg2) -> Predicate:
        return Predicate(self.letter, arg1, arg2)


def fully_simplify_COR(expression):
    """ Fully simplifies a COR expression """
    previous_iteration = expression
    expression = simplify_COR(expression)
    while str(previous_iteration) != str(expression):
        previous_iteration = expression
        expression = simplify_COR(expression)
    return expression


def simplify_COR(expression):
    """ Simplifies a COR expression """
    match expression:
        case Complement(argument=arg):
            match arg:
                case UniversalRelation():
                    return EmptyRelation()
                case EmptyRelation():
                    return UniversalRelation()
                case _:
                    return Complement(simplify_COR(arg))
        case Dagger(argument1=arg1, argument2=arg2):
            if isinstance(arg1, EmptyRelation) and isinstance(arg2, EmptyRelation):
                return EmptyRelation()
            elif isinstance(arg1, EmptyRelation) and isinstance(arg2, UniversalRelation):
                return UniversalRelation()
            elif isinstance(arg1, UniversalRelation) and isinstance(arg2, EmptyRelation):
                return UniversalRelation()
            else:
                return Dagger(simplify_COR(arg1), simplify_COR(arg2))
        case Composition(argument1=arg1, argument2=arg2):
            if isinstance(arg1, IdentityRelation):
                return simplify_COR(arg2)
            elif isinstance(arg2, IdentityRelation):
                return simplify_COR(arg1)
            elif isinstance(arg1, UniversalRelation) and isinstance(arg2, UniversalRelation):
                return UniversalRelation()
            else:
                return Composition(simplify_COR(arg1), simplify_COR(arg2))
        case Union(argument1=arg1, argument2=arg2):
            if isinstance(arg1, EmptyRelation):
                return simplify_COR(arg2)
            elif isinstance(arg2, EmptyRelation):
                return simplify_COR(arg1)
            elif isinstance(arg1, UniversalRelation) or isinstance(arg2, UniversalRelation):
                return UniversalRelation()
            else:
                return Union(simplify_COR(arg1), simplify_COR(arg2))
        case Intersection(argument1=arg1, argument2=arg2):
            if isinstance(arg1, UniversalRelation):
                return simplify_COR(arg2)
            elif isinstance(arg2, UniversalRelation):
                return simplify_COR(arg1)
            elif isinstance(arg1, EmptyRelation) or isinstance(arg2, EmptyRelation):
                return EmptyRelation()
            else:
                return Intersection(simplify_COR(arg1), simplify_COR(arg2))
        case _:
            return expression


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = Union(Complement(Composition(Relation("A"), Relation("B"))),
                            Intersection(Converse(Relation("C")), IdentityRelation()))

    print("Original Expression:  ", test_expression)  # Original expression
    print("Simplified:           ", fully_simplify_COR(test_expression))  # Simplified expression
    print("Translated Expression:", test_expression.translate("x", "y"))  # Translated expression
    print("Negation Normal Form: ", negation_normal(test_expression.translate("x", "y")))  # Negation normal form
    print("Simplified:           ", fully_simplify_FO3(negation_normal(test_expression.translate("x", "y"))))
