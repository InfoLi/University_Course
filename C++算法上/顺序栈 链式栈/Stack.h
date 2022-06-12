#pragma once
#ifndef _ stack_h_
#define _ stack_h_
#include <iostream>
#include <assert.h>
using namespace std;
// 栈
template <typename E> class Stack {
private:
	void operator = (const Stack&) {}
	Stack(const Stack&) {}
public:
	Stack() {}
	virtual ~Stack() {}

	virtual void clear() = 0;
	virtual void push(const E& it) = 0;
	virtual E pop() = 0;
	virtual const E& topValue() const = 0;
	virtual int length() const = 0;
};

//单链表节点
template <typename E> class Link {
public:
	E element;
	Link* next;
	Link(const E& elemval, Link* nextval = NULL)
	{
		element = elemval; next = nextval;
	}
	Link(Link* nextval = NULL) { next = nextval; }
};
#endif
