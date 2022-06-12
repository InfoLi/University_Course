#include<iostream>
#include<stdlib.h>
#include"compare.h"
#include"heap.h"
#include<ctime>
#include<Windows.h>
using namespace std;

template <typename E,typename Comp>
void heapsort(E A[], int n) {
	E maxval;
	heap<E, Comp> H(A, n, n);
	for (int i = 0; i < n; i++)
		maxval = H.removefirst();
}
void heapsort(int n) {
	LARGE_INTEGER freq_;
	QueryPerformanceFrequency(&freq_);
	LARGE_INTEGER begin_time;
	LARGE_INTEGER end_time;
	double ns_time;

	//best
	int* bestArraydata = new int[100000];
	for (int i = 0; i < n; i++) {
		bestArraydata[i] = i;
	}
	cout << "the best situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	heapsort<int, minintCompare>(bestArraydata, n);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	delete[]bestArraydata;

	//worst
	int* worstArraydata = new int[100000];
	for (int i = 0; i < n; i++) {
		worstArraydata[i] = n - i - 1;
	}
	cout << "the worst situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	heapsort<int, minintCompare>(worstArraydata,n);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	delete[]worstArraydata;

	//aver
	int number = 10; //取10次平均
	double sum_time = 0;
	for (int j = 0; j < number; j++)
	{
		int* averArraydata = new int[100000]; //存放数组
		for (int i = 0; i < n; i++) {
			int temp = rand() % 100; //1-100取随机数
			averArraydata[i] = temp;
		}
		QueryPerformanceCounter(&begin_time);
		heapsort<int, minintCompare>(averArraydata, n);
		QueryPerformanceCounter(&end_time);
		ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
		sum_time = sum_time + ns_time;
		/* test
		cout << "swap" << a[0] << "somp" << a[1] << endl;
		cout << "sumtime" << sum_time << endl;
		for (int k = 0; k < n; k++)
		{
			cout << averArraydata[k] << " ";
		}
		cout << j << endl;
		*/
	}
	cout << "the aver situation n=" << n << endl;
	cout << "time use=" << sum_time / number << "ms" << endl;
}
/*
int main()
{
	heapsort(10);
	heapsort(100);
	heapsort(1000);
	heapsort(10000);
	heapsort(100000);
}
*/