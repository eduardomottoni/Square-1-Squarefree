# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 11:10:12 2023

@author: eotoni
"""


def is_squarefree(num, primes):
    # Check if the number is square-free
    for p in primes:
        if p * p > num:
            break
        if num % (p * p) == 0:
            return False
    return True

def sieve_of_eratosthenes(limit):
    # Implement the Sieve of Eratosthenes to find primes up to the square root of the input limit
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False

    return [p for p in range(2, limit + 1) if sieve[p]]

def count_squarefree_numbers_in_range(start, end):
    squarefree_count = 0
    limit = int(((end**2)+1)**0.5)
    primes = sieve_of_eratosthenes(limit)

    for x in range(start, end + 1):
        value = x**2 + 1

        if is_squarefree(value, primes):
            squarefree_count += 1

    return squarefree_count

# Find the count of square-free numbers in the range [1, 10]
result = count_squarefree_numbers_in_range(1, 1000)
print(result)

