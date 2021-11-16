'''
Fast Integer Exponentiation:
Compute n^m: i.e. 7^11 => convert m(11) to binary rep.
=> 7^(1011) => 7^1*8 * 7^0*4 * 7^1*2 * 7^1*1
=> 7^2^3 * 7^0 * 7^2 * 7^1 = 7^8 * 7^3 = 7^11
'''


def fast_exp(a, b, c):
    # a = coeff, b = exp, c = modulo divisor
    a %= c
    for _ in range(b):
        a = a ** 2 % c
    return a


result = fast_exp(34522, 159, 7)
print(result)


def mod_arith(a, b, n):
    add = (a + b) % n == ((a % n) + (b % n)) % n
    sub = (a - b) % n == ((a % n) - (b % n)) % n
    mult = (a * b) % n == ((a % n) * (b % n)) % n

    a**2 % b == (a * a) % b
    a**4 % b == (a**2 % b)**2 % b
    a**8 % b == ((a**2 % b)**2 % b)**2 % b
