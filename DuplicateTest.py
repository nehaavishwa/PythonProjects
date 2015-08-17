__author__ = 'nehaavishwa'


def arrfunc(arr):
    a = len(arr)
    sum = 0
    sum2 = 0
    for i in range(0, a):
        sum = sum + arr[i]
    sum2 = ((a-1) * (a-2)) >> 1
    print(sum-sum2)

arrfunc([0, 2, 1, 2, 3])




