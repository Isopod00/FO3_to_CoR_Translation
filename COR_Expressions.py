from FO3_Expressions import *


class UniversalRelation:
    """ This class describes the COR mathematical symbol T (universal relation) """

    def __str__(self) -> str:
        return 'T'

    def _translate(self) -> tt:
        return tt()


class EmptyRelation:
    """ This class describes the COR mathematical symbol 𝟎 (empty relation) """

    def __str__(self) -> str:
        return '𝟎'

    def _translate(self) -> ff:
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

    def _translate(self) -> Negation:
        if isinstance(self.argument, Relation) or isinstance(self.argument, IdentityRelation):
            return Negation(self.argument._translate("x", "y"))
        else:
            return Negation(self.argument._translate())


class Union:
    """This class describes the union between two relations arg1 and arg2, which can be any relations """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∪ ({self.argument2})'

    def _translate(self) -> OR:
        if isinstance(self.argument1, Relation) or isinstance(self.argument1, IdentityRelation):
            left = self.argument1._translate("x", "y")
        else:
            left = self.argument1._translate()
        if isinstance(self.argument2, Relation) or isinstance(self.argument2, IdentityRelation):
            right = self.argument2._translate("x", "y")
        else:
            right = self.argument2._translate()
        return OR(left, right)


class Intersection:
    """This class describes the intersection between two relations arg1 and arg2, which can be any relations """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∩ ({self.argument2})'

    def _translate(self) -> AND:
        if isinstance(self.argument1, Relation) or isinstance(self.argument1, IdentityRelation):
            left = self.argument1._translate("x", "y")
        else:
            left = self.argument1._translate()
        if isinstance(self.argument2, Relation) or isinstance(self.argument2, IdentityRelation):
            right = self.argument2._translate("x", "y")
        else:
            right = self.argument2._translate()
        return AND(left, right)


class Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, y) | (x, z) ∈ arg1 ∧ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'{self.argument1} ∘ {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self) -> ThereExists:
        return ThereExists('z', AND(self.argument1._translate("x", "z"), self.argument2._translate("z", "y")))


class Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'{self.argument1} † {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self) -> ForAll:
        return ForAll('z', OR(self.argument1._translate("x", "z"), self.argument2._translate("z", "y")))


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
    expression = Union(Converse(Composition(Relation("A"), Relation("B"))),
                       Intersection(Converse(Relation("C")), IdentityRelation()))

    print("Original Expression:", expression)  # Original expression
    print("Translated Expression:", expression._translate())  # Translated expression
    print("Negation Normal Form:", expression._translate()._negation_normal_form())  # Negation normal form
