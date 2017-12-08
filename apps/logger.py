def log(func):
    def wrapper(*args):
        func_name = func.__name__
        list_of_args = []
        for a in args:
            list_of_args.append(a)
        rs = func(*args)
        print('\n{}({})'.format(func_name, str(list_of_args).strip('[]')))
        return rs

    return wrapper