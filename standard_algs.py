import random
import heapq
import numpy as np
from kk import karmarkar_karp

##########################################################################################
# Helper Functions #######################################################################
##########################################################################################
def random_solution(A: list[int]) -> list[int]:
    """
    Generate a random solution of -1 and 1.

    Args:
    A: Input list of integers

    Returns:
    list[int]: Random solution of A in standard form
    """

    return [random.choice([-1, 1]) for _ in range(len(A))]

def random_neighbor(S: list[int]) -> list[int]:
    """
    Generate a random neighbor of the input solution.

    Args:
    S: Input solution in standard form

    Returns:
    list[int]: Random neighbor of input solution in standard form
    """
    i,j = random.sample(range(len(S)), 2)
    S[i] *= random.choice([-1, 1])
    S[j] *= random.choice([-1, 1])
    return S

def standard_to_residue(S: list[int], A: list[int]) -> int:
    """
    Convert a standard solution to the residue of the input list.

    Args:
    S: Solution in standard form
    A: Input list of integers

    Returns:
    int: Residue of A given S
    """

    return np.multiply(S, A).sum()

##########################################################################################
# Algorithms #############################################################################
##########################################################################################
def repeated_random(A: list[int], max_iter: int) -> int:
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

def hill_climbing(A: list[int], max_iter: int) -> int:
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

def simulated_annealing(A: list[int], max_iter: int) -> int:
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
