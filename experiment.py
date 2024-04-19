import random
import csv 
import standard_algs
import prepartition_algs
from kk import karmarkar_karp
from tqdm import tqdm
import numpy as np
import time

INSTANCES = 50 # Required: 50
ITERATIONS = 25000 # Required: 25000
INPUT_SIZE = 100 
MAX_VALUE = 10**12

def experiment_record():
    with open('test.csv', mode='w') as file2:
        writer2 = csv.writer(file2)
        writer2.writerow(["KK", "Repeated Random", "Hill Climbing", "Simulated Annealing", "Repeated Random PP", "Hill Climbing PP", "Simulated Annealing PP"])
    with open('experiment4.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["KK", "Repeated Random", "Hill Climbing", "Simulated Annealing", "Repeated Random PP", "Hill Climbing PP", "Simulated Annealing PP"])

        for i in tqdm(range(INSTANCES)):
            data = np.random.randint(1, MAX_VALUE, INPUT_SIZE)
            with open('times.csv', mode='a') as file2:
                writer2 = csv.writer(file2)
                kk_start = time.time()
                kk_result = karmarkar_karp(data)
                kk_end = time.time()

                repeated_random_start = time.time()
                repeated_random_result = standard_algs.residue(standard_algs.repeated_random(data,ITERATIONS), data)
                repeated_random_end = time.time()

                hill_climbing_start = time.time()
                hill_climbing_result = standard_algs.residue(standard_algs.hill_climbing(data, ITERATIONS), data)
                hill_climbing_end = time.time()

                simulated_annealing_start = time.time()
                simulated_annealing_result = standard_algs.residue(standard_algs.simulated_annealing(data,ITERATIONS),data)
                simulated_annealing_end = time.time()

                pp_repeated_random_start = time.time()
                pp_repeated_random_result = prepartition_algs.residue(prepartition_algs.repeated_random(data,ITERATIONS), data)
                pp_repeated_random_end = time.time()

                pp_hill_climbing_start = time.time()
                pp_hill_climbing_result = prepartition_algs.residue(prepartition_algs.hill_climbing(data, ITERATIONS), data)
                pp_hill_climbing_end = time.time()

                pp_simulated_annealing_start = time.time()
                pp_simulated_annealing_result = prepartition_algs.residue(prepartition_algs.simulated_annealing(data,ITERATIONS),data)
                pp_simulated_annealing_end = time.time()

                writer2.writerow([kk_end - kk_start, repeated_random_end - repeated_random_start, hill_climbing_end - hill_climbing_start, simulated_annealing_end - simulated_annealing_start, pp_repeated_random_end - pp_repeated_random_start, pp_hill_climbing_end - pp_hill_climbing_start, pp_simulated_annealing_end - pp_simulated_annealing_start])

                writer.writerow([kk_result, repeated_random_result, hill_climbing_result, simulated_annealing_result, pp_repeated_random_result, pp_hill_climbing_result, pp_simulated_annealing_result])
    
def experiment():
    for i in tqdm(range(INSTANCES)):
        data = np.random.randint(1, MAX_VALUE, INPUT_SIZE)
    
        repeated_random_result = standard_algs.residue(standard_algs.repeated_random(data,ITERATIONS), data)
        hill_climbing_result = standard_algs.residue(standard_algs.hill_climbing(data, ITERATIONS), data)
        simulated_annealing_result = standard_algs.residue(standard_algs.simulated_annealing(data,ITERATIONS),data)

        pp_repeated_random_result = prepartition_algs.residue(prepartition_algs.repeated_random(data,ITERATIONS), data)
        pp_hill_climbing_result = prepartition_algs.residue(prepartition_algs.hill_climbing(data, ITERATIONS), data)    
        pp_simulated_annealing_result = prepartition_algs.residue(prepartition_algs.simulated_annealing(data,ITERATIONS),data)

if __name__ == "__main__":
    experiment_record()
