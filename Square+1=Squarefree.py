def square_free_sieve(limit):
    """Generator that yields all square free numbers less than limit"""
    a = [True] * limit
    # Needed so we don't mark off multiples of 1^2
    yield 1
    a[0] = a[1] = False
    for i, is_square_free in enumerate(a):
        if is_square_free:
            yield i
            i2 = i * i
            for n in range(i2, limit, i2):
                a[n] = False

# Defina o limite como um número inteiro
# Defina o limite como um número inteiro
limit_int = 123567101113

# Crie o conjunto de números sem quadrados perfeitos
squares_set = {n**2 + 1 for n in range(1, limit_int + 1)}

# Use a função square_free_sieve com o limite
test2_set = set(square_free_sieve(max(squares_set)))

# Encontre a interseção entre os conjuntos
result_set = squares_set.intersection(test2_set)

print(result_set)
print(len(result_set))