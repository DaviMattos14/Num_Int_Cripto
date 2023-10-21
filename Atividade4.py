# Atividade 4 - Algoritmos
from math import floor, sqrt

# Exercício 1


def mod(a, b): return a % b


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, mod(a, b))

# Exercício 2


def xmdc(a, b):  # Quero xmdc(a,b) = xA + yB
    if a % b == 0:
        return b, 0, 1
    q, r = divmod(a, b)
    mdc, x, y = xmdc(b, r)
    return mdc, y, x - q*y

# Exercício 3


def bezout(a, b):
    mdc, x, y = xmdc(a, b)
    print(f"{mdc} = {x}*{a} + {y}*{b}")

# Exercício 4


def inverse_of(a, m):
    mdc, x, y = xmdc(m, a)
    return y % m

# Exercício 5


def trial(n, nxt=2):
    assert nxt >= 2, "but the smallest prime is 2, isn't it?"
    assert n >= 2
    if nxt > floor(sqrt(n)):
        return n
    if divides(nxt, n):
        return nxt
    return trial(n, nxt + 1)


def itrial(n, nxt=2):
    assert nxt >= 2
    assert n >= 2
    for nxt in range(nxt, floor(sqrt(n)) + 1):
        if divides(nxt, n):
            return nxt
    return n


def divides(b, a):
    return (a % b) == 0

# Exercício 7


def is_prime(n):
    if itrial(n) == n:
        return True
    return False

#Exercício 8

def primes_by_trial(n):

    return [(2, 2), (3,1)]

if "__main__" == __name__: 
    #print(mdc(18,60) == 6)
    #print(mdc(123,456) == 3)
    #print(xmdc(8,5))
    #print(xmdc(5,8))
    #bezout(13,22)
    #print(inverse_of(5,8))
    #print(trial(8164489))
    print(itrial(8164489))