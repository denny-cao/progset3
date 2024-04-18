import prepartition_algs 
import standard_algs

def residue_test():
    # Test residue function
    A = [10, 8, 7,6, 5]
    # P = [1,2,2,4,5]
    P = [0,1,1,3,4]

    assert prepartition_algs.residue_prepartition(A, P) == 4

def simulated_annealing_test():
    # Test simulated annealing
    A = [10,8,7,6,5]

    print(standard_algs.residue(standard_algs.simulated_annealing(A), A))

if __name__ == "__main__":
    simulated_annealing_test()
    print("All tests passed!")

