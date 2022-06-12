#pragma once
#ifndef _array based stack_h_
#define _array based stack_h_
#include <iostream>
#include <assert.h>
#include "Stack.h"
using namespace std;

// ˳��ջ
template <typename E> class AStack :public Stack<E> {
private:
	int maxSize;
	int top;
	E* listArray;
public:
	AStack(int size = 10000000)
	{
		maxSize = size; top = 0; listArray = new E[size];
	}
	~AStack() { delete[] listArray; }
	void clear() { top = 0; }
	void push(const E& it) {                          //����Ԫ��
		assert(top != maxSize, "Stack is full");
		listArray[top++] = it;
	}
	E pop() {                                         //ɾ��Ԫ��
		assert(top != 0, "Stack is empty");
		return listArray[--top];
	}
	const E& topValue() const {                       //���ص�ǰջ����Ԫ��
		assert(top != 0, "Stack is empty");
		return listArray[top - 1];
	}
	int length() const { return top; }
};
#endif
