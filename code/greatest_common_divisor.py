"""Euclid's Algorithm
پیدا کردن بزرگترین مقسوم علیه مشترک
"""
from typing import Union


def greatest_common_divisor(m: int, n: int) -> Union[int, None]:
    if not isinstance(m, int) or not isinstance(n, int):
        return
    if m < 0 or n <= 0:
        return
    if m == 0:
        return 0
    if m < n:
        # this if statement decreases running time in about one half of all
        # cases
        m, n = n, m
    while r := m % n:
        m, n = n, r
    return n

# def greatest_common_divisor(m: int, n: int) -> int:
#     """Recursive version"""
#     if m%n == 0:
#             return n
#     return greatest_common_divisor(n, r)


print(greatest_common_divisor(-12, 4))
print(greatest_common_divisor(13, -4))
print(greatest_common_divisor(13, 4.2))
print(greatest_common_divisor(119, 544))
print(greatest_common_divisor(True, True))
print(greatest_common_divisor(False, True))
print(greatest_common_divisor(True, False))
