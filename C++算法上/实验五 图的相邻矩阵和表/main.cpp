#include <iostream>
#include <iomanip>
#include "graph.h"
#include "list.h"
#include "link list.h"
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
		adjacency_matrix[v1][v2] = 1;
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
		cout << "Ȩ�ر�" << endl;
		for (int i = 0; i < numVertex; i++)
		{
			for (int j = 0; j < numVertex; j++)
				cout << setw(4) << matrix[i][j] << "  ";
			cout << endl;
		}
		cout << "���ھ���" << endl;
		for (int i = 0; i < numVertex; i++)
		{
			for (int j = 0; j < numVertex; j++)
				cout << setw(4) << adjacency_matrix[i][j] << "  ";
			cout << endl;
		}
	}
};

//��������
class Edge {	
	int vert, wt;
public:
	Edge() { vert = -1; wt = -1; }
	Edge(int v, int w) { vert = v; wt = w; }
	int vertex() { return vert; }
	int weight() { return wt; }
};
//�ڽӱ��ʵ��
class Graphl : public Graph {
private:
	List<Edge>** vertex;	//������� 
	int numVertex, numEdge; //�ߣ�����
	int* mark;
public:
	Graphl(int numVert)
	{
		Init(numVert);
	}

	~Graphl()
	{
		delete[] mark;
		for (int i = 0; i < numVertex; i++) delete[] vertex[i];
		delete[] vertex;
	}

	void Init(int n) {
		int i;
		numVertex = n;
		numEdge = 0;
		mark = new int[n]; //��Ǿ���
		for (i = 0; i < numVertex; i++) mark[i] = 0;
		vertex = (List<Edge>**) new List<Edge> * [numVertex];
		for (i = 0; i < numVertex; i++)  //�ڽӱ�����ʼ��
			vertex[i] = new LList<Edge>();
	}

	int n() { return numVertex; }
	int e() { return numEdge; }

	int first(int v) {
		if (vertex[v]->length() == 0)
			return numVertex;
		vertex[v]->moveToStart();
		Edge it = vertex[v]->getValue();
		return it.vertex();
	}

	int next(int v, int w) {
		Edge it;
		if (isEdge(v, w)) {
			if ((vertex[v]->currPos() + 1) < vertex[v]->length()) {
				vertex[v]->next();
				it = vertex[v]->getValue();
				return it.vertex();
			}
		}
		return n();
	}

	void setEdge(int i, int j, int weight) {
		Assert(weight > 0, "Ȩ�ز���С����");
		Edge currEdge(j, weight);
		if (isEdge(i, j))
		{
			vertex[i]->remove();
			vertex[i]->insert(currEdge);
		}
		else {
			numEdge++;
			for (vertex[i]->moveToStart();
				vertex[i]->currPos() < vertex[i]->length();
				vertex[i]->next()) {
				Edge temp = vertex[i]->getValue();
				if (temp.vertex() > j) break;
			}
			vertex[i]->insert(currEdge);
		}
	}

	void delEdge(int i, int j) {
		if (isEdge(i, j)) {
			vertex[i]->remove();
			numEdge--;
		}
	}

	bool isEdge(int i, int j) {
		Edge it;
		for (vertex[i]->moveToStart();
			vertex[i]->currPos() < vertex[i]->length();
			vertex[i]->next()) {
			Edge temp = vertex[i]->getValue();
			if (temp.vertex() == j) return true;
		}
		return false;
	}

	int weight(int i, int j) {
		Edge curr;
		if (isEdge(i, j)) {
			curr = vertex[i]->getValue();
			return curr.weight();
		}
		else return 0;
	}

	void showmvertex()  //�������
	{
		cout << "�ڽ�Ȩ�ر�" << endl;
		for (int i = 0; i < numVertex; i++)
		{
			cout << i;
			for (int j = 0; j < numVertex; j++)
				if (weight(i, j) != 0)
				{
					cout<<"->"<<j<<":" <<weight(i, j);
				}
			cout << endl;
		}
	}
	int getMark(int v) { return mark[v]; }
	void setMark(int v, int val) { mark[v] = val; }
};

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
	Graphl b(6);
	b.setEdge(0, 1, 10);
	b.setEdge(0, 3, 20);
	b.setEdge(1, 3, 5);
	b.setEdge(0, 5, 3);
	b.setEdge(1, 2, 3);
	b.setEdge(5, 3, 10);
	b.setEdge(5, 4, 11);
	b.setEdge(5, 4, 3);
	b.setEdge(2, 4, 15);
	b.showmvertex();
	return 0;
}