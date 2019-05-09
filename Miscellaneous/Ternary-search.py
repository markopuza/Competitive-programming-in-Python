'''
    Selection of ternary search algorithm variants.

    Ternary search finds maximum of unimodal lists/functions in log time.
'''


#########################################################################

def ternary_search(a):
    # Finds maximum of unimodal array. For minimum, reverse comparison
    l, r = 0, len(a)
    while r > l + 2:
        lmid, rmid = l + (r - l) // 3, r - (r - l) // 3
        if a[lmid] < a[rmid]:
            l = lmid
        else:
            r = rmid
    return max([(a[i], i) for i in range(l, r+1)])[1]


def continuous_ternary_search(f, l, r, eps=1e-9):
    # Finds maximum. For minimum, reverse comparison
    while r - l > eps:
        lmid, rmid = l + (r - l) / 3, r - (r - l) / 3
        if f(lmid) < f(rmid):
            l = lmid
        else:
            r = rmid
    return (l + r)/2


#########################################################################




'''    Verification test    '''
if __name__ == '__main__':
    # finding maximum of a quadtratic function
    f = lambda x: -(x - 42)**2 + 65
    v = continuous_ternary_search(f, -10**6, 10**6)
    print('Maximum of function is at', v, ' with value ', f(v))

    a = [1, 1, 2, 2, 3, 4, 6, 7, 8, 122, 8, 6, 6, 5, 3, 2, 1, 1] + [0]*10**5
    assert ternary_search(a) == 9
