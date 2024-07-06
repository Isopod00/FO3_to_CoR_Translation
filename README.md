# FO3 to CoR Translation

This project aims to translate First-Order 3-variable (FO3) predicate logic into the Calculus of Relations (CoR).

Contributors: Anthony Brogni (brogn002@umn.edu) and Sebastiaan J. C. Joosten (sjoosten@umn.edu)

## This tool currently supports:

- Object representation of FO3 Expressions (including predicates with repeated arguments and formulas with typed arguments)

- Object representation of CoR Expressions (both homogeneous/untyped and heterogeneous/typed)

- Generation of random formulas and automated testing with the z3-solver Python library

- Discovery of simplification rules with the help of Z3

- Simplification of CoR formulas (both homogeneous/untyped and heterogeneous/typed)

## Installation Instructions

1. Clone this repository to your local machine:

```
git clone https://github.com/Isopod00/FO3_to_CoR_Translation.git
```

2. Once it is cloned, open this repository in your Python IDE of choice, and select a Python 3.11 interpreter as this project was written using Python 3.11.

3. Next, install all necessary dependencies. A requirements.txt file is included in this repository to make the dependency installation process smoother. The requirements.txt file lists all dependencies and the version used for each one. You can install them all simply by running this command:

```
pip3 install -r requirements.txt
```

4. Unfortunately, no user-friendly frontend has been developed for this tool yet, so for now you will need to interact with the code directly. Please refer to the main.py file for example usage. The "Summary of each File" section below describes what you can expect to find in each file of this project, and thus is also a useful resource. The examples in the included main.py file can be modified to suit the desired usage of the user.

## Summary of each File

- **FO3_Expressions.py**: Definitions of FO3 objects

- **COR_Expressions.py**: Definitions of CoR objects (homogeneous/untyped)

- **Typed_COR_Expressions.py**: Definitions of heterogeneous/typed CoR objects

- **FO3_Translation_Methods.py**: Methods for applying the Good, Nice, and Final translation steps

- **Typed_FO3_Translation.py**: Contains the modified Final translation step for heterogeneous/typed formulas

- **Testing.py**: Random formula generation and automated testing with the z-3 solver module

- **Typed_Testing.py**: A modified version of Testing.py for heterogeneous/typed formulas

- **Search_For_Simplification_Rules.py**: Code for finding all possible simplification rules of a given size

- **Generate_Typed_Rules.py**: Code for taking our dictionary of homogeneous rules and producing a dictionary of heterogeneous rules

- **Simplify.py**: Python code generated from the rules in **COR_Rules.txt** for simplifying homogeneous CoR expressions

- **Typed_Simplify.py**: Python code generated from the rules in **Typed_COR_Rules.txt** for simplifying heterogeneous CoR expressions

- **List_Methods.py**: Helper methods for treating lists as if they were sets
