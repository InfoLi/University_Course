#include <iostream>
#include "array based stack.h"
#include "linked stack.h"
using namespace std;
int main()
{
	/*
	AStack<int> a;
	a.push(10);
	a.push(20);         // 20 10
	cout << a.length()<<endl;
	cout << a.topValue() << endl;
	a.pop();  // 10
	cout << a.topValue();
	return 0;
	*/

	LStack<int> b;
	b.push(1);
	b.push(0);      // 0 1
	cout << b.topValue() << endl;
	b.pop();
	cout << b.topValue() << endl;



}