''' Euler"s totient function for a single number '''


#########################################################################

from functools import lru_cache

def factorize(n):
    factorization = set()
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factorization.add(i)
                break
    return factorization

@lru_cache(maxsize=None)
def phi(n):
    totient = n
    for p in factorize(n):
        totient -= totient//p
    return totient

#########################################################################



'''    Verification test    '''
if __name__ == "__main__":
    assert phi(12312) == 3888
