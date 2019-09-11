"""
insert sorting
"""
from utils import get_random_array


def tst(a):
    """
    increasing sort.
    :param a: array.
    :return: none
    """
    if not isinstance(a, list):
        raise Exception('ha ha')
    for i in range(1, len(a)):
        k = a[i]
        pre_index = i - 1
        while pre_index > -1 and a[pre_index] > k:
            # compare with before object. skip all bigger.
            a[pre_index+1] = a[pre_index]
            pre_index -= 1
        a[pre_index + 1] = k
    print(a)


def tst3():
    # from big to small.
    pass


def tst2():
    # a = [13, 889, 1, 2, 9, 7]
    a = get_random_array()
    print(a)
    tst(a)


def tst4():
    """
    Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in
    an .n C 1/-element array C . State the problem formally and write pseudocode for adding the two integers.
    :return:
    """


tst2()
