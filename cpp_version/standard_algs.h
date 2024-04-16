# include <iostream>
# include <random>
# include <vector>
using namespace std;

vector<long long> random_std_solution(int s) {
	/*
	 * Generates a random standard solution of size s.
	*/
	vector<int> S(s);
	for (int i = 0; i < s; i++) {
		S[i] = rand() % 2 == 0 ? 1 : -1;
	}
	return S;
}

vector<long long> random_neighbor(vector<int> S) {
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
	for (int i = 0; i < sizeof(A); i++) {
		res += A[i] * S[i];
	}
	return res;
}

vector<long long> repeated_random(vector<int> A, max_iter=25000) {
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

vector<long long> hill_climbing(vector<int> A, max_iter=25000) {
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

vector<long long> simulated_annealing(vector<int> A, max_iter=25000) {
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