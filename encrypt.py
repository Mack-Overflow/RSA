

def encrypt(m, k, N):
    c = (m + k) % N


def decrypt(c, k, N):
    m = (c - k) % N
