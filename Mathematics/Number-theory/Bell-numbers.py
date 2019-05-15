'''
    Bell number B_n is the number of different ways to partition (possibly empty) a set that has exactly n elements.
'''




#########################################################################
# DP approach

def Bell(n, MOD):
    b = [[0 for i in range(n+1)] for j in range(n+1)]
    b[0][0] = 1
    for i in range(1, n+1):
        b[i][0] = b[i-1][i-1]
        for j in range(1, i+1):
            b[i][j] = (b[i-1][j-1] + b[i][j-1]) % MOD
    return b[n][0]

#########################################################################





'''    Verification test    '''
if __name__ == "__main__":
    MOD = 10**9 + 7
    arr = [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570, 4213597, 27644437, 190899322, 1382958545, 10480142147, 82864869804, 682076806159, 5832742205057, 51724158235372, 474869816156751, 4506715738447323, 44152005855084346]
    assert all(x%MOD == y%MOD for x, y in zip(arr, [Bell(n, MOD) for n in range(len(arr))]))
