# PRIME NUMBER GENERATOR WITH FUNCTIONAL PROGRAMING

# Generator Function
def generate(limit):
    P = [2, 3]
    sieve = [False] * (limit + 1)

    for x in range(1, int(limit**0.5) + 1):
        for y in range(1, int(limit**0.5) + 1):
            n = 4*x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3*x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3*x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for n in range(5, int(limit**0.5) + 1):
        if sieve[n]:
            for k in range(n**2, limit + 1, n**2):
                sieve[k] = False

    for p in range(5, limit + 1):
        if sieve[p]:
            P.append(p)

    return P

# Get The Biggest Prime Number Function
def biggest_prime(limit):
    max_prime = max(generate(limit))
    return max_prime