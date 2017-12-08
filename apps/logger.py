def log(func):
    def wrapper(*args):
        list_of_args = []
        for a in args:
            list_of_args.append(a)
        rs = func(*args)
        print('\n{}({})'.format(func.__name__, str(list_of_args).strip('[]')))
        return rs

    return wrapper
