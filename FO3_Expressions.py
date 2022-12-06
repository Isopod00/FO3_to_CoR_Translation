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


class Negation:
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


class ForAll:
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


class ThereExists:
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


class AND:
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


class OR:
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


class Equals:
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


class tt:
    """ This class represents the literal boolean value True. """

    def _negate(self):
        return ff()

    def _negation_normal_form(self):
        return self

    def __str__(self):
        return "True"


class ff:
    """ This class represents the literal boolean value False. """

    def _negate(self):
        return tt()

    def _negation_normal_form(self):
        return self

    def __str__(self):
        return "False"


class Predicate:
    """ This class represents a single predicate denoted by the letter argument, with variables arg1 and arg2 """

    def __init__(self, letter, arg1, arg2):
        self.variable1 = arg1
        self.variabl2 = arg2
        self.letter = letter

    def __str__(self) -> str:
        return f'{self.letter}({self.variable1},{self.variabl2})'

    def _negate(self):
        return Negation(self)

    def _negation_normal_form(self):
        return self


def Implies(a, b) -> OR:
    """ Create a new OR object using the mathematical definition of implies -> """
    return OR(Negation(a), b)


def big_AND(terms, variable):
    """ This method computes the n-ary logical AND of n elements """
    answer = tt()
    for term in terms:
        modified_term = ff()
        for predicate in term:
            modified_term = make_OR(modified_term, predicate)
        answer = make_AND(answer, ForAll(variable, modified_term))
    return answer


def big_OR(terms, variable):
    """ This method computes the n-ary logical OR of n elements """
    answer = ff()
    for term in terms:
        modified_term = tt()
        for predicate in term:
            modified_term = make_AND(modified_term, predicate)
        answer = make_OR(answer, ThereExists(variable, modified_term))
    return answer


def T_dash(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_ForAll(expression.argument)
        return big_AND(terms, expression.variable)
    elif isinstance(expression, ThereExists):
        terms = T_ThereExists(expression.argument)
        return big_OR(terms, expression.variable)
    elif isinstance(expression, AND):
        return AND(T_dash(expression.argument1), T_dash(expression.argument2))
    elif isinstance(expression, OR):
        return OR(T_dash(expression.argument1), T_dash(expression.argument2))
    else:
        return expression


def T_ThereExists(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_ForAll(expression.argument)
        return {frozenset([big_AND(terms, expression.variable)])}
    elif isinstance(expression, ThereExists):
        terms = T_ThereExists(expression.argument)
        return {frozenset([big_OR(terms, expression.variable)])}
    elif isinstance(expression, AND):
        answer = set()
        for set1 in T_ThereExists(expression.argument1):
            for set2 in T_ThereExists(expression.argument2):
                answer.add(set1.union(set2))
        return answer
    elif isinstance(expression, OR):
        return T_ThereExists(expression.argument1).union(T_ThereExists(expression.argument2))
    else:
        return {frozenset([expression])}


def T_ForAll(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_ForAll(expression.argument)
        return {frozenset([big_AND(terms, expression.variable)])}
    elif isinstance(expression, ThereExists):
        terms = T_ThereExists(expression.argument)
        return {frozenset([big_OR(terms, expression.variable)])}
    elif isinstance(expression, AND):
        return T_ForAll(expression.argument1).union(T_ForAll(expression.argument2))
    elif isinstance(expression, OR):
        answer = set()
        for set1 in T_ForAll(expression.argument1):
            for set2 in T_ForAll(expression.argument2):
                answer.add(set1.union(set2))
        return answer
    else:
        return {frozenset([expression])}


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    expression = ForAll("x", ThereExists("y", ForAll("z", AND(Implies(Equals("y", "z"), Equals("x", "y")),
                                                              Predicate("R", "x", "y")))))
    print("Original Expression:", expression)  # Original expression
    print("\nNegation Normal Form:", expression._negation_normal_form())  # Negation Normal Form
    print("\nGood FO3 Test (Translated): ", T_dash(expression._negation_normal_form()))
