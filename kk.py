import heapq
import numpy as np

def karmarkar_karp(A: np.ndarray) -> int:
    """
    Differencing: Take two elements from A, a_i and a_j, and replace the larger by abs(a_i - a_j) while replacing the smaller by 0. Repeat this until only one element remains. Take largest 2 elements and difference.

    Args:
    A: Input list of integers

    Returns:
    int: Possible residue of input
    """
    # convert input_list to a heap
    heap = []
    for num in A:
        if num:
            heapq.heappush(heap, -num) # Negate the number to make it a max heap
    # perform Differencing
    while len(heap) > 1:
        x = -heapq.heappop(heap)
        y = -heapq.heappop(heap)
        heapq.heappush(heap, -(x - y))

    return -heap[0]

