# include <iostream>
# include <queue>

using namespace std;

int karmarkar_karp(int input[]) {
	priority_queue<int> pq;
	for (int i = 0; i < sizeof(input); i++) {
		pq.push(input[i]);
	}
	while (pq.size() > 1) {
		int a = pq.top();
		pq.pop();
		int b = pq.top();
		pq.pop();
		pq.push(a - b);
	}
	// cout << pq.top() << endl;
	return pq.top();
}
