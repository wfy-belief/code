import pytest


def ans(info):
    ones, zeros = {}, {}
    for key, value in info:
        # 如果key不存在
        if key not in ones:
            ones[key] = 0
            zeros[key] = 0
        # 分别记录及格和不及格的个数
        if value == 1:
            ones[key] += 1
        else:
            zeros[key] += 1
    out = []
    for key in sorted(ones.keys()):
        out.append((key, ones[key], zeros[key]))
    return out


@pytest.mark.parametrize(
    'info_in, info_out',
    [
        (
            [(0, 0), (1, 0), (1, 1), (3, 1), (5, 1), (7, 1)],
            [(0, 0, 1), (1, 1, 1), (3, 1, 0), (5, 1, 0), (7, 1, 0)]
        ),
        (
            [(0, 0), (1, 0), (1, 1), (3, 1), (5, 1), (7, 1)],
            [(0, 0, 1), (1, 1, 1), (3, 1, 0), (5, 1, 0), (7, 1, 0)]
        ),
        (
            [(0, 0), (1, 0), (1, 1), (3, 1), (5, 1), (7, 1)],
            [(0, 0, 1), (1, 1, 1), (3, 1, 0), (5, 1, 0), (7, 1, 0)]
        ),
        (
            [(0, 0), (1, 0), (1, 1), (3, 1), (5, 1), (7, 1)],
            [(0, 0, 1), (1, 1, 1), (3, 1, 0), (5, 1, 0), (7, 1, 0)]
        ),
        (
            [(0, 0), (1, 0), (1, 1), (3, 1), (5, 1), (7, 1)],
            [(0, 0, 1), (1, 1, 1), (3, 1, 0), (5, 1, 0), (7, 1, 0)]
        ),
        (
            [(0, 0), (1, 0), (1, 1), (3, 1), (5, 1), (7, 1)],
            [(0, 0, 1), (1, 1, 1), (3, 1, 0), (5, 1, 0), (7, 1, 0)]
        )
    ]
)
def test_ans(info_in, info_out):
    result = ans(info_in)
    assert info_out == result
