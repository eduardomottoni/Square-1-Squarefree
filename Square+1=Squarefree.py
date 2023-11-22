from sympy import primerange
from math import isqrt

def generate_primes_up_to_limit(limit):
    # Generate a set of prime numbers up to the given limit
    return set(primerange(2, limit))

def is_squarefree(n, primes):
    # Check if n is squarefree

    # If n is even, divide it by 2 using bitwise operations
    if n & 1 == 0:
        n >>= 1

    # If 2 again divides n, then n is not a squarefree number.
    if n & 1 == 0:
        return False

    # Calculate the square root of n only once
    sqrt_n = isqrt(n)

    # Iterate through the precomputed set of primes
    for prime in primes:
        # If the prime is greater than the square root of n, break the loop
        if prime > sqrt_n:
            break
        # If n is divisible by the square of the current prime, it's not squarefree
        if n % (prime**2) == 0:
            return False
    
    # Return True if n is squarefree
    return True
def square_free_sieve(limit,squarefree_count):
    """Generator that yields all square free numbers less than limit"""
    a = [True] * limit
    # Needed so we don't mark off multiples of 1^2
    yield 1
    a[0] = a[1] = False
    for i, is_square_free in enumerate(a):
        if is_square_free:
            yield i
            
            i2 = i * i +1
            for n in range(i2, limit, i2):
                a[n] = False
            
# def count_squarefree_numbers(limit):
#     squarefree_count = 0

#     # Generate a set of primes up to the square root of the limit
#     primes_up_to_sqrt_limit = generate_primes_up_to_limit(isqrt(limit))

#     # Iterate through numbers up to the given limit
#     for p in range(1, limit + 1):
#         # Calculate the candidate number
#         candidate = p**2 + 1
        
#         # Check if the candidate is squarefree using the precomputed set of primes
#         if is_squarefree(candidate, primes_up_to_sqrt_limit):
#             squarefree_count += 1

#     return squarefree_count

def count_squarefree_numbers(limit):
    squarefree_count = 0

    # Generate a set of primes up to the square root of the limit
   
    return len(list(square_free_sieve(limit,squarefree_count)))
# Example usage

#limit = 123567101113
limit = 100
result = count_squarefree_numbers(limit)
print(result)
