#include <iostream>
#include "book.h"
#include "compare.h"
using namespace std;

//˳�����
template<typename E,typename Key,typename Comp,typename getKey>
int sequential(E array[], int n, Key K) {
	int i = 0;
	for (i = 0; i < n; i++) {
		if (Comp::eq(K, getKey::key(array[i]))) return i;
	}
	return -1;
}

void sequentialtest() {
	cout << "˳��������" << endl;
	int result;
	int arraysize = 100;
	int* bestarray = new int[arraysize];
	for (int i = 0; i < arraysize; i++)
	{
		bestarray[i] = i; // 0-99
	}
	// best (the first one)
	cout << "the best time"<<endl;
	int find = 0;
	comparisons = 0;
	result = sequential<int, int, intintCompare, getintKey>(bestarray, arraysize, find);
	cout << "����Ԫ�أ�";
	for (int i = 0; i < arraysize; i++)
	{
		cout << bestarray[i] << " ";
	}
	cout << endl;
	cout << "������Ԫ��Ϊ��" << find << endl;
	cout << "Ŀ��Ԫ����λ�ã�" << result << endl;
	cout << "comparisons: " << comparisons << endl;

	// worst (can't find)
	cout << "the worst time"<<endl;
	find = 999;
	comparisons = 0;
	result = sequential<int, int, intintCompare, getintKey>(bestarray, arraysize, find);
	cout << "����Ԫ�أ�";
	for (int i = 0; i < arraysize; i++)
	{
		cout << bestarray[i] << " ";
	}
	cout << endl;
	cout << "������Ԫ��Ϊ��" << find << endl;
	if (result == -1) {
		cout << "δ�ҵ�Ŀ��Ԫ��" << endl;
	}
	else {
		cout << "Ŀ��Ԫ����λ�ã�" << result << endl;
	}
	cout << "comparisons: " << comparisons << endl;

	// aver
	cout << "the aver time"<<endl;
	int times = 10;
	int sumcomps = 0;
	int* averarray = new int[arraysize];
	for (int i = 0; i < arraysize; i++)
	{
		averarray[i] = rand()%400; // 0-400
	}
	cout << "����Ԫ�أ�";
	for (int i = 0; i < arraysize; i++)
	{
		cout << averarray[i] << " ";
	}
	cout << endl;
	for (int j = 0; j < times; j++)
	{
		find = rand() % 200;
		comparisons = 0;
		result = sequential<int, int, intintCompare, getintKey>(averarray, arraysize, find);
		/*
		cout << "������Ԫ��Ϊ��" << find << endl;
		if (result == -1) {
			cout << "δ�ҵ�Ŀ��Ԫ��" << endl;
		}
		else {
			cout << "Ŀ��Ԫ����λ�ã�" << result << endl;
		}
		cout << "comparisons: " << comparisons << endl;
		*/
		sumcomps += comparisons;
	}
	cout << "avercomparisons: " << sumcomps/times << endl;
}
//���ּ���
template<typename Key, typename E, typename Comp, typename getKey>
int binary(E array[], int n, Key K) {
	int l = -1;
	int r = n;
	while (l + 1 != r) {
		int i = (l + r) / 2;
		if (Comp::eq(K, getKey::key(array[i]))) return i;
		else {
			if (Comp::lt(K, getKey::key(array[i]))) r = i;
			if (Comp::gt(K, getKey::key(array[i]))) l = i;
		}
	}
	return -1;
}

void binarytest()
{
	cout <<endl<< "���ּ��������" << endl;
	int result;
	int arraysize = 100;
	int* bestarray = new int[arraysize];
	for (int i = 0; i < arraysize; i++)
	{
		bestarray[i] = i; // 0-99
	}
	// best (the middle one)
	cout << "the best time" << endl;
	int find = 49;
	comparisons = 0;
	result = binary<int, int, intintCompare, getintKey>(bestarray, arraysize, find);
	cout << "����Ԫ�أ�";
	for (int i = 0; i < arraysize; i++)
	{
		cout << bestarray[i] << " ";
	}
	cout << endl;
	cout << "������Ԫ��Ϊ��" << find << endl;
	cout << "Ŀ��Ԫ����λ�ã�" << result << endl;
	cout << "comparisons: " << comparisons << endl;
	
	// worst (the worst one)
	cout << "the worst time" << endl;
	find = 999;
	comparisons = 0;
	result = binary<int, int, intintCompare, getintKey>(bestarray, arraysize, find);
	cout << "����Ԫ�أ�";
	for (int i = 0; i < arraysize; i++)
	{
		cout << bestarray[i] << " ";
	}
	cout << endl;
	cout << "������Ԫ��Ϊ��" << find << endl;
	if (result == -1) {
		cout << "δ�ҵ�Ŀ��Ԫ��" << endl;
	}
	else {
		cout << "Ŀ��Ԫ����λ�ã�" << result << endl;
	}
	cout << "comparisons: " << comparisons << endl;

	// aver
	cout << "the aver time" << endl;
	int times = 10;
	int sumcomps = 0;
	int* averarray = new int[arraysize];
	for (int i = 0; i < arraysize; i++)
	{
		averarray[i] = rand() % 400; // 0-400
	}
	cout << "����Ԫ�أ�";
	for (int i = 0; i < arraysize; i++)
	{
		cout << averarray[i] << " ";
	}
	cout << endl;
	for (int j = 0; j < times; j++)
	{
		find = rand() % 200;
		comparisons = 0;
		result = binary<int, int, intintCompare, getintKey>(averarray, arraysize, find);
		/*
		cout << "������Ԫ��Ϊ��" << find << endl;
		if (result == -1) {
			cout << "δ�ҵ�Ŀ��Ԫ��" << endl;
		}
		else {
			cout << "Ŀ��Ԫ����λ�ã�" << result << endl;
		}
		cout << "comparisons: " << comparisons << endl;
		sumcomps += comparisons;
		*/
	}
	cout << "avercomparisons: " << sumcomps / times << endl;
}
int main()
{
	sequentialtest();
	binarytest();
	return 0;
 }