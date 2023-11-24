def square_free_sieve(limit, values_set, start_index, end_index,square_free_list):
    """Count square-free numbers less than limit in the given set."""
    is_squarefree = [True] * (max(values_set) + 1)
    limit_sqrt = int(limit**0.5) + 1
    if start_index < 2:
        start_value = 2
        is_squarefree = [True] * (max(values_set) + 1)
        is_squarefree[0] = is_squarefree[1] = False
    else:
        start_value = start_index
        is_squarefree = square_free_list
    for i in range(start_value, end_index):
        if is_squarefree[i]:
            start = max(i*i, (start_index // i) * i)
            for n in range(start, min(end_index, max(values_set)) + 1, i*i):
                is_squarefree[n] = False

    
    return is_squarefree

# Defina o limite como um número inteiro maior
limit_int = 1000

# Crie o conjunto de números sem quadrados perfeitos
squares_set = {n**2 + 1 for n in range(0, limit_int)}

# Tamanho do chunk
chunk_size = 1000

# Inicialize a contagem total
total_square_free_numbers = 0
chunk_temp_holder_squarefree_numbers =[]
# Use a função square_free_sieve com o limite para cada chunk
for i in range(0, len(squares_set), chunk_size):
    start_index = i
    end_index = min(i + chunk_size, len(squares_set))
    chunk_square_free_numbers = square_free_sieve(max(squares_set), squares_set,
                                                  start_index, end_index, chunk_temp_holder_squarefree_numbers)
    chunk_temp_holder_squarefree_numbers = chunk_square_free_numbers
    square_free_numbers = sum(chunk_square_free_numbers[n] for n in squares_set)
    total_square_free_numbers += square_free_numbers
indices_true = [i for i in squares_set if chunk_temp_holder_squarefree_numbers[i]]
print(indices_true)
print(f"chunk size is: {chunk_size}")
print(f"Final total square free numbers: {len(indices_true)}")
