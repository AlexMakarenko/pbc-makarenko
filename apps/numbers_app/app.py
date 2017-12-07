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
def get_pairs_of_numbers(*args):
    lst = [el for el in args if type(el) is int or type(el) is float]
    result = set([tuple(sorted([x, i])) for i in lst for x in lst if x + i == 10])
    print('Result: {}'.format(result))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app returns pairs of numbers where sum is ten.")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--numbers", "-n", action='store', nargs='+', help="Enter numbers separated by a space.",
                       type=int,
                       required=True)
    args = parser.parse_args()
    get_pairs_of_numbers(*args.numbers)
