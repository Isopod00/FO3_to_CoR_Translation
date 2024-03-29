# Authors: Sebastiaan J. C. Joosten, Anthony Brogni
# Last Changed: March 2023

""" This file contains everything you need to build
object representations of heterogeneous/typed COR formulas in Python! """

from FO3_Expressions import *


class Typed_UniversalRelation:
    """ This class describes the universal relation on two sets: s1 and s2 """

    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2

    def __str__(self) -> str:
        return f'T[{self.set1}*{self.set2}]'

    def translate(self, arg1, arg2) -> tt:
        return tt()

    def type(self) -> list:
        return [self.set1, self.set2]

    def size(self) -> int:
        return 1

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_UniversalRelation({type1}, {type2})"


class Typed_EmptyRelation:
    """ This class describes the empty relation on two sets: s1 and s2 """

    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2

    def __str__(self) -> str:
        return f'𝟎[{self.set1}*{self.set2}]'

    def translate(self, arg1, arg2) -> ff:
        return ff()

    def type(self) -> list:
        return [self.set1, self.set2]

    def size(self) -> int:
        return 1

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_EmptyRelation({type1}, {type2})"


class Typed_IdentityRelation:
    """ This class describes the identity relation on two sets: s1 and s2 """

    def __init__(self, s1, s2):
        self.set1 = s1
        self.set2 = s2
        if s1 != s2:  # Type checking
            raise Exception(
                f'ERROR: Identity type mismatch! Type 1 is:{s1} and Type 2 is:{s2}')

    def __str__(self) -> str:
        return f'𝟏[{self.set1}*{self.set2}]'

    def translate(self, arg1, arg2) -> Equals:
        return Equals(Typed_Variable(arg1, self.set1), Typed_Variable(arg2, self.set2))

    def type(self) -> list:
        return [self.set1, self.set2]

    def size(self) -> int:
        return 1

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_IdentityRelation({type1}, {type2})"


class Typed_Converse:
    """ This class describes the converse of a typed relation (R⁻¹), which is all (b, a) such that (a, b) ∈ R """

    def __init__(self, arg):
        self.argument = arg

    def __str__(self) -> str:
        return f'({self.argument})⁻¹'

    def type(self) -> list:
        return [self.argument.type()[1], self.argument.type()[0]]

    def translate(self, arg1, arg2):
        return self.argument.translate(arg2, arg1)

    def size(self) -> int:
        return 1 + self.argument.size()

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_Converse({self.argument.object_representation(type2, type1)})"


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

    def size(self) -> int:
        return 1 + self.argument.size()

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_Complement({self.argument.object_representation(type1, type2)})"


class Typed_Union:
    """ This class describes the union between two typed relations arg1 and arg2 """

    def __init__(self, arg1, arg2):
        if arg1.type() != arg2.type():  # Type checking
            raise Exception(
                f'ERROR: Union type mismatch! Type 1 is:{arg1.type()} and Type 2 is:{arg2.type()}')
        else:
            self.argument1 = arg1
            self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∪ ({self.argument2})'

    def translate(self, arg1, arg2) -> OR:
        return make_OR(self.argument1.translate(arg1, arg2), self.argument2.translate(arg1, arg2))

    def type(self) -> list:
        return self.argument1.type()

    def size(self) -> int:
        return 1 + self.argument1.size() + self.argument2.size()

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_Union({self.argument1.object_representation(type1, type2)}, {self.argument2.object_representation(type1, type2)})"


class Typed_Intersection:
    """ This class describes the intersection between two typed relations arg1 and arg2 """

    def __init__(self, arg1, arg2):
        if arg1.type() != arg2.type():  # Type checking
            raise Exception(
                f'ERROR: Intersection type mismatch! Type 1 is:{arg1.type()} and Type 2 is:{arg2.type()}')
        else:
            self.argument1 = arg1
            self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∩ ({self.argument2})'

    def translate(self, arg1, arg2) -> AND:
        return make_AND(self.argument1.translate(arg1, arg2), self.argument2.translate(arg1, arg2))

    def type(self) -> list:
        return self.argument1.type()

    def size(self) -> int:
        return 1 + self.argument1.size() + self.argument2.size()

    def object_representation(self, type1, type2) -> str:
        return f"Typed_COR_Expressions.Typed_Intersection({self.argument1.object_representation(type1, type2)}, {self.argument2.object_representation(type1, type2)})"


class Typed_Composition:
    """ This class describes the composition operation arg1 ∘ arg2 = {(x, y) | (x, z) ∈ arg1 ∧ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        if arg1.type()[1] != arg2.type()[0]:  # Type checking
            raise Exception(
                f'ERROR: Composition type mismatch! Type 1 is:{arg1.type()} and Type 2 is:{arg2.type()}')
        else:
            self.argument1 = arg1
            self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) ∘ ({self.argument2})'

    def type(self) -> list:
        return [self.argument1.type()[0], self.argument2.type()[1]]

    def translate(self, arg1, arg2) -> ThereExists:
        fresh_var = [var for var in ['x', 'y', 'z'] if var not in [arg1, arg2]]
        # Or self.argument2.type()[0] is also correct, they should be the same
        newset = self.argument1.type()[1]
        newvar = fresh_var.pop()
        return ThereExists(Typed_Variable(newvar, newset), make_AND(self.argument1.translate(arg1, newvar),
                                                                    self.argument2.translate(newvar, arg2)))

    def size(self) -> int:
        return 1 + self.argument1.size() + self.argument2.size()

    def object_representation(self, type1, type2) -> str:
        middle_type = self.argument1.type()[1]
        if isinstance(self.argument1, Typed_Relation):
            middle_type = f"{self.argument1.object_representation('left', 'right')}.type()[1]"
        elif isinstance(self.argument2, Typed_Relation):
            middle_type = middle_type = f"{self.argument2.object_representation('left', 'right')}.type()[0]"
        return f"Typed_COR_Expressions.Typed_Composition({self.argument1.object_representation(type1, middle_type)}, {self.argument2.object_representation(middle_type, type2)})"


class Typed_Dagger:
    """ This class describes the dagger operation arg1 † arg2 = {(x, y) | (x, z) ∈ arg1 ∨ (z, y) ∈ arg2} """

    def __init__(self, arg1, arg2):
        if arg1.type()[1] != arg2.type()[0]:  # Type checking
            raise Exception(
                f'ERROR: Dagger type mismatch! Type 1 is:{arg1.type()} and Type 2 is:{arg2.type()}')
        else:
            self.argument1 = arg1
            self.argument2 = arg2

    def __str__(self) -> str:
        return f'({self.argument1}) † ({self.argument2})'

    def type(self) -> list:
        return [self.argument1.type()[0], self.argument2.type()[1]]

    def translate(self, arg1, arg2) -> ForAll:
        fresh_var = [var for var in ['x', 'y', 'z'] if var not in [arg1, arg2]]
        # Or self.argument2.type()[0] is also correct, they should be the same
        newset = self.argument1.type()[1]
        newvar = fresh_var.pop()
        return ForAll(Typed_Variable(newvar, newset),
                      make_OR(self.argument1.translate(arg1, newvar), self.argument2.translate(newvar, arg2)))

    def size(self) -> int:
        return 1 + self.argument1.size() + self.argument2.size()

    def object_representation(self, type1, type2) -> str:
        middle_type = self.argument1.type()[1]
        if isinstance(self.argument1, Typed_Relation):
            middle_type = f"{self.argument1.object_representation('left', 'right')}.type()[1]"
        elif isinstance(self.argument2, Typed_Relation):
            middle_type = middle_type = f"{self.argument2.object_representation('left', 'right')}.type()[0]"
        return f"Typed_COR_Expressions.Typed_Dagger({self.argument1.object_representation(type1, middle_type)}, {self.argument2.object_representation(middle_type, type2)})"


class Typed_Relation:
    """ This class represents a heterogeneous/typed relation on two sets: s1 and s2 """

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

    def size(self) -> int:
        return 1

    def object_representation(self, type1, type2) -> str:
        return self.letter


def make_typed_Composition(arg1, arg2):
    """ This helper function makes it easier to create simpler typed composition objects """
    if isinstance(arg1, Typed_IdentityRelation):
        return arg2
    elif isinstance(arg2, Typed_IdentityRelation):
        return arg1
    else:
        return Typed_Composition(arg1, arg2)


def make_typed_Union(arg1, arg2):
    """ This helper function makes it easier to create simpler typed union objects """
    if isinstance(arg1, Typed_EmptyRelation):
        return arg2
    elif isinstance(arg2, Typed_EmptyRelation):
        return arg1
    else:
        return Typed_Union(arg1, arg2)


def make_typed_Intersection(arg1, arg2):
    """ This helper function makes it easier to create simpler typed intersection objects """
    if isinstance(arg1, Typed_UniversalRelation):
        return arg2
    elif isinstance(arg2, Typed_UniversalRelation):
        return arg1
    else:
        return Typed_Intersection(arg1, arg2)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = Typed_Dagger(Typed_Relation(
        'A', 'Q', 'S'), Typed_Relation('B', 'S', 'R'))

    print("Original Expression:  ", test_expression)  # Original expression
    print("Translated Expression:", test_expression.translate(
        'x', 'y'))  # Translated expression
    print("Negation Normal Form: ", negation_normal(
        test_expression.translate('x', 'y')))  # Negation normal form
