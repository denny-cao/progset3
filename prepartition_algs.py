import random
import numpy as np
from kk import karmarkar_karp

MAX_ITER = 25000

##########################################################################################
# Helper Functions #######################################################################
##########################################################################################
def prepartition_to_standard(A: list[int], P: list[int]) -> list[int]:
    """
    Convert prepartition to standard representation.

    Args:
    A: Input list of integers 
    P: Prepartition of input list

    Returns:
    list[int]: Standard representation of prepartition form
    """
    A_prime = [0] * len(A)
    for j in range(len(A)):
        A_prime[P[j]] += A[j]

    return A_prime

def random_solution(A: list[int]) -> list[int]:
    """
    Generate a random prepartitioning of the input list.

    Args:
    A: Input list of integers

    Returns:
    list[int]: Random solution of A in prepartition form
    """

    return [random.randint(0, len(A) - 1) for _ in range(len(A))]

def random_neighbor(P: list[int]) -> list[int]:
    """
    Random move on prepartitioning.

    Args:
    P: Input solution in prepartition form

    Returns:
    list[int]: Random neighbor of input solution in prepartition form
    """

    i,j = random.randint(0, len(P) - 1), random.randint(0, len(P) - 1)
    while P[i] == j:
        j = random.randint(0, len(P) - 1)
    P[i] = j

    return P
##########################################################################################
# Algorithms #############################################################################
##########################################################################################
def repeated_random(A: list[int], max_iter: int=MAX_ITER) -> int:
    """
    Repeated Random: Randomly generate a solution and evaluate its residue. Repeat this num_iter times and
    return the best residue.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    int: Least residue of input_list
    """
    S = random_solution(A)
    for _ in range(max_iter):
        S_prime = random_solution(A)
        residue_S_prime, residue_S = karmarkar_karp(S_prime), karmarkar_karp(S)

        if residue_S_prime < residue_S:
            S = S_prime
        if residue_S == 0:
            break

    return S

def hill_climbing(A: list[int], max_iter: int=MAX_ITER) -> int:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to better neighbors.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    int: Least residue of A
    """
    S = random_solution(A)
    for _ in range(max_iter):
        S_prime = random_neighbor(S)
        residue_S_prime, residue_S = karmarkar_karp(S_prime), karmarkar_karp(S)

        if residue_S_prime < residue_S:
            S = S_prime
        if residue_S == 0:
            break

    return S

def simulated_annealing(A: list[int], max_iter: int=MAX_ITER) -> int:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to neighbors, that are not always better.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    int: Least residue of input_list
    """

    S = random_solution(A)
    S_double_prime = S

    for _ in range(max_iter):
        S_prime = random_neighbor(S)
        residue_S_prime, residue_S = karmarkar_karp(S_prime), karmarkar_karp(S)

        if residue_S_prime < residue_S:
            S = S_prime
        elif np.random.rand() < np.exp((residue_S - residue_S_prime) / 100):
            S = S_prime

        residue_S_double_prime = karmarkar_karp(S_double_prime)
        if residue_S_prime < residue_S_double_prime:
            S_double_prime = S_prime

        if residue_S == 0:
            break

    return S_double_prime
