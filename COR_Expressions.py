from FO3_Expressions import *


class UniversalRelation:
    """ This class describes the COR mathematical symbol T (universal relation) """

    def __str__(self) -> str:
        return 'T'

    def _translate(self):
        return tt()


class EmptyRelation:
    """ This class describes the COR mathematical symbol 𝟎 (empty relation) """

    def __str__(self) -> str:
        return '𝟎'

    def _translate(self):
        return ff()


class IdentityRelation:
    """ This class describes the COR mathematical symbol 𝟏 (identity relation) """

    def __str__(self) -> str:
        return '𝟏'

    def _translate(self):
        return Equals("x", "y")  # This is assuming the relations we are discussing contain pairs (x, y)


class Converse:
    """ This class describes the converse of a relation (R⁻¹), which is all (b, a) such that (a, b) ∈ R"""

    def __init__(self, rel):
        self.relation = rel

    def __str__(self) -> str:
        return f'({self.relation})⁻¹'

    def _translate(self):
        return Negation(self.relation._translate())


class Union:
    """This class describes the union between two relations arg1 and arg2, which can be any relations"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∪ ({self.argument2})'

    def _translate(self):
        return OR(self.argument1._translate(), self.argument2._translate())


class Intersection:
    """This class describes the intersection between two relations arg1 and arg2, which can be any relations"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∩ ({self.argument2})'

    def _translate(self):
        return AND(self.argument1._translate(), self.argument2._translate())


class Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, z) | (x, y) ∈ arg1 ∧ (y, z) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'{self.argument1} ∘ {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self):
        return ThereExists(f'{self.argument2.second_number}',
                           AND(self.argument1._translate(), self.argument2._translate()))


class Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'{self.argument1} † {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self):
        return ForAll(f'{self.argument2.second_number}', OR(self.argument1._translate(), self.argument2._translate()))


class Relation:
    """ This class represents a single relation with ordered pairs (arg1, arg2) and denoted by the letter argument"""

    def __init__(self, letter, arg1, arg2):
        self.first_number = arg1
        self.second_number = arg2
        self.letter = letter

    def __str__(self) -> str:
        return self.letter

    def _translate(self) -> str:
        return f'{self.letter}({self.first_number},{self.second_number})'


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    expression = Union(Converse(Composition(Relation("A", "x", "y"), Relation("B", "y", "z"))),
                       Intersection(Converse(Relation("B", "y", "z")), IdentityRelation()))

    print("Original Expression:", expression)  # Original expression
    print("Translated Expression:", expression._translate())  # Translated expression
    print("Negation Normal Form:", expression._translate()._negation_normal_form())  # Negation normal form
