"""
insert sorting
"""



def tst(a):
    """

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


def tst2():
    a = [13, 889, 1, 2, 9, 7]
    tst(a)


tst2()
