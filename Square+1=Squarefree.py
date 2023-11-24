def square_free_sieve(limit, values_set):
    """Count square-free numbers less than limit in the given set."""
    is_squarefree = [True] * (max(values_set) + 1)
    limit_sqrt = int(limit**0.5) + 1
    
    for i in range(2, limit_sqrt):
        if is_squarefree[i]:
            start = max(i*i, (min(values_set) // i) * i)
            for n in range(start, max(values_set) + 1, i*i):
                is_squarefree[n] = False

    square_free_numbers = sum(is_squarefree[n] for n in values_set)
    return square_free_numbers

# Defina o limite como um número inteiro maior
limit_int = 1000

# Crie o conjunto de números sem quadrados perfeitos
squares_set = {n**2 + 1 for n in range(1, limit_int + 1)}

# Use a função square_free_sieve com o limite
test2_set = square_free_sieve(max(squares_set), squares_set)

print(test2_set)
