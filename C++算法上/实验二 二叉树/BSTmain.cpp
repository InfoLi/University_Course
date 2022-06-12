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
    cout <<"5值所在的索引位是：" <<a.find(5)<<endl;
    cout << "目前树的大小：" << a.size()<<endl;
    cout << "所有节点数之和:" << a.countsum() << endl;
    cout << "删除最大值之后的树为：" << endl;
    a.removeAny();
    a.print();
    cout << "删除节点5之后的树为：" << endl;
    a.remove(5);
    a.print();
    a.clear();
    cout << "删除整个树之后" << endl;
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
    cout<<"所有节点数之和"<<treeone.countsum();
}
*/