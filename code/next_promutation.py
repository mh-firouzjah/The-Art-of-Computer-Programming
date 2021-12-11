"""Algorithm L from Donald E. Knuth
کوچکترین بزرگترین ترکیب بعدی
پیاده‌سازی با حلقه‌ی وایل سرعت عمل ۱.۴ برابر بهتری نسبت به فور ارائه می‌دهد.
"""


from typing import Union


def next_promutation(lst: Union[list[int], list[str]]
                     ) -> Union[Union[list[int], list[str]], None]:
    """returns next promutation of a given list"""
    if not isinstance(lst, list):
        raise TypeError("The only required argument must be of type list")
    for cls in [str, int]:
        if isinstance(lst[0],
                      cls) and not all(isinstance(i, cls) for i in lst):
            raise TypeError(
                "The only required argument must be list of either int or str")

    pivot = -1
    while True:
        if lst[pivot] < lst[pivot - 1]:
            pivot -= 1
            if pivot == -len(lst):
                return
        else:
            break

    left, right = lst[:pivot], lst[pivot:]
    inx = -1
    while True:
        if right[inx] < left[-1]:
            inx -= 1
        else:
            left[-1], right[inx] = right[inx], left[-1]
            break
    right = sorted(right)
    return left + right


test: list[int] = [1, 2, 3]
while res := next_promutation(test):
    print(res)
    test = res
print(res)

# [1, 2, 3] -> {
#     [1, 3, 2]
#     [2, 1, 3]
#     [2, 3, 1]
#     [3, 1, 2]
#     [3, 2, 1]
# }

print('ab', ''.join(next_promutation(list('ab'))), 'ba')
print('bb', next_promutation(list('bb')) is None)
print('hefg', ''.join(next_promutation(list('hefg'))), 'hegf')
print('dhck', ''.join(next_promutation(list('dhck'))), 'dhkc')
print('dkhc', ''.join(next_promutation(list('dkhc'))), 'hcdk')
