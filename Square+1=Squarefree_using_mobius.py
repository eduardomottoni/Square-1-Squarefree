def mobius_function(n):
    # Compute the Möbius function values up to n
    mobius = [0] * (n + 1)
    mobius[0] = mobius[1] = 1

    for i in range(1, n + 1):
        for j in range(2 * i, n + 1, i):
            mobius[j] -= mobius[i]

    return mobius

def count_squarefree_numbers_in_range(start, end):
    mobius_values = mobius_function(1 + (end**2))

    # Use a generator expression for squared_terms
    squared_terms = (1 + x**2 for x in range(start, end + 1))

    # Use a generator expression for filtered_terms
    filtered_terms = (term for term in squared_terms if mobius_values[term] != 0)

    # Print the count of filtered_terms
    print(sum(1 for _ in filtered_terms))

    result = 0
    return result

# Find the count of square-free numbers in the range [1, 10000000000]
result = count_squarefree_numbers_in_range(1, 1000)
