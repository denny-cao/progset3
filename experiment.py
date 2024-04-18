import random
import csv 
import standard_algs
import prepartition_algs
from kk import karmarkar_karp
from tqdm import tqdm

INSTANCES = 50 # Required: 50
ITERATIONS = 2500000 # Required: 25000
INPUT_SIZE = 100 
MAX_VALUE = 10**12

def experiment_record():
    with open('experiment.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["KK", "Repeated Random", "Hill Climbing", "Simulated Annealing", "Repeated Random PP", "Hill Climbing PP", "Simulated Annealing PP"])

        for i in tqdm(range(INSTANCES)):
            data = [random.randint(1, MAX_VALUE) for _ in range(INPUT_SIZE)]
    
            kk_result = karmarkar_karp(data)

            repeated_random_result = standard_algs.residue(standard_algs.repeated_random(data,ITERATIONS), data)
            hill_climbing_result = standard_algs.residue(standard_algs.hill_climbing(data, ITERATIONS), data)
            simulated_annealing_result = standard_algs.residue(standard_algs.simulated_annealing(data,ITERATIONS),data)

            pp_repeated_random_result = prepartition_algs.residue(prepartition_algs.repeated_random(data,ITERATIONS), data)
            pp_hill_climbing_result = prepartition_algs.residue(prepartition_algs.hill_climbing(data, ITERATIONS), data)    
            pp_simulated_annealing_result = prepartition_algs.residue(prepartition_algs.simulated_annealing(data,ITERATIONS),data)
    
            # Write to file
            writer.writerow([kk_result, repeated_random_result, hill_climbing_result, simulated_annealing_result, pp_repeated_random_result, pp_hill_climbing_result, pp_simulated_annealing_result])

if __name__ == "__main__":
    experiment_record()
