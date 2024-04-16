import sys
import kk
import standard_algs
import prepartition_algs

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 4:
        print('Usage: python3 partition.py <flag> <algorithm> <input_file>')
        sys.exit(1)

    flag = argv[1] # Autograder uses 0 but use others to debug

    algorithm = int(argv[2])
    algs = {
        0: 'kk.karmarkar_karp',
        1: 'standard_algs.repeat_random',
        2: 'standard_algs.hill_climbing',
        3: 'standard_algs.simulated_annealing',
        11: 'prepartition_algs.repeat_random',
        12: 'prepartition_algs.hill_climbing',
        13: 'prepartition_algs.simulated_annealing'
    }

    if algorithm not in algs:
        print('Invalid algorithm')
        sys.exit(1)

    # Parse input file
    input_file = argv[3] # List of 100 (unsorted) integers, one per line
    with open(input_file, 'r') as f:
        input_file = [int(line.strip()) for line in f]

    print(algs[algorithm](input_file))


