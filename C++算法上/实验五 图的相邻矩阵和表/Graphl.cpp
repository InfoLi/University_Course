#include <iostream>
#include <iomanip>
#include "graph.h"
#include "list.h"
#include "link list.h"
using namespace std;
class Edge {	//´¢´æÁ´±í
	int vert, wt;
public:
	Edge() { vert = -1; wt = -1; }
	Edge(int v, int w) { vert = v; wt = w; }
	int vertex() { return vert; }
	int weight() { return wt; }
};
class Graphl : public Graph {
private:
	List<Edge>** vertex;	//Á´±í¾ØÕó 
	int numVertex, numEdge;
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
		mark = new int[n];
		for (i = 0; i < numVertex; i++) mark[i] = 0;
		vertex = (List<Edge>**) new List<Edge> * [numVertex];
		for (i = 0; i < numVertex; i++)
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
		Assert(weight > 0, "May not set weight to 0");
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

	int getMark(int v) { return mark[v]; }
	void setMark(int v, int val) { mark[v] = val; }
};

int main()
{
	Graphl a(6);
	a.setEdge(0, 1, 10);
	a.setEdge(0, 3, 20);
	a.setEdge(1, 3, 5);
	a.setEdge(0, 5, 3);
	a.setEdge(1, 2, 3);
	a.setEdge(5, 3, 10);
	a.setEdge(5, 4, 11);
	a.setEdge(5, 4, 3);
	a.setEdge(2, 4, 15);
	return 0;
}