def add(a: int, b: int):
    return a + b


print(add(121, 129))


def func_func(n):
    def in_func_func(x):
        return n + x
    return in_func_func


new_func = func_func(100)
print(new_func(300))


def none_func():
    pass


print(none_func())
print(type(none_func()))


def optional_func(a, b, c=2):
    return a+b+c


print(optional_func(4, 4, 12))
print(optional_func(4, 4))
print(optional_func(b=4, a=4, c=22))


def array_func(*args):
    print(type(args))
    print(args)
    result = 0
    for x in args:
        result += x


print(array_func(12, 8, 10, 12, 8, 52, 12, 24, 12, 32))


def object_func(**kwargs):
    print(type(kwargs))
    print(kwargs)

    result = 0
    for x in kwargs.items():
        result += x[1]
    return result


print(object_func(a=2, b=40, test=12, hello=123))


def default_multiply(x):
    return x * 2


numbers = [12, 23, 12412, 1241, 12, 124124]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

words = ['sfs', "fsafs", "afssafafas"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)
