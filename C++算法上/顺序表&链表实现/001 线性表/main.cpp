#include <iostream>
#include "alist.h"
#include "link list.h"
using namespace std;
/*  Ë³Ðò±í
int main()
{
	Alist <int> a;
	a.append(4); a.append(3); a.append(2); a.append(1);a.append(0); // 4(curr) 3 2 1 0 
	a.showall(); cout << endl;
	cout << "curr:" << a.getValue() << endl; 
	a.next(); //4 3(curr) 2 1 0
	cout << "curr:" << a.getValue() << endl;
	a.insert(6);   // 4 6(curr) 3 2 1 0
	cout << "curr:" << a.getValue() << endl;
	a.prev();  //4(curr) 6 3 2 1 0
	a.remove(); // 6 3 2 1 0
	a.showall();
	return 0;
}
*/

int main()
{
	LList <int> b;
	b.append(5); b.append(6); b.append(7); b.append(8);  //5(curr) 6 7 8
	cout << "curr:" << b.getValue() << endl;
	b.next(); // 5 6(curr) 7 8
	cout << "curr:" << b.getValue() << endl;
	b.remove(); // 5 7(curr) 8
	cout << "curr:" << b.getValue() << endl;
}