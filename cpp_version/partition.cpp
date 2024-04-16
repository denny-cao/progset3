# include <iostream>
# include <queue>
# include <fstream>
# include <string>
# include <functional>
# include <array>
# include <vector>
# include <cmath>
# include <random>

using namespace std;

long long karmarkar_karp(vector<long long> A) {
	priority_queue<long long> pq;
	for (int i = 0; i < A.size(); i++) {
		pq.push(A[i]);
	}
	while (pq.size() > 1) {
		long long a = pq.top();
		pq.pop();
		long long b = pq.top();
		pq.pop();
		pq.push(a - b);
	}
	// cout << pq.top() << endl;
	return pq.top();
}

vector<long long> random_std_solution(int s) {
	/*
	 * Generates a random standard solution of size s.
	*/
	vector<long long> S(s);
	for (int i = 0; i < s; i++) {
		S[i] = rand() % 2 == 0 ? 1 : -1;
	}
	return S;
}

vector<long long> random_neighbor(vector<long long> S) {
	/*
	 * Generates a random standard neighbor of S.
	*/

	// Select 2 random indices and flip with 50% probability.
	int i = rand() % S.size();
	int j = rand() % S.size();

	while (i == j) {
		j = rand() % S.size();
	}

	S[i] *= rand() % 2 == 0 ? 1 : -1;
	S[j] *= rand() % 2 == 0 ? 1 : -1;

	return S;
}

int residue(vector<long long> A, vector<long long> S) {
	/*
	 * Returns the residue of the input and the standard solution S.
	*/
	long long res = 0;
	for (int i = 0; i < A.size(); i++) {
		res += A[i] * S[i];
	}
	return res;
}

vector<long long> repeated_random(vector<long long> A, max_iter=25000) {
	/*
	 * Repeatedly generates random standard solutions and returns the best one.
	*/
	vector<long long> S = random_std_solution(sizeof(A));

	for (int i = 0; i < max_iter; i++) {
	    vector<long long> S_prime = random_std_solution(A.size());
	    if (residue(A, S_prime) < residue(A, S)) {
	        S = S_prime;
	    }
	}
	return S;
}

vector<long long> hill_climbing(vector<long long> A, max_iter=25000) {
	/*
	 * Walks through the neighborhood of the current solution and returns the best one.
	*/
	vector<long long> S = random_std_solution(sizeof(A));

	for (int i = 0; i < max_iter; i++) {
	    vector<long long> S_prime = random_neighbor(S);
	    if (residue(A, S_prime) < residue(A, S)) {
	        S = S_prime;
	    }
	}
	return S;
}

vector<long long> simulated_annealing(vector<long long> A, max_iter=25000) {
	/*
	 * Moves to a neighbor that may not be better than the current solution with a probability.
	*/
	vector<long long> S = random_std_solution(sizeof(A));
	vector<long long> S_double_prime = S;
	for (int i = 0; i < max_iter; i++) {
	    vector<long long> S_prime = random_neighbor(S);
	    if (residue(A, S_prime) < residue(A, S)) {
	        S = S_prime;
	    } else {
	        long long T = 10 ** 10 * (0.8 ** (i / 300));
	        long long p = exp(-(residue(A, S_prime) - residue(A, S)) / T);
	        if (rand() % 100 < p) {
	            S = S_prime;
	        }
	    }
		if (residue(A, S) < residue(A, S_double_prime)) {
			S_double_prime = S;
		}
	}
	return S;
}
int main(int argc, char* argv[]) {
	if (argc != 4) {
		cout << "Usage: ./partition <flag> <algorithm> <input_file>" << endl;
		return 1;
	}

	int flag = stoi(argv[1]); // Autograder will use 0.
	int algorithm = stoi(argv[2]);
	
	string file_name = argv[3]; // Input file is 100 unsorted numbers, one for each line
	ifstream input_file (file_name);

	// Create an array of size 100
	vector<long long> A(100);

	// Read the input file and store the numbers in the array
	if (!input_file.is_open()) {
	    for (int i = 0; i < 100; i++) {
		    input_file >> A[i];
		}
	}

	function functions[14];
	functions[0] = karmarkar_karp;
	functions[1] = repeated_random;
	functions[2] = hill_climbing;
	functions[3] = simulated_annealing;
	functions[11] = pp_repeated_random;
	functions[12] = pp_hill_climbing;
	functions[13] = pp_simulated_annealing;

	if (algorithm == 0) {
		cout << functions[algorithm](A) << endl;
	} else if (algorithm == 1 || algorithm == 2 || algorithm == 3) {
		cout << residue(A,functions[algorithm](A)) << endl;
	} 
}
