import itertools

def bruteForce(arr):
    n = len(arr)
    min_cost = float('inf')
    min_permutation = None
    for permutation in itertools.permutations(range(n)):
        cost = 0
        for i, j in enumerate(permutation): 
            cost += arr[i][j]
            cost_str = ' + '.join([str(C[i][j]) for i, j in enumerate(permutation)])
        if cost < min_cost:
            min_cost = cost
            min_permutation = permutation
            
        print(f"Assignment: {permutation} : {cost_str} with total cost of {cost}")
    return min_permutation, min_cost

C = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 4],
    [7, 6, 9, 4]
]

min_permutation, min_cost = bruteForce(C)
print(f"Minimum cost assignment: {min_permutation} with cost {min_cost}")