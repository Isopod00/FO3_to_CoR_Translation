import sys
sys.path.append('src')

from src import Search_For_Simplification_Rules
from src.utils.FO3_Translation_Methods import *
from utils.Typed_FO3_Translation import *


def main_homogeneous(fo3_expression):
    # Translation Tool
    print("\nOriginal Expression: ", fo3_expression)  # Original expression
    nnf = negation_normal(fo3_expression)
    print("Negation Normal Form:", nnf)  # Negation Normal Form
    first_nice = T_Nice(nnf)
    print("Nice FO3 Translation:", first_nice)
    good = T_Good_Dash(first_nice)
    print("Good FO3 Translation:", good)  # Good FO3 Term
    nice = T_Nice(good)
    print("Nice FO3 Translation:", nice)  # Nice FO3 Term
    final = final_translation(nice, 'x', 'y')
    print("Final Translation:   ", final)
    # Simplification Tool
    simplified = Search_For_Simplification_Rules.fully_simplify(final)
    print("Simplified:          ", simplified)
    
    
def main_heterogeneous(typed_fo3_expression):
    # Translation Tool
    print("Original Expression:   ", typed_fo3_expression)  # Original expression
    nnf = negation_normal(typed_fo3_expression)
    print("Negation Normal Form:  ", nnf)  # Negation Normal Form
    first_nice = FO3_Translation_Methods.T_Nice(nnf)
    print("Nice FO3 Translation:  ", first_nice)
    good = FO3_Translation_Methods.T_Good_Dash(first_nice)
    print("Good FO3 Translation:  ", good)  # Good FO3 Term
    nice = FO3_Translation_Methods.T_Nice(good)
    print("Nice FO3 Translation:  ", nice)  # Nice FO3 Term
    final = typed_final_translation(nice, Typed_Variable('x', "Left"), Typed_Variable('y', "Right"))
    print("Final Translation:   ", final)
    # Simplification Tool
    simplified = Search_For_Simplification_Rules.fully_simplify(final, True)
    print("Simplified:          ", simplified, "\n")


if __name__ == "__main__":
    # fo3_expression must be a closed expression (no unbound variables)
    fo3_expression = ForAll("x", ForAll("y", ThereExists("z", AND(Negation(AND(Predicate("A", "x", "z"), Predicate("B", "z", "x"))), Predicate("C", "x", "y")))))
    main_homogeneous(fo3_expression)
    
    print() # New line
    
    x = Typed_Variable('x', 'A')
    y = Typed_Variable('y', 'B')
    z = Typed_Variable('z', 'B')

    # typed_fo3_expression must be a closed expression (no unbound variables)
    typed_fo3_expression = ForAll(x, ForAll(y, ThereExists(z, AND(Negation(AND(Predicate("A", x, z), Predicate("B", z, x))), Predicate("C", x, y)))))
    main_heterogeneous(typed_fo3_expression)
