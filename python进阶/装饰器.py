import functools


def outer(func):
    """
    装饰器
    """
    @functools.wraps(func)
    def inner():
        print(1)
        result = func()
        return result
    return inner


@outer
def test():
    """
    test->>>>
    >>>>>>>>>
    """
    print('test')


test()
print(test.__doc__)
