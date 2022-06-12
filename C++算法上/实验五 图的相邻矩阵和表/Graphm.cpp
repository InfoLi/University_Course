#include <iostream>
#include <iomanip>
#include "graph.h"
using namespace std;
// ���ھ���ʵ��
class Graphm :public Graph {
private:
	int numVertex, numEdge; //����������
	int** matrix; //ָ�����ھ�������
	int** adjacency_matrix;
	int* mark;    //ָ�� mark����
public:
	Graphm(int numVert)
	{
		Init(numVert);
	}

	~Graphm() {
		delete[] mark;
		for (int i = 0; i < numVertex; i++)
			delete[] matrix[i];
		delete[] matrix;
	}

	void Init(int n) { //����Ĺ���
		int i;
		numVertex = n;
		numEdge = 0;
		mark = new int[n];
		for (i = 0; i < numVertex; i++)
			mark[i] = 0;
		matrix = (int**) new int* [numVertex];
		adjacency_matrix = (int**) new int* [numVertex];
		for (i = 0; i < numVertex; i++)
		{
			matrix[i] = new int[numVertex];
			adjacency_matrix[i] = new int[numVertex];
		}
		for (i = 0; i < numVertex; i++)
			for (int j = 0; j < numVertex; j++)
			{
				matrix[i][j] = 0;
				adjacency_matrix[i][j] = 0;
			}
	}

	int n() { return numVertex; } //��ĸ���
	int e() { return numEdge; }  //�ߵĸ���
	//����ʵ��
	int first(int v) { 
		for (int i = 0; i < numVertex; i++)
			if (matrix[v][i] != 0) return i;
		return numVertex;
	}

	int next(int v, int w) {
		for (int i = w + 1; i < numVertex; i++)
			if (matrix[v][i] != 0)
				return i;
		return numVertex;
	}

	void setEdge(int v1, int v2, int wt) {
		Assert(wt > 0, "��Ч�ı�Ȩֵ");
		if (matrix[v1][v2] == 0) numEdge++;
		matrix[v1][v2] = wt;
		adjacency_matrix[v1][v2] =1;
	}

	void delEdge(int v1, int v2) {
		if (matrix[v1][v2] != 0) numEdge--;
		matrix[v1][v2] = 0;
	}

	bool isEdge(int i, int j)
	{
		return matrix[i][j] != 0;
	}

	int weight(int v1, int v2) { return matrix[v1][v2]; }
	int getMark(int v) { return mark[v]; }
	void setMark(int v, int val) { mark[v] = val; }

	void showmatrix()  //�������
	{
		cout << "Ȩ�ر�"<<endl;
		for (int i = 0; i < numVertex; i++) 
		{
			for (int j = 0; j < numVertex; j++)
				cout << setw(4) <<matrix[i][j]<<"  ";
			cout << endl;
		}
		cout << "���ھ���"<<endl;
		for (int i = 0; i < numVertex; i++)
		{
			for (int j = 0; j < numVertex; j++)
				cout << setw(4) << adjacency_matrix[i][j] << "  ";
			cout << endl;
		}
	}
};
// test
/*
int main()
{
	Graphm a(6);
	a.setEdge(0, 1, 10);
	a.setEdge(0, 3, 20);
	a.setEdge(1, 3, 5);
	a.setEdge(0, 5, 3);
	a.setEdge(1, 2, 3);
	a.setEdge(5, 3, 10);
	a.setEdge(5, 4, 11);
	a.setEdge(5, 4, 3);
	a.setEdge(2, 4, 15);
	a.showmatrix();
	return 0;
}
*/