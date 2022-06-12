#pragma once
#include "book.h"
// ͼ�Ķ���
class Graph {
private:
	void operator =(const Graph&) {}
	Graph(const Graph&) {}
public:
	Graph() {}
	virtual ~Graph() {}

	virtual void Init(int n) = 0; //����n���ڵ��ͼ

	virtual int n() = 0;
	virtual int e() = 0;

	virtual int first(int v) = 0;  //���ؽڵ�ĵ�һ���ھ�
	virtual int next(int v, int w) = 0; //���ؽڵ����һ���ھ�

	virtual void setEdge(int v1, int v2, int wght) = 0; //����ߵ�Ȩ��

	virtual void delEdge(int v1, int v2) = 0; //ɾ����

	virtual bool isEdge(int i, int j) = 0; //�жϱ�

	virtual int weight(int v1, int v2) = 0; //���رߵ�Ȩ��

	virtual int getMark(int v) = 0; // ����Mark����洢�ߵ�Ȩ��
	virtual void setMark(int v, int val) = 0;
};