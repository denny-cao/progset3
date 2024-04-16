import random
import numpy as np
from kk import karmarkar_karp

MAX_ITER = 25000

##########################################################################################
# Helper Functions #######################################################################
##########################################################################################
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

    P_copy = P.copy()

    i,j = random.randint(0, len(P) - 1), random.randint(0, len(P) - 1)
    while P_copy[i] == j:
        j = random.randint(0, len(P) - 1)
    P_copy[i] = j

    return P_copy

def residue_prepartition(A: list[int], P: list[int]) -> int:
    """
    Calculate residue of prepartition.

    Args:
    A: Input list of integers
    P: Prepartition of input list

    Returns:
    int: Residue of prepartition
    """
    A_prime = [0] * len(A)
    for j in range(len(A)):
        A_prime[P[j]] += A[j]

    return karmarkar_karp(A_prime)

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
    P = random_solution(A)
    for _ in range(max_iter):
        P_prime = random_solution(A)
        residue_P_prime, residue_P = residue_prepartition(A, P_prime), residue_prepartition(A, P)

        if residue_P_prime < residue_P:
            P = P_prime
        if residue_P == 0:
            break

    return P

def hill_climbing(A: list[int], max_iter: int=MAX_ITER) -> int:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to better neighbors.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    int: Least residue of A
    """
    P = random_solution(A)
    for _ in range(max_iter):
        P_prime = random_neighbor(P)
        residue_P_prime, residue_P = residue_prepartition(A, P_prime), residue_prepartition(A, P)

        if residue_P_prime < residue_P:
            P = P_prime
        if residue_P == 0:
            break

    return P

def simulated_annealing(A: list[int], max_iter: int=MAX_ITER) -> int:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to neighbors, that are not always better.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    int: Least residue of input_list
    """
    T = 10**10 * ((0.8)**(max_iter//300))

    P = random_solution(A)
    P_double_prime = P

    for _ in range(max_iter):
        P_prime = random_neighbor(P)
        residue_P_prime, residue_P = residue_prepartition(A, P_prime), residue_prepartition(A, P)

        if residue_P_prime < residue_P:
            P = P_prime
        elif np.random.rand() < np.exp((residue_P - residue_P_prime) / T):
            P = P_prime

        residue_P_double_prime = karmarkar_karp(P_double_prime)
        if residue_P_prime < residue_P_double_prime:
            P_double_prime = P_prime

        if residue_P == 0:
            break

    return P_double_prime
