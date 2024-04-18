import random
import numpy as np
from decimal import *

MAX_ITER = 25000

##########################################################################################
# Helper Functions #######################################################################
##########################################################################################
def random_solution(A: np.ndarray) -> np.ndarray:
    """
    Generate a random solution of -1 and 1.

    Args:
    A: Input list of integers

    Returns:
    list[int]: Random solution of A in standard form
    """

    # return [random.choice([-1, 1]) for _ in range(len(A))]
    return np.random.choice([-1, 1], size=len(A))

def random_neighbor(S: np.ndarray) -> np.ndarray:
    """
    Generate a random neighbor of the input solution.

    Args:
    S: Input solution in standard form

    Returns:
    np.ndarray: Random neighbor of input solution in standard form
    """

    S_copy = S.copy()
    i,j = random.sample(range(len(S_copy)), 2)
    S_copy[i] *= -1
    S_copy[j] *= random.choice([-1, 1])
    return S_copy


def residue(S: np.ndarray, A: np.ndarray) -> np.int64:
    """
    Calculate the residue of a solution.
    Args:
    S: Solution in standard form
    A: Input list of integers
    Returns:
    int: Residue of the solution
    """

    return np.abs(np.dot(S, A))

##########################################################################################
# Algorithms #############################################################################
##########################################################################################
def repeated_random(A: np.ndarray, max_iter: int=MAX_ITER) -> int:
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

        residue_S_prime, residue_S = residue(S_prime, A), residue(S, A)
        if residue_S_prime < residue_S:
            S = S_prime
        if residue_S == 0:
            break

    return S

def hill_climbing(A: np.ndarray, max_iter: int=MAX_ITER) -> int:
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

        residue_S_prime, residue_S = residue(S_prime, A), residue(S, A)
        if residue_S_prime < residue_S:
            S = S_prime
        if residue_S == 0:
            break

    return S

def simulated_annealing(A: np.ndarray, max_iter: int=MAX_ITER) -> np.ndarray:
    """
    Generate a random solution to the problem, and then attempt to improve it through moves to neighbors, that are not always better.

    Args:
    A: Input list of integers
    max_iter: Number of iterations

    Returns:
    np.ndarray: Least residue of A
    """
    S = random_solution(A)
    S_double_prime = S

    for iter in range(max_iter):
        T = (10**10) * ((0.8)**(np.floor(iter/300)))
        S_prime = random_neighbor(S)

        residue_S_prime, residue_S = residue(S_prime, A), residue(S, A)
        if residue_S_prime < residue_S:
            S = S_prime
        elif np.random.rand() < np.exp(-(residue_S_prime - residue_S) / T):
            S = S_prime

        residue_S_double_prime = residue(S_double_prime, A)
        if residue_S_prime < residue_S_double_prime:
            S_double_prime = S_prime

        if residue_S == 0:
            break

    return S_double_prime
