#include<iostream>
#include <time.h> 
#include<vector>
using namespace std;
struct level
{
    level** next;
    int value;
};
int randLevel() {
    srand((unsigned)time(NULL));
    double n = rand() % 20 + 1;
    
    int sum = 1;

    while (n>10)
    {
        sum++;
        n = rand() % 20 + 1;
    }

    return sum;
}
template<class T>
int length(T& arr)
{;
    return sizeof(arr) / sizeof(arr[0]);
}
class SkipList {
private:
    int size;
    level head;
    level *temp;
    void insertHelp();
public:
    SkipList();
    ~SkipList();
    void add(int value);
    void print() {
            temp = head.next[0];
            while (temp!=0)
            {
                cout << temp->value << " ";
                temp = temp->next[0];
            }
            cout << endl;
    }
    bool remove(int value);
    bool find(int value);
};

SkipList::SkipList() {
    int len = randLevel();
    head.next = new level*[len];
    for (int i = 0; i < len; i++)
    {
        head.next[i] = NULL;
    }
    size = 0;
}
SkipList::~SkipList() {
    temp = head.next[0];
    level* t = temp->next[0];

    for (int i = 0; i < size-1; i++)
    {
        delete temp->next;
        delete temp;

        temp = t;
        t = temp->next[0];
    }
    size = 0;
}
void SkipList::insertHelp() {
    level* t;

    int m = length(temp->next);
    level** array = new level * [m];

    int n = length(head.next);
    for (int i = 1; i <= n; i++)
    {
        t = &head;
        while (t->next[n - i] != NULL)
        {
            if (t->next[n - i]->value < temp->value)
                break;
            else
                t = t->next[n - i];
        }
        if (n - i < m)
            array[n - i] = t;
    }

    for (int i = 0; i < m; i++)
    {
        temp->next[i] = array[i]->next[i];
        array[i]->next[i] = temp;
    }
}
void SkipList::add(int value) {
    int len = randLevel();
    temp = new level;
    temp->next = new level* [len];
    for (int i = 0; i < len; i++)
        temp->next[i] = NULL;
    temp->value = value;
    size++;
    if (length(head.next) < len)
    {
        level t;
        t.next = new level * [length(head.next)];
        for (int i = 0; i < length(head.next); i++)
        {
            t.next[i] = head.next[i];
            t.next = head.next;
        }
        head.next = new level * [len];
        for (int i = 0; i < length(head.next); i++)
            head.next[i] = t.next[i];
        for (int i = length(head.next);i<len; i++)
        {
            head.next[i] = NULL;
        }
    }
    insertHelp();
}
bool SkipList::remove(int value) {
    if (size == 0)
    {
        return false;
    }
    level* t;
    int m = length(head.next);
    level** array = new level * [m];
    int n = length(head.next);
    for (int i = 1; i <= n; i++)
    {
        t = &head;
        while (t->next[n - i] != NULL)
        {
            if (t->next[n - i]->value <= value)               
                break;           
            else
                t = t->next[n - i];
        }
        if (n - i < m)
            array[n - i] = t;
    }
    if (array[0]->next[0]->value != value)
    {
        return false;
    }
    t = array[0]->next[0];  
    for (int i = 0; i < length(t->next); i++)
        array[i]->next[i] = t->next[i];
    delete[]t->next;
    delete t;
    size--;
    return true;
}
bool SkipList::find(int value) {
    if (size == 0)
    {
        return false;
    }
    level* t;
    int m = length(head.next);
    level** array = new level * [m];
    int n = length(head.next);
    for (int i = 1; i <= n; i++)
    {
        t = &head;
        while (t->next[n - i] != NULL)
        {
            if (t->next[n - i]->value <= value)           
                break;
            else
                t = t->next[n - i];
        }
        if (n - i < m)
            array[n - i] = t;
    }
    if (array[0]->next[0]->value != value)
    {
        return false;
    }
    return true;
}

int main() {
    SkipList sk;
    
    sk.add(1);
    sk.add(87);
    sk.add(24);
    sk.add(19);
    sk.add(48);
    sk.add(33);
    sk.add(14);
    sk.add(60);
    sk.add(19);
    sk.add(13);
    sk.print();

    cout<<"find 14:"<<sk.find(14)<<endl;

    sk.remove(14);
    sk.print();

    return 0;
}