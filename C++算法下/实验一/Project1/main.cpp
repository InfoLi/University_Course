/*
#include <iostream>
#include <ctime>
#include<assert.h>
#include<limits.h>
#include "ParPtrTree.h"
using namespace std;
void main() {
	// 65536 655360 6553600
	for (int i = 0; i < 10; i++) {
		ParPtrTree test = ParPtrTree(6553600);
		unsigned seed;
		seed = time(0);
		srand(seed);

		for (int i = 0; i < 6553600; i++) {
			test.UNION(rand() % 65536, rand() % 65536);
		}
	}
	cout << endl << sum / 10;
	system("pause");
}
*/
