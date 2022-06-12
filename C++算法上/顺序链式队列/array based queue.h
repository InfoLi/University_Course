#pragma once
#ifndef _array based queue_H
#define _array based queue_H
#include <iostream>
#include <assert.h>
#include "queue.h"
using namespace std;
template <typename E> class AQueue : public Queue<E> {
private:
	int maxSize;
	int front;
	int rear;
	E* listArray;
public:
	AQueue(int size = 100000) {
		maxSize = size + 1;
		rear = 0; front = 1;
		listArray = new E[maxSize];
	}
	~AQueue() { delete[] listArray; }

	void clear() { rear = 0; front = 1; }
	void enqueue(const E& it) {    //入队
		assert(((rear + 2) % maxSize) != front, "Queue is full");
		rear = (rear + 1) % maxSize;
		listArray[rear] = it;
	}
	E dequeue() {                  //出队
		assert(length() != 0, "Queue is empty");
		E it = listArray[front];
		front = (front + 1) % maxSize;
		return it;
	}
	const E& frontValue() const {       //队首元素 
		assert(length() != 0, "Queue is empty");
		return listArray[front];
	}
	virtual int length () const
	{
		return((rear + maxSize) - front + 1) % maxSize;         
	}
};
#endif 