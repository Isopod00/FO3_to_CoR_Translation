class Negation:
    """ This class describes the mathematical symbol ¬
    The argument for this class can be any logical expression that the negation should be applied to"""

    def __init__(self, arg):
        self.argument = arg

    def _negate_(self):
        return self.argument

    def _negation_normal_form_(self):
        return self.argument._negate_()

    def __str__(self):
        return f'¬({str(self.argument)})'


class ForAll:
    """ This class describes the mathematical symbol ∀.
         The two arguments (var and arg) describe the variable in question and
         the expression that ∀var is being applied to, respectively."""

    def __init__(self, var, arg):
        self.variable = var
        self.argument = arg

    def _negate_(self):
        return ThereExists(self.variable, self.argument._negate_())

    def _negation_normal_form_(self):
        return ForAll(self.variable, self.argument._negation_normal_form())

    def __str__(self):
        return f'∀{self.variable}. {str(self.argument)}'


class ThereExists:
    """ This class describes the mathematical symbol ∃.
     The two arguments (var and arg) describe the variable in question and
     the expression that ∃var is being applied to, respectively."""

    def __init__(self, var, arg):
        self.variable = var
        self.argument = arg

    def _negate_(self):
        return ForAll(self.variable, self.argument._negate_())

    def _negation_normal_form_(self):
        pass
        # TODO

    def __str__(self):
        return f'∃{self.variable}. {str(self.argument)}'


class AND:
    """ This class describes a logical AND statement with two arguments, the arguments can be any logical expression """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def _negate_(self):
        return OR(self.argument1._negate_(), self.argument2._negate_())

    def __str__(self):
        return f'({self.argument1}) \/ ({self.argument2})'


class OR:
    """ This class describes a logical OR statement with two arguments, the arguments can be any logical expression """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def _negate_(self):
        return AND(self.argument1._negate_(), self.argument2._negate_())

    def __str__(self):
        return f'({self.argument1}) /\ ({self.argument2})'

class Equals:
    """ This class describes two arguments being equal to each other.
    The two arguments (arg1 and arg2) should be strings """

    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def _negate_(self):
        return Negation(self)


# This code only runs if this file is run directly (it doesn't run when imported as a library)
if __name__ == "__main__":
    expression = Negation(ForAll("x", AND(Equals("x", "x"), Equals("x", "x"))))
    expression._negation_normal_form_()
