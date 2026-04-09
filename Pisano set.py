# k-Pisano-Legendre-primes-relative-to-(a,b)
# See https://doi.org/10.62072/acm.2026.09011
from sympy import legendre_symbol, primerange

def check(p,in1,in2,k):

    L, a, b, in1, in2 = [], in1, in2, in1%p, in2%p
    
    while True:

        L.append(legendre_symbol(a, p))

        a, b = b, (a + b)%p

        if (a, b) == (in1, in2): break

    return L.count(1) - L.count(-1) - L.count(0) == k 
a, b, k, n = 0, 1, 0, 3000

kpisano = [p for p in primerange(3, n) if check(p,a,b,k)]
print(kpisano)
