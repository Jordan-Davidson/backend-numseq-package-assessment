def is_prime(n):
    """ Returns true or false if n is prime """
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for num in range(3, int(n **0.5) + 1, 2):
            if n % num == 0:
                return False
    return True


def primes(n):
    """ Returns a list of all prime numbers less than n """
    res = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            res.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return res
