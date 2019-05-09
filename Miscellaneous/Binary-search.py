''' Selection of binary search algorithm variants. '''


#########################################################################


from bisect import bisect_left

def binary_search(a, x):
    ''' Returns index of element x in sorted array a if present, otherwise returns -1 '''
    pos = bisect_left(a, x)
    return (pos if pos != len(a) and a[pos] == x else -1)

def continuous_binary_search(f, value, l, r, eps=1e-9):
    ''' Finds f^(-1)(value) where f is an increasing function '''
    while abs(f((l+r)/2) - value) > eps:
        mid = (r + l)/2
        if f(mid) > value:
            r = mid
        else:
            l = mid
    return (l + r)/2



#########################################################################










'''    Verification test    '''
if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 4, 6, 7, 8, 9]
    for qry, ans in [(-1, -1), (0, -1), (1, 0), (2, 2), (3, 4), (5, -1), (9, 9), (10, -1)]:
        assert binary_search(a, qry) == ans

    # finding the root of a cubic function
    f = lambda x: (x - 500)**3 + 42
    root = continuous_binary_search(f, 0, -10**6, 10**6)
    print('Root =', root, 'f(root) =', f(root))
