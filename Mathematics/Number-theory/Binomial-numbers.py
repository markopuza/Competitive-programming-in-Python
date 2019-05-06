''' Computes the Binomial numbers. '''

#########################################################################

# O(k)
def choose(n, k):
    if k < 0 or k > n or n < 0:
        return 0

    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result

# O(k)
def mod_choose(n, k, M, modinv):
    ''' Computes {n choose k} mod M '''
    if k < 0 or k > n or n < 0:
        return 0

    result = 1
    for i in range(k):
        result = result * (n - i) % M
        result = result * modinv[i + 1] % M
        result %= M
    return result

# O(max_n**2)
def mod_choose_dp(max_n, M):
    ''' Computes all {n choose k} mod M for 0 <= n <= max_n, using dynamic programming '''
    ch = [[0 for _ in range(max_n+1)] for _ in range(max_n+1)]
    ch[0][0] = 1
    for n in range(max_n+1):
        for k in range(n+1):
            if k in [0, n]:
                ch[n][k] = 1
            else:
                ch[n][k] = (ch[n-1][k-1] + ch[n-1][k]) % M
    return ch

##########################################################################







'''    Verification test    '''
if __name__ == "__main__":
    M = 1000000007; modinv = [-1 for _ in range(1001)]
    modinv[1] = 1
    for x in range(2, 1001):
        modinv[x] = (-(M//x) * modinv[M%x])%M

    for arg in [(5, 0), (0, 5), (5, 5), (132, 22), (123, 34)]:
        r1, r2 = choose(*arg), mod_choose(*arg, M, modinv)
        assert r1 % M == r2
        if arg[0] >= arg[1] >= 0:
            r3 = mod_choose_dp(arg[0], M)[arg[0]][arg[1]]
            assert r2 == r3
        print('    {:<3d} choose {:<18d} = {:d}'.format(*arg, r1))
        print('    {:<3d} choose {:<3d} mod {:d} = {:d}'.format(*arg, M, r2))
