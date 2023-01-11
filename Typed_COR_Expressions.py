# Authors: Sebastiaan Joosten, Anthony Brogni

from FO3_Expressions import *


class Typed_UniversalRelation:
    """ This class describes the COR mathematical symbol T (universal relation) on two sets: s1 and s2 """

    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2

    def __str__(self) -> str:
        return f'T[{self.set1}*{self.set2}]'

    def translate(self, arg1, arg2) -> tt:
        return tt()

    def type(self) -> list:
        return [self.set1, self.set2]


class Typed_EmptyRelation:
    """ This class describes the COR mathematical symbol 𝟎 (empty relation) on two sets: s1 and s2 """

    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2

    def __str__(self) -> str:
        return f'𝟎[{self.set1}*{self.set2}]'

    def translate(self, arg1, arg2) -> ff:
        return ff()

    def type(self) -> list:
        return [self.set1, self.set2]


class Typed_IdentityRelation:
    """ This class describes the COR mathematical symbol 𝟏 (identity relation) on two sets: s1 and s2 """

    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2

    def __str__(self) -> str:
        return f'𝟏[{self.set1}*{self.set2}]'

    def translate(self, arg1, arg2) -> Equals:
        return Equals(Typed_Variable(arg1, self.set1), Typed_Variable(arg2, self.set2))

    def type(self) -> list:
        return [self.set1, self.set2]


class Typed_Converse:
    """ This class describes the converse of a typed RELATION (R⁻¹), which is all (b, a) such that (a, b) ∈ R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻¹'

    def type(self) -> list:
        return [self.argument.type()[1], self.argument.type()[0]]

    def translate(self, arg1, arg2):
        match self.argument:
            case Typed_Relation(letter=l, set1=s1, set2=s2):
                return Predicate(l, Typed_Variable(arg2, s2), Typed_Variable(arg1, s1))
            case Typed_IdentityRelation(set1=s1, set2=s2):
                return Equals(Typed_Variable(arg2, s2), Typed_Variable(arg1, s1))
            case Typed_UniversalRelation():
                return tt()  # TODO: I believe this needs to be changed
            case Typed_EmptyRelation():
                return ff()  # TODO: I believe this needs to be changed


class Typed_Complement:
    """ This class describes the complement of a typed relation (R⁻ ) which is all (a, b) not in R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻'

    def translate(self, arg1, arg2) -> Negation:
        return Negation(self.argument.translate(arg1, arg2))

    def type(self) -> list:
        return self.argument.type()


class Typed_Union:
    """This class describes the union between two typed relations arg1 and arg2 """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∪ ({self.argument2})'

    def translate(self, arg1, arg2) -> OR:
        return make_OR(self.argument1.translate(arg1, arg2), self.argument2.translate(arg1, arg2))

    def type(self) -> list:
        return self.argument1.type()


class Typed_Intersection:
    """This class describes the intersection between two typed relations arg1 and arg2 """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∩ ({self.argument2})'

    def translate(self, arg1, arg2) -> AND:
        return make_AND(self.argument1.translate(arg1, arg2), self.argument2.translate(arg1, arg2))

    def type(self) -> list:
        return self.argument1.type()


class Typed_Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, y) | (x, z) ∈ arg1 ∧ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∘ ({self.argument2})'

    def type(self) -> list:
        return [self.argument1.type()[0], self.argument2.type()[1]]

    def translate(self, arg1, arg2) -> ThereExists:
        fresh_var = [var for var in ['x', 'y', 'z'] if var not in [arg1, arg2]]
        newset = self.argument1.type()[1]
        newvar = fresh_var.pop()
        return ThereExists(Typed_Variable(newvar, newset), make_AND(self.argument1.translate(arg1, newvar),
                                                                    self.argument2.translate(newvar, arg2)))


class Typed_Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) † ({self.argument2})'

    def type(self) -> list:
        return [self.argument1.type()[0], self.argument2.type()[1]]

    def translate(self, arg1, arg2) -> ForAll:
        fresh_var = [var for var in ['x', 'y', 'z'] if var not in [arg1, arg2]]
        newset = self.argument1.type()[1]
        newvar = fresh_var.pop()
        return ForAll(Typed_Variable(newvar, newset),
                      make_OR(self.argument1.translate(arg1, newvar), self.argument2.translate(newvar, arg2)))


class Typed_Relation:
    """ This class represents a relation on two sets: s1 and s2 """

    def __init__(self, letter, s1, s2):
        self.letter = letter
        self.set1 = s1
        self.set2 = s2

    def __str__(self) -> str:
        return f'{self.letter}[{self.set1}*{self.set2}]'

    # This is assuming the relations we are discussing contain pairs (arg1, arg2)
    def translate(self, arg1, arg2) -> Predicate:
        return Predicate(self.letter, Typed_Variable(arg1, self.set1), Typed_Variable(arg2, self.set2))

    def type(self) -> list:
        return [self.set1, self.set2]


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = Typed_Dagger(Typed_Relation('A', 'Q', 'S'), Typed_Relation('B', 'S', 'R'))

    print("Original Expression:", test_expression)  # Original expression
    print("Translated Expression:", test_expression.translate('x', 'y'))  # Translated expression
    print("Negation Normal Form:", negation_normal(test_expression.translate('x', 'y')))  # Negation normal form
