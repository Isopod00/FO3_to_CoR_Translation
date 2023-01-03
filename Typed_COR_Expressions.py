# Authors: Sebastiaan Joosten, Anthony Brogni

from Typed_FO3_Expressions import *


class Typed_UniversalRelation:
    """ This class describes the COR mathematical symbol T (universal relation) on set1 and set2"""

    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __str__(self) -> str:
        return 'T'

    def translate(self, arg1, arg2) -> tt:
        return tt()


class Typed_EmptyRelation:
    """ This class describes the COR mathematical symbol 𝟎 (empty relation) on set1 and set2"""

    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def __str__(self) -> str:
        return '𝟎'

    def translate(self, arg1, arg2) -> ff:
        return ff()


class Typed_IdentityRelation:
    """ This class describes the COR mathematical symbol 𝟏 (identity relation) on set1 and set2 """

    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

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

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def translate(self, arg1, arg2) -> ThereExists:
        fresh_var = [var for var in ['x', 'y', 'z'] if var not in [arg1.var, arg2.var]]
        fresh_set = [s for s in ['Q', 'R', 'S'] if s not in [arg1.set, arg2.set]]
        newtypedvar = Typed_Variable(fresh_var.pop(), fresh_set.pop())
        return ThereExists(newtypedvar, make_AND(self.argument1.translate(arg1, newtypedvar),
                                                 self.argument2.translate(newtypedvar, arg2)))


class Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) † ({self.argument2})'

    # This is assuming that argument1 contains pairs (x, z) and argument2 contains pairs (z, y)
    def translate(self, arg1, arg2) -> ForAll:
        fresh_var = [var for var in ['x', 'y', 'z'] if var not in [arg1.var, arg2.var]]
        fresh_set = [s for s in ['Q', 'R', 'S'] if s not in [arg1.set, arg2.set]]
        newtypedvar = Typed_Variable(fresh_var.pop(), fresh_set.pop())
        return ForAll(newtypedvar,
                      make_OR(self.argument1.translate(arg1, newtypedvar), self.argument2.translate(newtypedvar, arg2)))


class Typed_Relation:
    """ This class represents a single relation denoted by the letter argument on set1 and set2"""

    def __init__(self, letter, set1, set2):
        self.letter = letter
        self.set1 = set1
        self.set2 = set2

    def __str__(self) -> str:
        return self.letter

    # This is assuming the relations we are discussing contain pairs (arg1, arg2)
    def translate(self, arg1, arg2) -> Predicate:
        return Predicate(self.letter, arg1, arg2)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = Union(Complement(Composition(Typed_Relation("A", 'Q', 'R'), Typed_Relation("B", 'R', 'Q'))),
                            Intersection(Converse(Typed_Relation("C", 'S', 'Q')), Typed_IdentityRelation('Q', 'Q')))

    x = Typed_Variable('x', 'Q')
    y = Typed_Variable('y', 'R')
    print("Original Expression:", test_expression)  # Original expression
    print("Translated Expression:", test_expression.translate(x, y))  # Translated expression
    print("Negation Normal Form:", negation_normal(test_expression.translate(x, y)))  # Negation normal form
