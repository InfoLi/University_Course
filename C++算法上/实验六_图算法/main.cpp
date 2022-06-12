#include <iostream>
#include "graph.h"
#include "Graphm.h"
#include "linked queue.h"
using namespace std;

// UNVISTIED = 0
// VISITED = 1

// ������ȱ����㷨
void PreVisit(Graphm* G,int  v) {
	cout << "->" << (v+1);
}

void DFS(Graphm* G, int v) {
	PreVisit(G, v);
	G->setMark(v, 1);
	for (int w = G->first(v); w < G->n(); w = G->next(v, w))
	{
		if (G->getMark(w) == 0)
		{
			DFS(G, w);
		}
	}
	// PostVisit(G, v);
}

// ͼ��������ȱ�������
void DFSgraphTraverse(Graphm* G) {
	cout << "������ȱ������˳��Ϊ:";
	int v;
	for (v = 0; v < G->n(); v++)
	{
		G->setMark(v, 0);
	}
	for (v = 0; v < G->n(); v++)
	{
		if (G->getMark(v) == 0)
			DFS(G, v);				//����һ����������
	}
}

//������ȱ����㷨
void BFS(Graphm* G,int start, LQueue<int>* Q) {
	int v, w;
	Q->enqueue(start);
	G->setMark(start, 1);
	while (Q->length() != 0) {
		v = Q->dequeue();
		PreVisit(G, v);
		for (w = G->first(v); w < G->n(); w = G->next(v, w))
			if (G->getMark(w) == 0)
			{
				G->setMark(w, 1);
				Q->enqueue(w);
			}
	}
}

// ͼ�Ĺ�����ȱ�������
void BFSgraphTraverse(Graphm* G) {
	LQueue<int> Q;
	cout << "������ȱ������˳��Ϊ:";
	int v;
	for (v = 0; v < G->n(); v++)
	{
		G->setMark(v, 0);
	}
	for (v = 0; v < G->n(); v++)
	{
		if (G->getMark(v) == 0)
			BFS(G, v,&Q);				//����һ����������
	}
}

//�ݹ��������� 
void tophelp(Graphm* G, int v) {
	G->setMark(v, 1);
	for (int w = G->first(v); w < G->n(); w = G->next(v, w))
		if (G->getMark(w) == 0)
			tophelp(G, w);
	cout<<"->"<<(v+1);
}

void topsort(Graphm* G) {
	int i;
	for (i = 0; i < G->n(); i++)
		G->setMark(i, 0);
	for (i = 0; i < G->n(); i++)
		if (G->getMark(i) == 0)
			tophelp(G, i);
}

// ��Դ���·��
int minVertex(Graphm* G, int* D) {
	int i, v;
	for (i = 0; i < G->n(); i++) {
		if (G->getMark(i) == 0) {
			v = i;
			break; }
	}
	for (i++; i < G->n(); i++)
	{
		if ((G->getMark(i) == 0) && (D[i] < D[v]))
			v = i;
	}
	return v;
}

void Dijkstra(Graphm* G, int* D, int v) {
	D[v] = 0;
	for (int i = 0; i < G->n(); i++) {
		v = minVertex(G, D);
		if (D[v] == INFINITY)return;
		G->setMark(v, 1);
		for (int w = G->first(v); w < G->n(); w = G->next(v, w)) {
			if (D[w] > (D[v] + G->weight(v, w)))
				D[w] = D[v] + G->weight(v, w);
		}
	}
}

// ���������Ż�
void topsort2(Graphm* G, LQueue<int>* Q) {
	int* Count = new int[G->n()];
	int v, w;
	for (v = 0; v < G->n(); v++) Count[v] = 0;
	for (v = 0; v < G->n(); v++)
		for (w = G->first(v); w < G->n(); w = G->next(v, w))
			Count[w]++;
	for (v = 0; v < G->n(); v++)
		if (Count[v] == 0) {
			Q->enqueue(v);
			G->setMark(v,1);
		}
	while (Q->length() != 0) {
		v = Q->dequeue();
		cout << v;
		for (w = G->first(v); w < G->n(); w = G->next(v, w)) {
			Count[w]--;
			if (Count[w] == 0)
				Q->enqueue(w);
				G->setMark(w, 1);
		}
	}
	for (int i = 1; i < G->n(); i++) {
		if (G->getMark(i) == 0) {
			cout << endl << "���ڻ�·";
		}
	}
}

int main() {
	
	Graphm a(6);
	a.setEdge(0, 1, 10);a.setEdge(1, 0, 10);
	a.setEdge(0, 3, 20); a.setEdge(3, 0, 20);
	a.setEdge(1, 3, 5); a.setEdge(3, 1, 5);
	a.setEdge(0, 5, 2); a.setEdge(5, 0, 2);
	a.setEdge(1, 2, 3); a.setEdge(2, 1, 3);
	a.setEdge(5, 3, 10); a.setEdge(3, 5, 10);
	a.setEdge(5, 4, 11); a.setEdge(4, 5, 11);
	a.setEdge(5, 4, 3); a.setEdge(4, 5, 3);
	a.setEdge(2, 4, 15); a.setEdge(4, 2, 15);
	a.showmatrix();
	/*
	cout << endl;
	DFSgraphTraverse(&a);
	cout <<'\n'<< endl;
	BFSgraphTraverse(&a);
	cout << '\n' << endl<<"������������";
	topsort(&a);
	*/
	cout << '\n' << endl;
	int D[6] = { INFINITY , INFINITY , INFINITY , INFINITY , INFINITY , INFINITY };
	Dijkstra(&a, D,0);
	cout << "�ӵ�1��������̵�Դ·����";
	for (int i = 0; i < 6; i++)
	{
		cout << D[i]<<'\t';
	}
	/*
	Graphm b(4);
	LQueue<int> Q;
	b.setEdge(0, 1, 1);
	b.setEdge(1, 2, 1);
	b.setEdge(2, 3, 1);
	b.setEdge(3, 0, 1);
	b.showmatrix();
	topsort2(&b, &Q);
	*/
}