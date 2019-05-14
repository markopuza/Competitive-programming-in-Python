'''
    Finds longest increasing subsequence in O(n log n) time.
'''


#########################################################################

def lis(a):
    p, m, l = [0]*len(a), [0]*(len(a) + 1), 0
    for i in range(len(a)):
       lo, hi = 1, l
       while lo <= hi:
           mid = (lo + hi)//2
           if a[m[mid]] < a[i]:
               lo = mid+1
           else:
               hi = mid-1
       p[i], m[lo] = m[lo-1], i
       if lo > l:
           l = lo
    s, k = [], m[l]
    for i in range(l-1, -1, -1):
        s.append(a[k])
        k = p[k]
    return s[::-1]

#########################################################################






'''    Verification test    '''
if __name__ == "__main__":
    for a in [[-1,2,-3,4,-5,5], [-1,-2,-3], [], [0], [2, -2, 1, 2, -1, 3, -1, -1, -1]]:
        print('{:s} has longest increasing sequence {:s}.'.format(str(a), str(lis(a))))
