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

    def negate(self):
        return self.argument

    def negation_normal_form(self):
        return self.argument.negate()

    def __str__(self) -> str:
        return f'¬({self.argument})'

    def depends_on(self) -> set:
        return self.argument.depends_on()


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


class AND(Term):
    """This class describes a logical AND statement with two arguments, the arguments can be any logical expressions"""

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


class OR(Term):
    """This class describes a logical OR statement with two arguments, the arguments can be any logical expressions"""

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
        return self.argument1.depends_on().Union(self.argument2.depends_on())


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

    print("Original Expression:", test_expression)  # Original expression
    print("Negation Normal Form:", negation_normal(test_expression))  # Negation Normal Form
