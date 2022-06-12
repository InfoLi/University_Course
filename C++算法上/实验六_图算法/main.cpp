#include <iostream>
#include "graph.h"
#include "Graphm.h"
#include "linked queue.h"
using namespace std;

// UNVISTIED = 0
// VISITED = 1

// 深度优先遍历算法
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

// 图的深度优先遍历函数
void DFSgraphTraverse(Graphm* G) {
	cout << "深度优先遍历点的顺序为:";
	int v;
	for (v = 0; v < G->n(); v++)
	{
		G->setMark(v, 0);
	}
	for (v = 0; v < G->n(); v++)
	{
		if (G->getMark(v) == 0)
			DFS(G, v);				//任意一个遍历函数
	}
}

//广度优先遍历算法
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

// 图的广度优先遍历函数
void BFSgraphTraverse(Graphm* G) {
	LQueue<int> Q;
	cout << "广度优先遍历点的顺序为:";
	int v;
	for (v = 0; v < G->n(); v++)
	{
		G->setMark(v, 0);
	}
	for (v = 0; v < G->n(); v++)
	{
		if (G->getMark(v) == 0)
			BFS(G, v,&Q);				//任意一个遍历函数
	}
}

//递归拓扑排序 
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

// 单源最短路径
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

// 拓扑排序优化
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
			cout << endl << "存在回路";
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
	cout << '\n' << endl<<"拓扑排序逆序：";
	topsort(&a);
	*/
	cout << '\n' << endl;
	int D[6] = { INFINITY , INFINITY , INFINITY , INFINITY , INFINITY , INFINITY };
	Dijkstra(&a, D,0);
	cout << "从点1出发的最短单源路径：";
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