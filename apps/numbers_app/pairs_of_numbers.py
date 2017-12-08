from apps.logger import log


@log
def get_pairs_of_numbers(*args):
    lst = [el for el in args if type(el) is int or type(el) is float]
    result = set([tuple(sorted([x, i])) for i in lst for x in lst if x + i == 10])
    return list(result)
