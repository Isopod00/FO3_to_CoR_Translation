from FO3_Expressions import *


class UniversalRelation:
    """ This class describes the COR mathematical symbol T (universal relation) """

    def __str__(self) -> str:
        return 'T'

    def _translate(self, arg1, arg2) -> tt:
        return tt()


class EmptyRelation:
    """ This class describes the COR mathematical symbol 𝟎 (empty relation) """

    def __str__(self) -> str:
        return '𝟎'

    def _translate(self, arg1, arg2) -> ff:
        return ff()


class IdentityRelation:
    """ This class describes the COR mathematical symbol 𝟏 (identity relation) """

    def __str__(self) -> str:
        return '𝟏'

    # This is assuming the relations we are discussing contain pairs (arg1, arg2)
    def _translate(self, arg1, arg2) -> Equals:
        return Equals(arg1, arg2)


class Converse:
    """ This class describes the converse of a relation (R⁻¹), which is all (b, a) such that (a, b) ∈ R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻¹'

    def _translate(self, arg1, arg2):
        return self.argument._translate(arg2, arg1)


class Complement:
    """ This class describes the complement of a relation (R⁻ ) which is all (a, b) not in R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻'

    def _translate(self, arg1, arg2) -> Negation:
        return Negation(self.argument._translate(arg1, arg2))


class Union:
    """This class describes the union between two relations arg1 and arg2, which can be any relations """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∪ ({self.argument2})'

    def _translate(self, arg1, arg2) -> OR:
        return OR(self.argument1._translate(arg1, arg2), self.argument2._translate(arg1, arg2))


class Intersection:
    """This class describes the intersection between two relations arg1 and arg2, which can be any relations """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∩ ({self.argument2})'

    def _translate(self, arg1, arg2) -> AND:
        return AND(self.argument1._translate(arg1, arg2), self.argument2._translate(arg1, arg2))


class Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, y) | (x, z) ∈ arg1 ∧ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'{self.argument1} ∘ {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self, arg1, arg2) -> ThereExists:
        return ThereExists('z', AND(self.argument1._translate(arg1, "z"), self.argument2._translate("z", arg2)))


class Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'{self.argument1} † {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self, arg1, arg2) -> ForAll:
        return ForAll('z', OR(self.argument1._translate(arg1, "z"), self.argument2._translate("z", arg2)))


class Relation:
    """ This class represents a single relation denoted by the letter argument """

    def __init__(self, letter):
        self.letter = letter

    def __str__(self) -> str:
        return self.letter

    # This is assuming the relations we are discussing contain pairs (arg1, arg2)
    def _translate(self, arg1, arg2) -> Predicate:
        return Predicate(self.letter, arg1, arg2)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    expression = Union(Complement(Composition(Relation("A"), Relation("B"))),
                       Intersection(Converse(Relation("C")), IdentityRelation()))

    print("Original Expression:", expression)  # Original expression
    print("Translated Expression:", expression._translate("x", "y"))  # Translated expression
    print("Negation Normal Form:", expression._translate("x", "y")._negation_normal_form())  # Negation normal form
