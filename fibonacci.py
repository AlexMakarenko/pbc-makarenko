

def fibonacci_sequence(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result, print(result)

