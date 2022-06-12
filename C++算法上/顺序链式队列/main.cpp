#include <iostream>
#include "array based queue.h"
#include "linked queue.h"
using namespace std;
int main()
{/*
	AQueue<int> a;
	a.enqueue(20);
	a.enqueue(10); //20 10
	cout << a.length() << endl;
	cout << a.frontValue() << endl;
	a.dequeue();
	cout << a.frontValue() << endl;
	*/
	LQueue<int> b;
	b.enqueue(20);
	b.enqueue(10); //20 10
	cout << b.length() << endl;
	cout << b.frontValue() << endl;
	b.dequeue();
	cout << b.frontValue() << endl;
}