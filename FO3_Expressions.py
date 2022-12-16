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


class Term:
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


def Implies(a, b) -> OR:
    """ Create a new OR object using the mathematical definition of implies -> """
    return OR(Negation(a), b)


def big_AND(terms, variable):
    """ This method helps compute the n-ary logical AND of n elements for the GOOD translation """
    answer = tt()
    for term in terms:
        modified_term = ff()
        for predicate in term:
            modified_term = make_OR(modified_term, predicate)
        answer = make_AND(answer, ForAll(variable, modified_term))
    return answer


def big_OR(terms, variable):
    """ This method helps compute the n-ary logical OR of n elements for the GOOD translation """
    answer = ff()
    for term in terms:
        modified_term = tt()
        for predicate in term:
            modified_term = make_AND(modified_term, predicate)
        answer = make_OR(answer, ThereExists(variable, modified_term))
    return answer


def T_Good_Dash(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_Good_ForAll(expression.argument)
        return big_AND(terms, expression.variable)
    elif isinstance(expression, ThereExists):
        terms = T_Good_ThereExists(expression.argument)
        return big_OR(terms, expression.variable)
    elif isinstance(expression, AND):
        return AND(T_Good_Dash(expression.argument1), T_Good_Dash(expression.argument2))
    elif isinstance(expression, OR):
        return OR(T_Good_Dash(expression.argument1), T_Good_Dash(expression.argument2))
    else:
        return expression


def T_Good_ThereExists(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_Good_ForAll(expression.argument)
        return {frozenset([big_AND(terms, expression.variable)])}
    elif isinstance(expression, ThereExists):
        terms = T_Good_ThereExists(expression.argument)
        return {frozenset([big_OR(terms, expression.variable)])}
    elif isinstance(expression, AND):
        answer = set()
        for set1 in T_Good_ThereExists(expression.argument1):
            for set2 in T_Good_ThereExists(expression.argument2):
                answer.add(set1.union(set2))
        return answer
    elif isinstance(expression, OR):
        return T_Good_ThereExists(expression.argument1).union(T_Good_ThereExists(expression.argument2))
    else:
        return {frozenset([expression])}


def T_Good_ForAll(expression):
    """ Translation function for translating FO3 terms in negation normal form into "good" FO3 terms """
    if isinstance(expression, ForAll):
        terms = T_Good_ForAll(expression.argument)
        return {frozenset([big_AND(terms, expression.variable)])}
    elif isinstance(expression, ThereExists):
        terms = T_Good_ThereExists(expression.argument)
        return {frozenset([big_OR(terms, expression.variable)])}
    elif isinstance(expression, AND):
        return T_Good_ForAll(expression.argument1).union(T_Good_ForAll(expression.argument2))
    elif isinstance(expression, OR):
        answer = set()
        for set1 in T_Good_ForAll(expression.argument1):
            for set2 in T_Good_ForAll(expression.argument2):
                answer.add(set1.union(set2))
        return answer
    else:
        return {frozenset([expression])}


def T_Nice(expression):
    """ Translation function for translating "good" FO3 terms into "nice" FO3 terms """
    if isinstance(expression, OR):
        return OR(T_Nice(expression.argument1), T_Nice(expression.argument2))
    elif isinstance(expression, AND):
        return AND(T_Nice(expression.argument1), T_Nice(expression.argument2))
    elif isinstance(expression, ThereExists):
        terms = expression.argument.getAsAndList()
        var = expression.variable

        lhs_list = []  # does NOT depend on the variable
        rhs_list = []  # DOES depend on the variable

        for term in terms:
            if isinstance(term, ForAll) or isinstance(term, ThereExists):
                if term.variable == var:
                    rhs_list.append(term)
                else:
                    lhs_list.append(term)
            else:
                if term.argument1 == var or term.argument2 == var:
                    rhs_list.append(term)
                else:
                    lhs_list.append(term)

        lhs = n_ary_AND(lhs_list)
        rhs = ThereExists(var, n_ary_AND(rhs_list))

        return AND(lhs, rhs)
    elif isinstance(expression, ForAll):
        terms = expression.argument.getAsOrList()
        var = expression.variable

        lhs_list = []  # does NOT depend on the variable
        rhs_list = []  # DOES depend on the variable
        for term in terms:
            if isinstance(term, ForAll) or isinstance(term, ThereExists):
                if term.variable == var:
                    rhs_list.append(term)
                else:
                    lhs_list.append(term)
            else:
                if term.argument1 == var or term.argument2 == var:
                    rhs_list.append(term)
                else:
                    lhs_list.append(term)

        if len(lhs_list) > 0 and len(rhs_list) > 0:
            lhs = T_Nice(n_ary_OR(lhs_list))
            rhs = ForAll(var, T_Nice(n_ary_OR(rhs_list)))
            return OR(lhs, rhs)
        elif len(rhs_list) > 0:
            rhs = ForAll(var, T_Nice(n_ary_OR(rhs_list)))
            return rhs
        elif len(lhs_list) > 0:
            lhs = T_Nice(n_ary_OR(lhs_list))
            return lhs
    else:
        return expression


def n_ary_AND(expressions_list):
    answer = tt()
    for term in expressions_list:
        answer = make_AND(answer, term)
    return answer


def n_ary_OR(expressions_list):
    answer = ff()
    for term in expressions_list:
        answer = make_OR(answer, term)
    return answer


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    test_expression = ForAll('x', AND(Predicate("A", "x", "y"), AND(Equals('y', 'z'), Predicate('B', 'y', 'z'))))

    print("Original Expression:", test_expression)  # Original expression
    print("\nNegation Normal Form:", test_expression._negation_normal_form())  # Negation Normal Form
    print("\nGood FO3 Translation: ", T_Good_Dash(test_expression._negation_normal_form()))  # Good FO3 Term
    print("\nNice FO3 Translation: ", T_Nice(T_Good_Dash(test_expression._negation_normal_form())))  # Nice FO3 Term
