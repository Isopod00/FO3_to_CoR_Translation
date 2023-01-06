def list_union(list1, list2):
    """ Computes the mathematical 'union' of two python lists """
    answer = list1.copy()
    for term in list2:
        if term not in list1:
            answer.append(term)
    return answer


def list_difference(list1, list2):
    """ Computes the mathematically 'difference' of two python lists """
    return [term for term in list1 if term not in list2]
