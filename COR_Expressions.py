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

    def __str__(self):
        return f'({self.relation})⁻¹'

    def _translate(self):
        if isinstance(self.relation, str):
            return Negation(self.relation)
        else:
            return Negation(self.relation._translate())


class Union:
    """This class describes the union between two relations arg1 and arg2, which can be any relations"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self):
        return f'({self.argument1}) ∪ ({self.argument2})'

    def _translate(self):
        if isinstance(self.argument1, str) and isinstance(self.argument2, str):
            return OR(self.argument1, self.argument2)
        elif isinstance(self.argument1, str):
            return OR(self.argument1, self.argument2._translate())
        elif isinstance(self.argument2, str):
            return OR(self.argument1._translate(), self.argument2)
        else:
            return OR(self.argument1._translate(), self.argument2._translate())


class Intersection:
    """This class describes the intersection between two relations arg1 and arg2, which can be any relations"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self):
        return f'({self.argument1}) ∩ ({self.argument2})'

    def _translate(self):
        if isinstance(self.argument1, str) and isinstance(self.argument2, str):
            return AND(self.argument1, self.argument2)
        elif isinstance(self.argument1, str):
            return AND(self.argument1, self.argument2._translate())
        elif isinstance(self.argument2, str):
            return AND(self.argument1._translate(), self.argument2)
        else:
            return AND(self.argument1._translate(), self.argument2._translate())


class Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, z) | (x, y) ∈ arg1 ∧ (y, z) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self):
        return f'{self.argument1} ∘ {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self):
        if isinstance(self.argument1, str) and isinstance(self.argument2, str):
            return ThereExists("z", AND(self.argument1, self.argument2))
        elif isinstance(self.argument1, str):
            return ThereExists("z", AND(self.argument1, self.argument2._translate()))
        elif isinstance(self.argument2, str):
            return ThereExists("z", AND(self.argument1._translate(), self.argument2))
        else:
            return ThereExists("z", AND(self.argument1._translate(), self.argument2._translate()))


class Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self):
        return f'{self.argument1} † {self.argument2}'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def _translate(self):
        if isinstance(self.argument1, str) and isinstance(self.argument2, str):
            return ForAll("z", OR(self.argument1, self.argument2))
        elif isinstance(self.argument1, str):
            return ForAll("z", OR(self.argument1, self.argument2._translate()))
        elif isinstance(self.argument2, str):
            return ForAll("z", OR(self.argument1._translate(), self.argument2))
        else:
            return ForAll("z", OR(self.argument1._translate(), self.argument2._translate()))


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    expression = Union(Converse(Composition("A", "B")), Intersection(Converse("B"), IdentityRelation()))

    print("Original Expression:", expression)  # Original expression
    print("Translated Expression:", expression._translate())  # Translated expression
    print("Negation Normal Form:", expression._translate()._negation_normal_form())  # Negation normal form
