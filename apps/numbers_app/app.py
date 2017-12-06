# ./app.py
import argparse


def log(func):
    def wrapper(*args):
        for a in args:
            print('Input arg: "{}"'.format(a))
        rs = func(*args)
        print("Status: No errors")
        return rs

    return wrapper


@log
def get_pairs_of_numbers(n):
    if type(n) is int and n>0:
        lst = range(1, n)
        result = set([tuple(sorted([x, 10 - x])) for i in lst for x in lst if x + i == 10])
        print('Result: {}'.format(result))
        return result
    else:
        print('Input type must be int > 0.')
        return []


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app returns pairs of numbers where sum is ten.")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--length", "-l", action='store', help="Length of set of numbers.", type=int, required=True)
    args = parser.parse_args()
    get_pairs_of_numbers(args.length)
