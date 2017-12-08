# ./app.py
import argparse
from apps import get_fibonacci_sequence
from apps import get_pairs_of_numbers

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app returns the fibonacci sequence of required length.",
                                     prog="PROG")
    group = parser.add_argument_group("Parameters")
    parser.add_argument('-a', '--app', type=str, required=True, help='App to run: fib or pairs')
    group.add_argument("--length", "-l", action='store', help="Needed length of fibonacci sequence.", type=int,
                       required=False)
    group.add_argument("--numbers", "-n", action='store', nargs='+', help="Numbers separated by a space.", type=int,
                       required=False)
    args = parser.parse_args()
    if args.app == 'fib':
        print(get_fibonacci_sequence(args.length))
    elif args.app == 'pairs':
        print(str(get_pairs_of_numbers(*args.numbers)).strip('[]'))
