'''
    Stirling number of second kind S(n, k) is the number of ways to partition a set of n objects into k non-empty subsets.
'''




#########################################################################

# Works modulo MOD, takes fact (n! % MOD) and factinv (n!^(-1) % MOD) as input
def Stirling(n, k, fact, factinv, MOD):
    if k > n:
        return 0
    result = 0
    for j in range(k+1):
        result += (-1 if (k-j)&1 else 1) * fact[k] * factinv[j] * factinv[k-j] * pow(j, n, MOD) % MOD
        result %= MOD
    result *= factinv[k]
    return result % MOD


#########################################################################







def fast_modinv(up_to, M):
    ''' Fast modular inverses of 1..up_to   modulo M. '''
    modinv = [-1 for _ in range(up_to + 1)]
    modinv[1] = 1
    for x in range(2, up_to + 1):
        modinv[x] = (-(M//x) * modinv[M%x])%M
    return modinv

'''    Verification test    '''
if __name__ == "__main__":
    MOD = 10**9+7
    maxn = 100
    modinv = fast_modinv(maxn, MOD)
    fact, factinv = [1], [1]
    for i in range(1, maxn):
        fact.append(fact[-1]*i % MOD)
        factinv.append(factinv[-1]*modinv[i] % MOD)

    assert Stirling(10, 3, fact, factinv, MOD) == 9330 % MOD
    assert Stirling(10, 5, fact, factinv, MOD) == 42525 % MOD
