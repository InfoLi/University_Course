#pragma once
#ifndef alist_H
#define alist_H
//˳���ʵ��
#include <iostream>
#include <assert.h>
#include "list.h"
using namespace std;
template <typename E>                 //ģ����
class Alist : public List<E> {
private:
	int maxSize;
	int listSize;
	int curr;
	E* listArray;
	void moveToEnd() { curr = listSize; }  //ǰ����β
public:
	Alist(int size = 1000) {            //��ʼ����������
		maxSize = size;
		listSize = curr = 0;
		listArray = new E[maxSize];
	}
	~Alist() { delete[] listArray; }

	void clear() {                     //���������
		delete []  listArray;
		listSize = curr = 0;
		listArray = new E[maxSize];
	}

	void insert(const E& it) {         //����Ԫ��
		assert(listSize < maxSize, "List capacity exceeded");
		for (int i = listSize; i > curr; i--)
			listArray[i] = listArray[i - 1];
		listArray[curr] = it;
		listSize++;
	}

	void append(const E& it) {         //��β����Ԫ�أ����ı䵱ǰλ��
		assert(listSize < maxSize, "List capacity exceeded");
		listArray[listSize++] = it;
	}

	E remove() {                       //ɾ����ǰλ��Ԫ��
		assert((curr >= 0) && (curr < listSize), "No element");
		E it = listArray[curr];
		for (int i = curr; i < listSize - 1; i++)
			listArray[i] = listArray[i + 1];
		listSize--;
		return it;
	}
	void moveToStart() { curr = 0; }   //���ر�ͷ
	void prev() { if (curr != 0) curr--; }   //��ǰλ����ǰ��һλ
	void next() { if (curr < listSize) curr++; }  //��ǰλ�������һλ

	int length() const { return listSize; }  //���س���
	int currPos() const { return curr; }     //���ص�ǰ��λ��

	void moveToPos(int pos) {                //ǰ�������λ��
		assert((pos >= 0) && (pos <= listSize), "Pos out of range");
		curr = pos;
	}
	const E& getValue() const {             //���ص�ǰλ�õ�Ԫ��
		assert((curr >= 0) && (curr < listSize), "No current element");
		return listArray[curr];
	}

	void showall() {                        //����������Ԫ��
		for (int i = 0; i < listSize; i++)
			cout << listArray[i] << " ";
	}
};
#endif
