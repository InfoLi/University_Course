#pragma once
#ifndef _linked stack_h_
#define _linked stack_h_
#include <iostream>
#include <assert.h>
#include "Stack.h"
using namespace std;
template <typename E> class LStack : public Stack<E> {
private:
	Link<E>* top;
	int size;
public:
	LStack(int sz = 100000)
	{
		top = NULL; size = 0;
	}
	~LStack() { clear(); }
		void clear() {
		while (top != NULL) {
			Link<E>* temp = top;
			top = top->next;
			delete temp;
		}
		size = 0;
	}
	void push(const E& it) {
		top = new Link<E>{ it,top };
		size++;
	}
	E pop() {
		assert(top != NULL, "Stack is empty");
		E it = top->element;
		Link<E>* ltemp = top->next;
		delete top;
		top = ltemp;
		size--;
		return it;
	}

	const E& topValue() const {
		assert(top != 0, "Stack is empty");
		return top->element;
}
	int length() const { return size; }
};

#endif