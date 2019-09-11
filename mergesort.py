"""

"""


def tst(a, b):
    infinite = 999999999999
    total_len = len(a) + len(b)
    c = [0] * total_len
    # merge from a to b
    # or merge from b to a
    a.append(infinite)
    b.append(infinite)
    i = 0
    j = 0
    k = 0
    while k < total_len:
        # who small move who, then next.
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
        else:
            c[k] = b[j]
            j += 1
        k += 1
    print(c)


def tst2():
    a = [0, 2, 4, 6]
    b = [1, 3, 5, 7]
    tst(a, b)


tst2()
