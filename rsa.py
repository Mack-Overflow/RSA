from math import gcd, sqrt
import random
import numpy as np


"""
    Implement RSA Encryption, call your method names, details below:
    sieve(), gcd_ex(a, b), modulo_expo(base, exponent, modulus), 
"""


# zero-fill sieves it's generally faster than one-filling
#     value of zero in the array implies that the current index is a prime number
#     value of one in the array implies that the current index is a composite number
sieves = np.zeros(shape=2**17, dtype=np.uint32)
primes = []  # fill primes array with prime #s calculated by sieve

""" 
    using the Sieve of Eratosthenes, please calculate prime numbers < 2^17
    For this assignment only use prime numbers > 2^16, which is a little less than half the prime numbers)
"""


def sieve():
    global primes
    global sieves
    upperBound = 2**17
    startPrimes = 2**16
    # loop through values from 2 and all square roots up to upperBound
    p = 2
    while (p**2 <= upperBound):
        if sieves[p] == 0:  # if curr index in sieves is primes
            for i in range(p*2, upperBound, p):
                sieves[i] = 1
        p += 1
    sieves[0], sieves[1] = 1, 1

    for k in range(upperBound):
        if not sieves[k]:
            primes.append(k)

    return primes


"""
Implement extended Euclidean Algorithm
should return gcd, x, y
see https://learn.zybooks.com/zybook/UVUCS3310MortensenSpring2021/chapter/9/section/5
"""


def gcd_ex(a, b):
    s, x = 1, 0
    t, y = 0, 1

    if a > b:
        a, b = b, a

    while a:
        q = b // a
        s, x = x, s - q * x
        t, y = y, t - q * y
        a, b = b % a, a

    return (b, s, t)


""" 
implement modular exponentiation
https://learn.zybooks.com/zybook/UVUCS3310MortensenSpring2021/chapter/9/section/7
See Figure 9.7.4: An iterative algorithm for fast modular exponentiation.
"""


def modulo_expo(base, exponent, modulus):
    a, b, c = 1, base, exponent
    while c > 0:
        if c % 2 == 1:
            a = (a*b) % modulus
        b = (b**2) % modulus
        c /= 2
    return a


"""
modulo_number used to calculate d and e will be (p-1)*(q-1)
function should return d, e; function should use extended euclidian algorithm
"""


def get_keys(p, q):
    z = (p-1) * (q-1)
    e = random.randrange(1, z)

    g = gcd_ex(e, z)[0]
    while g != 1:
        e = random.randrange(1, z)
        g = gcd_ex(e, z)[0]
    d = gcd_ex(e, z)[0]
    return d, e


"""
c = (m ** e) % n (return c)
where c is the encrypted message (m allowable up to max of a 32 bit unsigned integer, 2^32-1)
"""


def encrypt(m, e, N):
    c = modulo_expo(m, e, N)
    return c


"""
m = (c ** d) % n (return m)
where m is the decrypted plain text message (up to 32 bit unsigned integer)
"""


def decrypt(c, d, N):
    m = modulo_expo(c, d, N)
    return m


def main():
    global primes
    # global sieves
    # gcd_ex(2, 8)
    # sieves()
    print(modulo_expo(5, 2, 9))


main()
