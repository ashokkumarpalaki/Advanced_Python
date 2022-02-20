"""
implementing decorators in realtime manner
"""
import math


def customdecorator(foo):
    def inner(*args, **kwargs):
        print("from decorator")
        val = foo(*args, **kwargs)
        result = 0
        for i in args:
            if result < 0:
                result += i
            result -= i
        values = {"sqrt": math.sqrt(val),
                  "add": val,
                  "sub": result}
        return values

    return inner


@customdecorator
def display(*args, **kwargs):
    print("from function")
    val = 0
    for i in args:
        if isinstance(i, str):
            val = str(val)
        val += i
    return val


if __name__ == '__main__':
    print(display(10, 20))
