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


def _big_AND(ex):
    terms = _T("∀", ex.argument)
    answer = ""
    for term in terms:
        modified_term = ""
        for predicate in term:
            if modified_term == "":
                modified_term = predicate
            else:
                modified_term = OR(modified_term, predicate)

        if answer == "":
            answer = ForAll(ex.variable, modified_term)
        else:
            answer = AND(answer, ForAll(ex.variable, modified_term))
    return answer


def _big_OR(ex):
    terms = _T("∃", ex.argument)
    answer = ""
    for term in terms:
        modified_term = ""
        for predicate in term:
            if modified_term == "":
                modified_term = predicate
            else:
                modified_term = AND(modified_term, predicate)

        if answer == "":
            answer = ThereExists(ex.variable, modified_term)
        else:
            answer = OR(answer, ThereExists(ex.variable, modified_term))
    return answer


def _T(parameter, expression):
    if parameter == "-":
        if isinstance(expression, ForAll):
            return _big_AND(expression)
        elif isinstance(expression, ThereExists):
            return _big_OR(expression)
        elif isinstance(expression, AND):
            return AND(_T("-", expression.argument1), _T("-", expression.argument2))
        elif isinstance(expression, OR):
            return OR(_T("-", expression.argument1), _T("-", expression.argument2))
        else:
            return expression
    elif parameter == "∃":
        if isinstance(expression, ForAll):
            return {frozenset(_big_AND(expression))}
        elif isinstance(expression, ThereExists):
            return {frozenset(_big_OR(expression))}
        elif isinstance(expression, AND):
            answer = set()
            for set1 in _T("∃", expression.argument1):
                for set2 in _T("∃", expression.argument2):
                    answer.add(set1.union(set2))
            return answer
        elif isinstance(expression, OR):
            return _T("∃", expression.argument1).union(_T("∃", expression.argument2))
        else:
            return {frozenset([expression])}
    elif parameter == "∀":
        if isinstance(expression, ForAll):
            return {frozenset(_big_AND(expression))}
        elif isinstance(expression, ThereExists):
            return {frozenset(_big_OR(expression))}
        elif isinstance(expression, AND):
            return _T("∀", expression.argument1).union(_T("∀", expression.argument2))
        elif isinstance(expression, OR):
            answer = set()
            for set1 in _T("∀", expression.argument1):
                for set2 in _T("∀", expression.argument2):
                    answer.add(set1.union(set2))
            return answer
        else:
            return {frozenset([expression])}
    else:
        print("ERROR: Unsupported Parameter!")
        return


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    expression = Negation(ForAll("x", ThereExists("y", OR(Equals("x", "-y"), Equals("x", "0")))))
    print("Original Expression:", expression)  # Original expression
    print("Negated Expression:", expression._negate())  # Negated expression
    print("Negation Normal Form:", expression._negation_normal_form())  # Negation Normal Form

    expression2 = ThereExists("z", AND(OR(Predicate("A", "x", "z"), Predicate("B", "z", "x")), Predicate("C", "x", "y")))
    print()
    print("Good FO3 Test (Original): ", expression2)
    print("Good FO3 Test (Translated): ", _T("-", expression2))
