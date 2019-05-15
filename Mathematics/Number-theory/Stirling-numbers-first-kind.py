'''
    Stirling number of first kind s(n, k) is the number of permutations of length n having exactly k cycles.
'''




#########################################################################

# Works modulo MOD
def Stirling(n, k, MOD):
    if k > n:
        return 0
    s = [[0 for _ in range(k+1)] for _ in range(n+1)]
    s[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            s[i][j] = ((i-1)*s[i-1][j] + s[i-1][j-1]) % MOD
    return s[n][k]

#########################################################################







'''    Verification test    '''
if __name__ == "__main__":
    MOD = 10**9+7
    assert Stirling(9, 5, MOD) == 22449
