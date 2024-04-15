import random
import time
import csv 
import standard_algs
import prepartition_algs
from kk import karmarkar_karp

INSTANCES = 5 # Required: 50
ITERATIONS = 500 # Required: 25000
INPUT_SIZE = 5 # Required: 100
MAX_VALUE = 100

def experiment_record():
    # TODO: Implement this function to store data
    pass

def experiment():
    for i in range(INSTANCES):
        print(f"Instance {i+1}")
        data = [random.randint(0, MAX_VALUE) for _ in range(INPUT_SIZE)] 
        print(f"Data: {data}")
        # Part 1: Find result from KK algorithm
        kk_result = karmarkar_karp(data)
        print(f"KK result: {kk_result}")
       
        # Part 2: Find result from standard algorithms
        repeated_random_result = standard_algs.repeated_random(data, ITERATIONS)
        # print(f"Repeated random result: {repeated_random_result}")
        hill_climbing_result = standard_algs.hill_climbing(data, ITERATIONS)
        # print(f"Hill climbing result: {hill_climbing_result}")
        simulated_annealing_result = standard_algs.simulated_annealing(data, ITERATIONS)
        # print(f"Simulated annealing result: {simulated_annealing_result}")

        print(f"Repeated random residual: {standard_algs.standard_to_residue(data, repeated_random_result)}")
        print(f"Hill climbing residual: {standard_algs.standard_to_residue(data, hill_climbing_result)}")
        print(f"Simulated annealing residual: {standard_algs.standard_to_residue(data, simulated_annealing_result)}")
        
        # Part 3: Find result from prepartition algorithms
        repeated_random_pp_result = prepartition_algs.repeated_random(data, ITERATIONS)
        # print(f"Repeated random prepartition result: {repeated_random_pp_result}")
        hill_climbing_pp_result = prepartition_algs.hill_climbing(data, ITERATIONS)
        # print(f"Hill climbing prepartition result: {hill_climbing_pp_result}")
        simulated_annealing_pp_result = prepartition_algs.simulated_annealing(data, ITERATIONS)
        # print(f"Simulated annealing prepartition result: {simulated_annealing_pp_result}")

        print(f"Repeated random prepartition residual: {standard_algs.standard_to_residue(data, prepartition_algs.prepartition_to_standard(data, repeated_random_pp_result))}")
        print(f"Hill climbing prepartition residual: {standard_algs.standard_to_residue(data, prepartition_algs.prepartition_to_standard(data, hill_climbing_pp_result))}")
        print(f"Simulated annealing prepartition residual: {standard_algs.standard_to_residue(data, prepartition_algs.prepartition_to_standard(data, simulated_annealing_pp_result))}")

if __name__ == "__main__":
    experiment()
    # experiment_record()
