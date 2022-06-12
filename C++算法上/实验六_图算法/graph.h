#pragma once
#include "book.h"
// 图的定义
class Graph {
private:
	void operator =(const Graph&) {}
	Graph(const Graph&) {}
public:
	Graph() {}
	virtual ~Graph() {}

	virtual void Init(int n) = 0; //定义n个节点的图

	virtual int n() = 0;
	virtual int e() = 0;

	virtual int first(int v) = 0;  //返回节点的第一个邻居
	virtual int next(int v, int w) = 0; //返回节点的下一个邻居

	virtual void setEdge(int v1, int v2, int wght) = 0; //定义边的权重

	virtual void delEdge(int v1, int v2) = 0; //删除边

	virtual bool isEdge(int i, int j) = 0; //判断边

	virtual int weight(int v1, int v2) = 0; //返回边的权重

	virtual int getMark(int v) = 0; // 利用Mark数组存储边的权重
	virtual void setMark(int v, int val) = 0;
};