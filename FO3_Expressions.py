# Authors: Sebastiaan J. C. Joosten, Anthony Brogni
# Last Changed: March 2023
""" This file contains everything you need to build mathematical FO3 objects in Python, even typed FO3 objects! """
from List_Methods import *


class Term:
    """ This is a super class that other FO3 expression classes inherit from. """

    def getAsAndList(self):
        return [self]

    def getAsOrList(self):
        return [self]


class Typed_Variable:
    """ This class represents a typed variable from a specific set. """

    def __init__(self, v, s):
        self.var = v
        self.set = s

    def __str__(self) -> str:
        return f'{self.var} ∈ {self.set}'

    def __eq__(self, other):
        """ Define what it means for two Typed_Variables to be 'equal' """
        return isinstance(other, Typed_Variable) and self.var == other.var and self.set == other.set


class Negation(Term):
    """ This class describes the mathematical symbol ¬ (not/negation)
    The argument for this class can be any logical expression that the negation should be applied to. """

    def __init__(self, arg):
        self.argument = arg

    def negate(self):
        return self.argument

    def negation_normal_form(self):
        return self.argument.negate()

    def __str__(self) -> str:
        return f'¬({self.argument})'

    def depends_on(self) -> set:
        return self.argument.depends_on()

    def free_variables(self) -> list:
        return self.argument.free_variables()


class ForAll(Term):
    """ This class describes the mathematical symbol ∀ (for all)
         The two arguments (var and arg) describe the variable in question and
         the expression that ∀var is being applied to, respectively. """

    def __init__(self, var, arg):
        self.variable = var
        self.argument = arg

    def negate(self):
        return ThereExists(self.variable, self.argument.negate())

    def negation_normal_form(self):
        return ForAll(self.variable, self.argument.negation_normal_form())

    def __str__(self) -> str:
        return f'∀{self.variable}. {self.argument}'

    def depends_on(self) -> set:
        return self.argument.depends_on()

    def free_variables(self) -> list:
        return list_difference(self.argument.free_variables(), [self.variable])


class ThereExists(Term):
    """ This class describes the mathematical symbol ∃ (there exists)
     The two arguments (var and arg) describe the variable in question and
     the expression that ∃var is being applied to, respectively. """

    def __init__(self, var, arg):
        self.variable = var
        self.argument = arg

    def negate(self):
        return ForAll(self.variable, self.argument.negate())

    def negation_normal_form(self):
        return ThereExists(self.variable, self.argument.negation_normal_form())

    def __str__(self) -> str:
        return f'∃{self.variable}. {self.argument}'

    def depends_on(self) -> set:
        return self.argument.depends_on()

    def free_variables(self) -> list:
        return list_difference(self.argument.free_variables(), [self.variable])


class AND(Term):
    """ This class describes a logical AND statement with two arguments, the arguments can be any logical expressions"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def negate(self):
        return OR(self.argument1.negate(), self.argument2.negate())

    def negation_normal_form(self):
        return AND(self.argument1.negation_normal_form(), self.argument2.negation_normal_form())

    def __str__(self) -> str:
        return f'({self.argument1}) ∧ ({self.argument2})'

    def getAsAndList(self):
        lhs = self.argument1.getAsAndList()
        rhs = self.argument2.getAsAndList()
        return lhs + rhs

    def depends_on(self) -> set:
        return self.argument1.depends_on().union(self.argument2.depends_on())

    def free_variables(self) -> list:
        return list_union(self.argument1.free_variables(), self.argument2.free_variables())


class OR(Term):
    """ This class describes a logical OR statement with two arguments, the arguments can be any logical expressions"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def negate(self):
        return AND(self.argument1.negate(), self.argument2.negate())

    def negation_normal_form(self):
        return OR(self.argument1.negation_normal_form(), self.argument2.negation_normal_form())

    def __str__(self) -> str:
        return f'({self.argument1}) ∨ ({self.argument2})'

    def getAsOrList(self):
        lhs = self.argument1.getAsOrList()
        rhs = self.argument2.getAsOrList()
        return lhs + rhs

    def depends_on(self) -> set:
        return self.argument1.depends_on().union(self.argument2.depends_on())

    def free_variables(self) -> list:
        return list_union(self.argument1.free_variables(), self.argument2.free_variables())


class Equals(Term):
    """ This class describes two arguments being equal to each other.
    The two arguments (arg1 and arg2) should be strings """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def negate(self):
        return Negation(self)

    def negation_normal_form(self):
        return self

    def __str__(self) -> str:
        return f'{self.argument1} = {self.argument2}'

    def depends_on(self) -> set:
        return {self.argument1, self.argument2}

    def free_variables(self) -> list:
        return [self.argument1, self.argument2] if self.argument1 != self.argument2 else [self.argument1]


class tt(Term):
    """ This class represents the literal boolean value True. """

    def negate(self):
        return ff()

    def negation_normal_form(self):
        return self

    def __str__(self):
        return "True"

    def getAsAndList(self):
        return []

    def depends_on(self) -> set:
        return set()

    def free_variables(self) -> list:
        return []


class ff(Term):
    """ This class represents the literal boolean value False. """

    def negate(self):
        return tt()

    def negation_normal_form(self):
        return self

    def __str__(self):
        return "False"

    def getAsOrList(self):
        return []

    def depends_on(self) -> set:
        return set()

    def free_variables(self) -> list:
        return []


class Predicate(Term):
    """ This class represents a single predicate denoted by the letter argument, with variables arg1 and arg2 """

    def __init__(self, letter, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2
        self.letter = letter

    def __str__(self) -> str:
        return f'{self.letter}({self.argument1},{self.argument2})'

    def negate(self):
        return Negation(self)

    def negation_normal_form(self):
        return self

    def depends_on(self) -> set:
        return {self.argument1, self.argument2}

    def free_variables(self) -> list:
        return [self.argument1, self.argument2] if self.argument1 != self.argument2 else [self.argument1]


def Implies(a, b) -> OR:
    """ Create a new OR object using the mathematical definition of implies -> """
    return OR(Negation(a), b)


def make_OR(arg1, arg2):
    """ This method helps improve/simplify the construction of mathematical OR objects """
    if isinstance(arg1, ff):
        return arg2
    elif isinstance(arg2, ff):
        return arg1
    else:
        return OR(arg1, arg2)


def make_AND(arg1, arg2):
    """ This method helps improve/simplify the construction of mathematical AND objects """
    if isinstance(arg1, tt):
        return arg2
    elif isinstance(arg2, tt):
        return arg1
    else:
        return AND(arg1, arg2)


def make_ThereExists(variable, argument):
    """ This method helps improve/simplify the creation of mathematical ThereExists objects """
    match argument:
        case tt() | ff():
            return argument
        case _:
            return ThereExists(variable, argument)


def make_ForAll(variable, argument):
    """ This method helps improve/simplify the creation of mathematical ForAll objects """
    match argument:
        case tt() | ff():
            return argument
        case _:
            return ForAll(variable, argument)


def negation_normal(argument):
    """ The reason for this method is that I discovered a bug in which some expressions need multiple iterations to be
     put into negation normal form correctly. """
    previous_iteration = argument
    argument = argument.negation_normal_form()
    while str(previous_iteration) != str(argument):
        previous_iteration = argument
        argument = argument.negation_normal_form()
    return argument


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = Negation(
        ThereExists('x', Negation(
            ThereExists('y', Negation(
                AND(Predicate("A", "x", "y"), AND(Equals('y', 'z'), Predicate('B', 'y', 'z'))))))))

    print("Original Expression: ", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form

    print()
    x = Typed_Variable('x', 'Q')
    y = Typed_Variable('y', 'R')
    z = Typed_Variable('z', 'S')
    test_expression = Negation(
        ThereExists(x, Negation(
            ThereExists(y, Negation(
                AND(Predicate("A", x, y), AND(Equals(y, z), Predicate('B', y, z))))))))

    print("Original Expression: ", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form
