from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second


if __name__ == '__main__':
    result = divide(69, 3)
    print(result)