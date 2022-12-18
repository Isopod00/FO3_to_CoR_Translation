# Authors: Sebastiaan Joosten, Anthony Brogni

class Term:
    """ This is a super class that other classes can inherit from. """

    def getAsAndList(self):
        return [self]

    def getAsOrList(self):
        return [self]


class Negation(Term):
    """ This class describes the mathematical symbol ¬ (not/negation)
    The argument for this class can be any logical expression that the negation should be applied to. """

    def __init__(self, arg):
        self.argument = arg

    def _negate(self):
        return self.argument

    def _negation_normal_form(self):
        return self.argument._negate()

    def __str__(self) -> str:
        return f'¬({self.argument})'

    def _depends_on(self):
        return self.argument._depends_on()


class ForAll(Term):
    """ This class describes the mathematical symbol ∀ (for all)
         The two arguments (var and arg) describe the variable in question and
         the expression that ∀var is being applied to, respectively. """

    def __init__(self, var, arg):
        self.variable = var
        self.argument = arg

    def _negate(self):
        return ThereExists(self.variable, self.argument._negate())

    def _negation_normal_form(self):
        return ForAll(self.variable, self.argument._negation_normal_form())

    def __str__(self) -> str:
        return f'∀{self.variable}. {self.argument}'

    def _depends_on(self):
        return self.argument._depends_on()


class ThereExists(Term):
    """ This class describes the mathematical symbol ∃ (there exists)
     The two arguments (var and arg) describe the variable in question and
     the expression that ∃var is being applied to, respectively. """

    def __init__(self, var, arg):
        self.variable = var
        self.argument = arg

    def _negate(self):
        return ForAll(self.variable, self.argument._negate())

    def _negation_normal_form(self):
        return ThereExists(self.variable, self.argument._negation_normal_form())

    def __str__(self) -> str:
        return f'∃{self.variable}. {self.argument}'

    def _depends_on(self):
        return self.argument._depends_on()


class AND(Term):
    """This class describes a logical AND statement with two arguments, the arguments can be any logical expressions"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def _negate(self):
        return OR(self.argument1._negate(), self.argument2._negate())

    def _negation_normal_form(self):
        return AND(self.argument1._negation_normal_form(), self.argument2._negation_normal_form())

    def __str__(self) -> str:
        return f'({self.argument1}) ∧ ({self.argument2})'

    def getAsAndList(self):
        lhs = self.argument1.getAsAndList()
        rhs = self.argument2.getAsAndList()
        return lhs + rhs

    def _depends_on(self):
        return self.argument1._depends_on() + self.argument2._depends_on()


class OR(Term):
    """This class describes a logical OR statement with two arguments, the arguments can be any logical expressions"""

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def _negate(self):
        return AND(self.argument1._negate(), self.argument2._negate())

    def _negation_normal_form(self):
        return OR(self.argument1._negation_normal_form(), self.argument2._negation_normal_form())

    def __str__(self) -> str:
        return f'({self.argument1}) ∨ ({self.argument2})'

    def getAsOrList(self):
        lhs = self.argument1.getAsOrList()
        rhs = self.argument2.getAsOrList()
        return lhs + rhs

    def _depends_on(self):
        return self.argument1._depends_on() + self.argument2._depends_on()


class Equals(Term):
    """ This class describes two arguments being equal to each other.
    The two arguments (arg1 and arg2) should be strings """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def _negate(self):
        return Negation(self)

    def _negation_normal_form(self):
        return self

    def __str__(self) -> str:
        return f'{self.argument1} = {self.argument2}'

    def _depends_on(self):
        return self.argument1 + self.argument2


class tt(Term):
    """ This class represents the literal boolean value True. """

    def _negate(self):
        return ff()

    def _negation_normal_form(self):
        return self

    def __str__(self):
        return "True"

    def getAsAndList(self):
        return []

    def _depends_on(self):
        return ""


class ff(Term):
    """ This class represents the literal boolean value False. """

    def _negate(self):
        return tt()

    def _negation_normal_form(self):
        return self

    def __str__(self):
        return "False"

    def getAsOrList(self):
        return []

    def _depends_on(self):
        return ""


class Predicate(Term):
    """ This class represents a single predicate denoted by the letter argument, with variables arg1 and arg2 """

    def __init__(self, letter, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2
        self.letter = letter

    def __str__(self) -> str:
        return f'{self.letter}({self.argument1},{self.argument2})'

    def _negate(self):
        return Negation(self)

    def _negation_normal_form(self):
        return self

    def _depends_on(self):
        return self.argument1 + self.argument2


def Implies(a, b) -> OR:
    """ Create a new OR object using the mathematical definition of implies -> """
    return OR(Negation(a), b)


def make_OR(arg1, arg2):
    """ This method helps improve/simplify the construction of OR objects """
    if isinstance(arg1, ff):
        return arg2
    elif isinstance(arg2, ff):
        return arg1
    else:
        return OR(arg1, arg2)


def make_AND(arg1, arg2):
    """ This method helps improve/simplify the construction of AND objects """
    if isinstance(arg1, tt):
        return arg2
    elif isinstance(arg2, tt):
        return arg1
    else:
        return AND(arg1, arg2)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = Negation(ThereExists('x', AND(Predicate("A", "x", "y"), AND(Equals('y', 'z'), Predicate('B', 'y', 'z')))))

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", test_expression._negation_normal_form())  # Negation Normal Form
