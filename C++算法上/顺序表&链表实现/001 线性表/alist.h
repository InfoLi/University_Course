#pragma once
#ifndef alist_H
#define alist_H
//顺序表实现
#include <iostream>
#include <assert.h>
#include "list.h"
using namespace std;
template <typename E>                 //模板类
class Alist : public List<E> {
private:
	int maxSize;
	int listSize;
	int curr;
	E* listArray;
	void moveToEnd() { curr = listSize; }  //前往表尾
public:
	Alist(int size = 1000) {            //初始化给定表长度
		maxSize = size;
		listSize = curr = 0;
		listArray = new E[maxSize];
	}
	~Alist() { delete[] listArray; }

	void clear() {                     //清空整个表
		delete []  listArray;
		listSize = curr = 0;
		listArray = new E[maxSize];
	}

	void insert(const E& it) {         //插入元素
		assert(listSize < maxSize, "List capacity exceeded");
		for (int i = listSize; i > curr; i--)
			listArray[i] = listArray[i - 1];
		listArray[curr] = it;
		listSize++;
	}

	void append(const E& it) {         //表尾插入元素（不改变当前位置
		assert(listSize < maxSize, "List capacity exceeded");
		listArray[listSize++] = it;
	}

	E remove() {                       //删除当前位置元素
		assert((curr >= 0) && (curr < listSize), "No element");
		E it = listArray[curr];
		for (int i = curr; i < listSize - 1; i++)
			listArray[i] = listArray[i + 1];
		listSize--;
		return it;
	}
	void moveToStart() { curr = 0; }   //返回表头
	void prev() { if (curr != 0) curr--; }   //当前位置向前移一位
	void next() { if (curr < listSize) curr++; }  //当前位置向后移一位

	int length() const { return listSize; }  //返回长度
	int currPos() const { return curr; }     //返回当前的位置

	void moveToPos(int pos) {                //前往输入的位置
		assert((pos >= 0) && (pos <= listSize), "Pos out of range");
		curr = pos;
	}
	const E& getValue() const {             //返回当前位置的元素
		assert((curr >= 0) && (curr < listSize), "No current element");
		return listArray[curr];
	}

	void showall() {                        //输出表的所有元素
		for (int i = 0; i < listSize; i++)
			cout << listArray[i] << " ";
	}
};
#endif
