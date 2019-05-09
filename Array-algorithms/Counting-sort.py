'''
    Count sort. Outperforms the default sorting routine when the range of values is reasonably bounded.

'''

#########################################################################

def count_sort(a):
    mn, mx = float('inf'), -float('inf')
    for x in a:
        if x < mn: mn = x
        if x > mx: mx = x
    counter = [0 for _ in range(mx - mn + 1)]
    for x in a:
        counter[x - mn] += 1
    j = 0
    for i in range(mx - mn + 1):
        a[j:j+counter[i]] = [i + mn]*counter[i]
        j += counter[i]


#########################################################################








'''    Verification test    '''
if __name__ == "__main__":
    from random import randint
    from time import clock
    a = [randint(10**4, 10**4 + 10**5) for _ in range(10**6)]
    aa = list(a)
    start = clock(); count_sort(a); print('Count sort:', clock() - start)
    start = clock(); aa.sort(); print('Default sort:', clock() - start)
    assert a == aa

    a = [randint(-10**6, 10**6) for _ in range(10**7)]
    aa = list(a)
    start = clock(); count_sort(a); print('Count sort:', clock() - start)
    start = clock(); aa.sort(); print('Default sort:', clock() - start)
    assert a == aa
