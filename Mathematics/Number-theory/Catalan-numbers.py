'''
    Calculates Catalan numbers (2n choose n) / (n+1)
'''




#########################################################################

def Catalan(n, MOD):
    # Assumes MOD prime
    f = 1
    for i in range(1, n+1):
        f = f*i % MOD
    res = pow(f, MOD-2, MOD) * pow(f*(n+1), MOD-2, MOD) % MOD
    for i in range(n+1, 2*n+1):
        f = f*i % MOD
    res *= f
    return res % MOD

#########################################################################






'''    Verification test    '''
if __name__ == "__main__":
    MOD = 10**9 + 7
    arr = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700]
    assert all(x%MOD == y%MOD for x, y in zip(arr, [Catalan(n, MOD) for n in range(len(arr))]))
