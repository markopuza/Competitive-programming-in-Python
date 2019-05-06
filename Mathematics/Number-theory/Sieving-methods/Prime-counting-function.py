''' The prime counting function pi(n) = # of primes <= n '''

#########################################################################

def pi(n):
    ''' Returns two arrays pi1, pi2:
            pi1[i] = pi(i) for i <= sqrt(n)
            pi2[i] = pi(n // i) for i <= sqrt(n)
     '''
    lim = int(n**0.5)
    while lim*lim <= n: lim += 1
    lim -= 1

    pi1, pi2 = [0]*(lim + 1), [0]*(lim + 1)
    for i in range(1, lim + 1):
        pi1[i] = i - 1
        pi2[i] = n//i - 1

    for i in range(2, lim + 1):
        if pi1[i] == pi1[i - 1]:
            continue
        p = pi1[i - 1]
        for j in range(1, min(n // (i * i), lim) + 1):
            st = i * j
            if st <= lim:
                pi2[j] -= pi2[st] - p
            else:
                pi2[j] -= pi1[n // st] - p
        for j in range(lim, min(lim, i * i - 1), -1):
            pi1[j] -= pi1[j // i] - p
    return pi1, pi2

#########################################################################








'''    Verification test    '''
if __name__ == '__main__':
    from sympy.ntheory.generate import primepi
    n = 10**6
    pi1, pi2 = pi(n)
    for i in range(len(pi1)):
        assert pi1[i] == primepi(i)
    for i in range(1, len(pi2)):
        assert pi2[i] == primepi(n // i)


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
