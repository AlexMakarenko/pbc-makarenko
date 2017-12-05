

def get_pairs_of_numbers():
    lst = list(range(1, 10))
    result = set([tuple(sorted([x, 10-x])) for i in lst for x in lst if x+i == 10])
    return result, print(result)
