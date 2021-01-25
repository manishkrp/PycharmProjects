# This python program finds out the
# largest prime factor of the given no.
import math

def maxPrime(n):

    max_prime = -1

    # if the given no.is even
    if n % 2 == 0:
        max_prime = 2
        n /= 2

    #the no.being even is ruled out here
    for i in range(3,int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n/i

    if n > 2:
        max_prime = n

    return int(max_prime)

# driver program
n = 15
val = maxPrime(n)
print(str(val))

n = 2536589754363
val = maxPrime(n)
print(str(val))
