#include <iostream>
using namespace std;
#define ROOT -1
// ���ڵ��ʾ��
int sum = 0;
class ParPtrTree {
private:
	int* array;		//Ԫ��ֵΪ���ڵ��λ��
	int* num;
	int size;
	int FIND(int) const;
public:
	ParPtrTree(int);
	~ParPtrTree() { delete[] array; }
	void UNION(int, int);		//�ϲ�
	bool differ(int, int);		//�ж�
};

ParPtrTree::ParPtrTree(int sz) {
	size = sz;
	array = new int[sz]; 
	num = new int[sz];
	for (int i = 0; i < sz; i++) {
		array[i] = ROOT;
		num[i] = 1;
	}
}

int ParPtrTree::FIND(int curr)const {
	sum++;
	if (array[curr] == ROOT) return curr;
	array[curr] = FIND(array[curr]);
	return array[curr];
}

bool ParPtrTree::differ(int a, int b) {
	int root1 = FIND(a);          
	int root2 = FIND(b);           
	return root1 != root2;        
}

void ParPtrTree::UNION(int a, int b) { 
	/*
	int root1 = FIND(a);        
	int root2 = FIND(b);       
	if (root1 != root2) array[root2] = root1; 
	*/

	int root1 = FIND(a);
	int root2 = FIND(b);
	if (root1 == root2) {
		return;
	}
	else {
		if (num[root2] > num[root1]) {
			array[root1] = root2;
			num[root2] += num[root1];
		}
		else {
			array[root2] = root1;
			num[root1] += num[root2];
		}
	}
}