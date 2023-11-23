import numpy as np
from sympy import primerange, sqrt

def square_free_sieve(limit, values_set):
    """Generator that yields all square free numbers less than limit"""
    a = np.zeros((max(values_set) + 1), dtype=bool)
    # Needed so we don't mark off multiples of 1^2
    
    # Preencha com quadrados de números
    for i in range(2, limit):
        i **=2
        for n in range(i, limit, i):
            # for value in values_set:
            #     if value % n == 0:
            #         values_set.remove(value)
            if n in values_set:
                values_set.remove(n)

    # for i, sqrtnumber in enumerate(values_set):
    #     a[sqrtnumber] = True
    # primes = primerange(sqrt(limit)+1)
    # for prime in set(primes):
    #     prime **= 2
    #     for n in range(prime, limit, prime):
    #         a[n] = False
    # #yield 1
    # a[0] = a[1] = False
    # for i, is_square_free in enumerate(a):
    #     if is_square_free:
    #         #yield i
    #         i2 = i * i
    #         for n in range(i2, limit, i2):
    #             a[n] = False
    number = len(values_set)  # Soma dos True (1) no array
    return number

# Defina o limite como um número inteiro
# limit_int = 123567101113
limit_int = 10000

# Crie o conjunto de números sem quadrados perfeitos
squares_set = {n**2 + 1 for n in range(1, limit_int + 1)}

# Use a função square_free_sieve com o limite
test2_set = square_free_sieve(max(squares_set), squares_set)

# Encontre a interseção entre os conjuntos
#result_set = squares_set.intersection(test2_set)

print(test2_set)
