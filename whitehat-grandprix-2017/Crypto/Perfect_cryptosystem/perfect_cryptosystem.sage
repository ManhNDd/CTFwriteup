from sage.all import *
import itertools


def secure_random():
    # https://xkcd.com/221/
    return 4


def shuffle(s):
    n = len(s)
    for i in xrange(n):
        r = i + randint(0, n - i - 1)
        s[r], s[i] = s[i], s[r]
    return s


def sum_nu(poly, u):
    nu = []
    for m in poly.monomials():
        if u in m.variables():
            nu += m.variables()
    s = 0
    for v in list(set(nu)):
        s += v
    return s


def distance(poly, u, v):
    if u * v in poly.monomials():
        return 1
    nu = []
    nv = []
    for m in poly.monomials():
        if u in m.variables():
            nu += m.variables()
        elif v in m.variables():
            nv += m.variables()

    if list(set(nu) & set(nv)):
        return 2

    return 3


def reduce(poly, mono):
    for (u, v) in itertools.combinations(mono.variables(), 2):
        if distance(poly, u, v) < 3:
            return 0
    m = 1
    for v in mono.variables():
        m *= v
    return m


def keygen(sk_size):
    pk_size = sk_size * 4
    R = PolynomialRing(ZZ, 'v', pk_size)
    v = R.gens()
    pk = 0

    m = ZZ.range(pk_size)
    m = shuffle(m)
    pm = [m[sk_size * i:sk_size * (i + 1)] for i in range(4)]
    ind = ZZ.range(sk_size)

    ind = shuffle(ind)
    for i in xrange(sk_size):
        i1 = pm[0][i]
        i2 = pm[1][ind[i]]
        pk += v[i1] * v[i2]

    ind = shuffle(ind)
    for i in xrange(sk_size):
        i1 = pm[0][i]
        i2 = pm[2][ind[i]]
        pk += v[i1] * v[i2]

    ind = shuffle(ind)
    for i in xrange(sk_size):
        i1 = pm[0][i]
        i2 = pm[3][ind[i]]
        pk += v[i1] * v[i2]

    ind = shuffle(ind)
    for i in xrange(sk_size):
        i1 = pm[1][i]
        i2 = pm[2][ind[i]]
        pk += v[i1] * v[i2]

    ind = shuffle(ind)
    for i in xrange(sk_size):
        i1 = pm[1][i]
        i2 = pm[3][ind[i]]
        pk += v[i1] * v[i2]

    ind = shuffle(ind)
    for i in xrange(sk_size):
        i1 = pm[2][i]
        i2 = pm[3][ind[i]]
        pk += v[i1] * v[i2]

    sk = [v[i] for i in pm[0]]
    return sk, pk


def encrypt(m, pk):
    mi = '0x'
    for c in m:
        mi += hex(ord(c))[2:]
    M = Integer(mi)

    # partition graph
    psize = secure_random()
    V = pk.variables()
    S = [[V[i + j] for j in xrange(psize)]
         for i in xrange(0, pk.nvariables(), psize)]

    # partition message
    CS = []
    sum = ZZ(0)
    for i in xrange(0, pk.nvariables() - psize, psize):
        cs = ZZ.random_element(19 - 2 ^ 255, 2 ^ 255 - 19)  # remember me?
        CS += [cs]
        sum += cs
    CS += [M - sum]

    # build the polynomial
    F = 0
    i = 0
    for Si in S:
        f = CS[i]
        for u in Si:
            f *= sum_nu(pk, u)
            sf = 0
            for m in f.monomials():
                sf += f.monomial_coefficient(m) * reduce(pk, m)
            f = sf
        F += f
        i += 1

    return F


def decrypt(c, sk):
    nv = c.nvariables()
    subs = []
    for v in c.variables():
        value = 1 if v in sk else 0
        subs += [value]

    return hex(c(subs)).decode('hex')


if __name__ == '__main__':
    set_random_seed()
    msg = 'xxx'
    sk, pk = keygen(32)
    cipher = encrypt(msg, pk)
    print pk
    print cipher
