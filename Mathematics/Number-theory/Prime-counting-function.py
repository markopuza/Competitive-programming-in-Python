''' The prime counting function pi(n) = # of primes <= n '''

#########################################################################

def pi(n):
    ''' Returns two arrays arr1, arr2:
            arr1[i] = pi(i) for i <= sqrt(n)
            arr2[i] = pi(n // i) for i <= sqrt(n)
     '''
    lim = int(n**0.5)
    while lim*lim <= n: lim += 1
    lim -= 1

    arr1, arr2 = [0]*(lim + 1), [0]*(lim + 1)
    for i in range(1, lim + 1):
        arr1[i] = i - 1
        arr2[i] = n//i - 1

    for i in range(2, lim + 1):
        if arr1[i] == arr1[i - 1]:
            continue
        p = arr1[i - 1]
        for j in range(1, min(n // (i * i), lim) + 1):
            st = i * j
            if st <= lim:
                arr2[j] -= arr2[st] - p
            else:
                arr2[j] -= arr1[n // st] - p
        for j in range(lim, min(lim, i * i - 1), -1):
            arr1[j] -= arr1[j // i] - p
    return arr1, arr2

#########################################################################








'''    Verification test    '''
if __name__ == '__main__':
    from sympy.ntheory.generate import primepi
    n = 10**6
    arr1, arr2 = pi(n)
    for i in range(len(arr1)):
        assert arr1[i] == primepi(i)
    for i in range(1, len(arr2)):
        assert arr2[i] == primepi(n // i)


'''
Approximate runtime (Computing pi(n)):
_______________________________________________
        n              time
       100             3e-5s
      10**4            0.0002s
      10**6            0.007s
      10**8            0.2s
      10**10           5.4s
'''
