import sys
import algorithms

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 4:
        print('Usage: python3 partition.py <flag> <algorithm> <input_file>')
        sys.exit(1)

    flag = argv[1] # Autograder uses 0 but use others to debug

    algorithm = argv[2]
    algs = {
        0: 'karmarkar_karp',
        1: 'repeat_random',
        2: 'hill_climbing',
        3: 'simulated_annealing'
        11: 'prepartitioned_repeat_random',
        12: 'prepartitioned_hill_climbing',
        13: 'prepartitioned_simulated_annealing'
    }

    if algorithm not in algs:
        print('Invalid algorithm')
        sys.exit(1)

    # Parse input file
    input_file = argv[3] # List of 100 (unsorted) integers, one per line
    with open(input_file, 'r') as f:
        input_file = [int(line.strip()) for line in f]

    print(algorithms.algs[algorithm](input_file))


