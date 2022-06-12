#pragma once
#ifndef _queue_H
#define _queue_H
#include <iostream>
#include <assert.h>
using namespace std;

//队列
template <typename E> class Queue {
private:
	void operator =( const Queue& ) {}
	Queue(const Queue&) {}
public:
	Queue() {}
	virtual ~Queue() {};
	virtual void clear() = 0;
	virtual void enqueue(const E&) = 0;
	virtual E dequeue() = 0;
	virtual const E& frontValue() const = 0;
	virtual int length() const = 0;
};

//单链表节点类
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