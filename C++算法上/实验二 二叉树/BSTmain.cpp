#include <iostream>
#include "BST.h"
using namespace std;
int main()
{   //test
    BST<int, int> a;
    a.insert(40, 40);
    a.insert(20, 20);
    a.insert(8, 8);
    a.insert(20, 20);
    a.insert(10, 10);
    a.insert(0,0);
    a.insert(5,5);
    a.print();
    cout <<"5ֵ���ڵ�����λ�ǣ�" <<a.find(5)<<endl;
    cout << "Ŀǰ���Ĵ�С��" << a.size()<<endl;
    cout << "���нڵ���֮��:" << a.countsum() << endl;
    cout << "ɾ�����ֵ֮�����Ϊ��" << endl;
    a.removeAny();
    a.print();
    cout << "ɾ���ڵ�5֮�����Ϊ��" << endl;
    a.remove(5);
    a.print();
    a.clear();
    cout << "ɾ��������֮��" << endl;
    a.print();
    return 0;
}
/*
int main()
{
    BST<int, int> treeone;
    treeone.insert(11,11);
    treeone.insert(32,32);
    treeone.insert(3,3);
    treeone.insert(34,34);
    treeone.insert(25,25);
    treeone.insert(16,16);
    treeone.insert(7,7);
    treeone.print();
    cout<<"���нڵ���֮��"<<treeone.countsum();
}
*/