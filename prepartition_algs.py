import random
import numpy as np
from kk import karmarkar_karp

MAX_ITER = 25000
T = 10**10 * ((0.8)**(np.floor(MAX_ITER/300)))
##########################################################################################
# Helper Functions #######################################################################
##########################################################################################
def random_solution(A: np.ndarray) -> np.ndarray:
    """
    Generate a random prepartitioning of the input list.

    Args:
    A: Input list of integers

    Returns:
    np.ndarray: Random solution of A in prepartition form
    """

    return np.random.randint(0, len(A), len(A))

def random_neighbor(P: np.ndarray) -> np.ndarray:
    """
    Random move on prepartitioning.

    Args:
    P: Input solution in prepartition form

    Returns:
    list[int]: Random neighbor of input solution in prepartition form
    """

    P_copy = P.copy()
    i,j = random.sample(range(len(P)), 2)
    P_copy[i] = j

    return P_copy

def residue(P: np.ndarray, A: np.ndarray) -> np.int64:
    """
    Calculate residue of prepartition.

    Args:
    P: Prepartition of input list
    A: Input list of integers

    Returns:
    np.int64: Residue of prepartition
    """
    A_prime = np.zeros(len(A))
    for j in range(len(A)):
        A_prime[P[j]] += A[j]

    return karmarkar_karp(A_prime)

##########################################################################################
# Algorithms #############################################################################
##########################################################################################
def repeated_random(A: np.ndarray, max_iter: int=MAX_ITER) -> np.int64:
    """
    Repeated Random: Randomly generate a solution and evaluate its residue. Repeat this num_iter times and
    return the best residue.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    np.int64: Least residue of input_list
    """
    P = random_solution(A)
    for _ in range(max_iter):
        P_prime = random_solution(A)
        residue_P_prime, residue_P = residue(P, A), residue(P_prime, A)

        if residue_P_prime < residue_P:
            P = P_prime
        if residue_P == 0:
            break

    return P

def hill_climbing(A: np.ndarray, max_iter: int=MAX_ITER) -> np.int64:
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
        residue_P_prime, residue_P = residue(P_prime, A), residue(P, A)

        if residue_P_prime < residue_P:
            P = P_prime
        if residue_P == 0:
            break

    return P

def simulated_annealing(A: np.ndarray, max_iter: int=MAX_ITER) -> np.ndarray:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to neighbors, that are not always better.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    np.ndarray: Least residue of A
    """
    P = random_solution(A)
    P_double_prime = P

    for _ in range(max_iter):
        P_prime = random_neighbor(P)
        residue_P_prime, residue_P = residue(P_prime, A), residue(P, A)

        if residue_P_prime < residue_P:
            P = P_prime
        elif np.random.rand() < np.exp(-(residue_P_prime - residue_P)/T):
            P = P_prime

        residue_P_double_prime = residue(P_double_prime, A)
        if residue_P_prime < residue_P_double_prime:
            P_double_prime = P_prime

        if residue_P == 0:
            break

    return P_double_prime
