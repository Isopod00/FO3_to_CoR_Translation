# FO3_to_CoR_Translation
The goal of this project is to translate First-Order 3-variable (FO3) predicate logic into the Calculus of Relations (CoR).

Contributors: Anthony Brogni (brogn002@umn.edu), Sebastiaan J. C. Joosten (sjoosten@umn.edu)

## This tool currently supports:

-FO3 Expressions (including terms with repeated arguments and formulas with typed arguments)

-CoR Expressions (both homogeneous and heterogeneous)

-Automated testing with the z3-solver Python library

-Simplification of CoR formulas

 ## Summary of each File
 
 -FO3_Expressions.py : Definitions of FO3 objects
 
 -COR_Expressions.py : Definitions of CoR objects (homogeneous/untyped)
 
 -Typed_COR_Expressions.py : Definitions of heterogeneous/typed CoR objects
 
 -FO3_Translation_Methods.py : Methods for applying the Good, Nice, and Final translation steps
 
 -Typed_FO3_Translation.py : Contains the modified Final translation step for heterogeneous/typed formulas
 
 -Testing.py : Random formula generation and automated testing with the z-3 solver module
 
 -Typed_Testing.py : A modified version of Testing.py for heterogeneous/typed formulas
 
 -Search_For_Simplification_Rules.py : Code for finding all possible simplfication rules of a given size
 
 -Simplify.py : Python code generated from our simplification rules for simplifying CoR expressions
 
 -List_Methods.py : Helper methods for treating lists as if they were sets
