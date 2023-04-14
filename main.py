# Miller-Rabin primality test
import random              # needed for random numbers generations
def modulo(b, y, p):        # function for computing b^y mod p
    res = 1;               # setting internal variable to 1
    b = b % p;             # updating b in cas it is mor than or equal to p
    while (y > 0):         # loop until y is less or equal to 0
        if (y & 1):        # odd y, multiply b with the result to get new result
            res = (res * b) % p;
        y = y >> 1;        # y is even, compute y = y/2
        b = (b * b) % p;   # update b
    return res;            # return result

def MillerRabinTest(d, n):     # test body, need to be repeated k times
    a = 2 + random.randint(1, n - 4); # random intiger "a" in range [2, n-2]
                           # Compute a^d % n
    b = modulo(a, d, n);
    if (b == 1 or b == n - 1):
        return True;       # n is probably prime
    while (d != n - 1):    # until d is not n-1
        b = (b * b) % n;   # square b, compute modulo
        d *= 2;            # multiply d by 2
        if (b == 1):       # check if b is equal to 1, if yes then return
            return False;  # n is composite
        if (b == n - 1):   # check if b is equal to n-1, if yes then return
            return True;   # n is probably prime
    return False;          # n is composite

def isPrime(n, k):         # function needed to initialize the test with proper parameters
    if (n <= 1 or n == 4): # Check initial case undefined by the test
        return False;      # n is composite
    if (n <= 3):           # Check initial case undefined by the test
        return True;       # n is probably prime
    d = n - 1;             # computing d such that n= 2^d * r + 1, r >= 1
    while (d % 2 == 0):    # until d mod 2 is not equal to 0
        d //= 2;           # integer division by 2, returns whole part
    for i in range(k):     # repeating k times
        if (MillerRabinTest(d, n) == False):
            return False;  # n is composite
    return True;           # n is probably prime

def Accuracy(n, k):        # function for computing the accuracy of the algorithm
    b=bin(n).count("1")+bin(n).count("0"); # counting bits of the solution
    if ((b >= 21) and ( k >= b/4)):        # requirements for boundary to hold
        Ac=((1/7)*(b**(15/4))*(2**(-b/2)))*(4**(-k));# boundary computing
        Ac=Ac*100;         # percentage computing
    else:
        Ac=4**(-k);         # boundary computing for smaller cases
        Ac=Ac*100;         # percentage computing
    return Ac;