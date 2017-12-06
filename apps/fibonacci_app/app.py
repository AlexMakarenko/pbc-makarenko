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
def get_fibonacci_sequence(n):
    a, b = 0, 1
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    print('Result: {}'.format(result))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app returns the fibonacci sequence of required length.")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--length", "-l", action='store', help="Needed length of fibonacci sequence.", type=int,
                       required=True)
    args = parser.parse_args()
    get_fibonacci_sequence(args.length)
