from typing import List


def test(c: int, d: int) -> int:
    # 参数注解 和 函数注解
    return c + d


if __name__ == '__main__':
    # 参考 https://cuiqingcai.com/7071.html
    # 变量注解
    l: List[int] = [1, 2, 3]
    a: int = 1
    print(a)
    b: float = 2.3
    # 查看注解
    print(test.__annotations__)
