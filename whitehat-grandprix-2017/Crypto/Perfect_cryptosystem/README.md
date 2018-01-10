### Description:
We created a new perfect cryptosystem which is based on
- a secure random function
- a combinatorial NP-complete problem

We believe our cryptosystem is secure. Can you break our belief?

### Downloadable Files
    cipher
    pub
    perfect_cryptosystem.sage

The challenge provides us the implementation in Sagemath.
It looks so horrible.

So let's go with the description of the challenge.
All I get is this is based on a combinatorical NP-complete problem, and
the keyword "perfect" in the description.

If you're lucky, you will find this idea is based on the perfect code cryptosystem,
or "kid crypto".

This cryptosystem is actually constructed from a NP-complete problem, but it's not secure.
We can decrypt the ciphertext without finding the perfect code. We can use Gaussian elimination
to solve this challenge.

If you're not that lucky, well, time to read the code.
Firstly, take a look at `keygen`.
The secret key size is 32, thus the public key size is 32 * 4 = 128.

Maybe we could try with a smaller size, e.g., secret key size is 3.

Run the function and you will get a polynomial with 12 variables, which is the public key.
Print out each set `pm[0], pm[1], ..., pm[3]` we see that the public key is a sum of
products of elements from these sets, but **there is no products of 2 elements in the same set.**
We have 6 combinations.

So, we know that this function creates a polynomial of 128 variables. These set of variables are
divided to 4 subsets, (A1, A2, A3, A4). And the public key is created from products
of elements from A(i) and A(j) (i != j). We have 6 combinations.
The secret key is A1 set, so **there is no products of 2 elements in the same set.**

The public key can be seen as a representation of a 3-regular graph using polynomial.
Of course, the indices have been randomized so there is no specific order we can exploit.

Now, the `encrypt` part.
Based on the comments (thanks the author), we can see that:
1. the public key is divided into 32 subsets, 4 elements each. (Blame the author for his secure_random)
2. the message is converted to big integer and then writed as a sum of 32 random numbers.
3. for each partition of the public key (32 partitions), it construct a polynomial and then multiplies with
a partition of the message. (we temporarily ignore the reduce part for now)
4. the cipher text is the sum of all constructed polynomials.

The `decrypt` function is very simple, it validates the ciphertext polynomial with
- x(i) = 1 if x(i) is in secret key
- x(i) = 0 if x(i) is not.
All it does is to remove the polynomials which have variables not being in secret key.

So, to decrypt the message, all we do is to find how the message was divided.
If you have some sense of maths, you will recognize that this can be solve by "trying" reconstruct the
ciphertext with unknown coefficients. Then we will have an equation system and we will be able to recover
the partitions of the message. Solve it using Gaussion elimination (Sagemath is already supported this).

Take sum of them, we get the message.

Crytanalysis code:

```
def cryptanalysis(c, pk):
    # partition graph
    psize = secure_random()
    V = pk.variables()
    S = [[V[i + j] for j in xrange(psize)]
         for i in xrange(0, pk.nvariables(), psize)]

    F = []
    for Si in S:
        f = 1
        for u in Si:
            f *= sum_nu(pk, u)
            sf = 0
            for m in f.monomials():
                sf += f.monomial_coefficient(m) * reduce(pk, m)
            f = sf
        F += [f]

    mat = []
    for m in c.monomials():
        row = []
        for f in F:
            if m in f.monomials():
                row += [1]
            else:
                row += [0]
        row += [c.monomial_coefficient(m)]
        mat += [row]

    mat = [list(i) for i in set(map(tuple, mat))]
    M = matrix(ZZ, mat).echelon_form()
    return hex(sum(M.column(-1))).decode('hex')

R = PolynomialRing(ZZ, 'v1,v2,v3,...,v128', 128) # complete the list for me
c = '' # paste the cipher message here
pk = '' # paste the pub key here
print cryptanalysis(c, pk)
```

Flag is `Kid Krypto is secure for the given class of people!`
