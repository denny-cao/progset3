import random
import heapq

def karmarkar_karp(input_list: list[int]) -> int:
    """
    Differencing: Take two elements from A, a_i and a_j, and replace the larger by abs(a_i - a_j) while
    replacing the smaller by 0. Repeat this until only one element remains. Take largest 2 elements and
    difference.

    Args:
    input_list: List of integers

    Returns:
    int: Possible residue of input
    """

    # convert input_list to a heap
    heap = []
    for num in input_list:
        if num:
            heapq.heappush(heap, -num) # Negate the number to make it a max heap
    # perform Differencing
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        heapq.heappush(heap, -(a - b))

    return -heap[0]

def random_solution(input_list: list[int]) -> list[int]:
    """
    Generate a random solution by randomly assigning each element to a subset.

    Args:
    input_list: List of integers

    Returns:
    int: Possible residue of input
    """
    A = input_list

    n = len(input_list)
    P = [random.randint(0, n-1) for _ in range(n)]

    A_prime = [0] * n
    for j in range(n):
        A_prime[P[j]] += A[j]

    return P, A_prime

def repeated_random(input_list: list[int], num_iter: int) -> int:
    """
    Repeated Random: Randomly generate a solution and evaluate its residue. Repeat this num_iter times and
    return the best residue.

    Args:
    input_list: List of integers
    num_iter: Number of iterations

    Returns:
    int: Least residue of input_list
    """

    S, A = random_solution(input_list)
    for _ in range(num_iter):
        S_prime, A_prime = random_solution(input_list) 
        residue_S, residue_S_prime = karmarkar_karp(A), karmarkar_karp(A_prime)
        if residue_S_prime < residue_S:
            S = S_prime
            A = A_prime
        if residue_S == 0:
            break

    return S

def random_neighbor(input_list: list[int]) -> list[int]:
    """
    Repeatedly generate random solutions to the problem, as determined by the representation.

    Args:
    input_list: List of integers

    Returns:
    list[int]: Random neighbor of input_list
    """

    S = input_list

    n = len(input_list)
    i, j = random.sample(range(n), 2)
    S[i], S[j] = S[i]* random.choice([-1, 1]), S[j] * random.choice([-1, 1])
    return S


def hill_climbing(input_list: list[int], num_iter: int) -> int:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to better neighbors.

    Args:
    input_list: List of integers
    num_iter: Number of iterations

    Returns:
    int: Least residue of input_list
    """

    S = random_solution(input_list)
    for _ in range(num_iter):
        S_prime = random_neighbor(S)
        if karmarkar_karp(S_prime) < karmarkar_karp(S):
            S = S_prime
        if karmarkar_karp(S) == 0:
            break

    return S

def simulated_annealing(input_list: list[int], num_iter: int) -> int:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to neighbors, that are not always better.

    Args:
    input_list: List of integers
    num_iter: Number of iterations

    Returns:
    int: Least residue of input_list
    """

    S = random_solution(input_list
    S_double_prime = S

    for _ in range(num_iter):
        S_prime = random_neighbor(S)
        if karmarkar_karp(S_prime) < karmarkar_karp(S):
            S = S_prime
        else:
            delta = karmarkar_karp(S_prime) - karmarkar_karp(S)
            if random.random() < math.exp(-delta/num_iter):
                S = S_prime

    return S


    

