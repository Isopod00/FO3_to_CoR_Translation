# Author: Anthony Brogni
# Last Changed: January 2023

""" This file contains useful methods that allow lists to be manipulated like sets.
We use these methods to help determine the free variables of typed FO3 expressions 
since we are representing typed variables as objects, which are mutable and thus 
cannot be stored in a traditional Python set. """


def list_union(list1, list2) -> list:
    """ Computes the mathematical 'union' of two python lists """
    answer = list1.copy()
    for term in list2:
        if term not in list1:
            answer.append(term)
    return answer


def list_difference(list1, list2) -> list:
    """ Computes the mathematical 'difference' of two python lists """
    return [term for term in list1 if term not in list2]
