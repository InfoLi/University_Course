#include<iostream>
#include<stdlib.h>
#include"compare.h"
#include<ctime>
#include<Windows.h>
using namespace std;

template <typename E, typename Comp>
inline int partition(E A[], int l, int r, E& pivot) {
	do {
		while (Comp::prior(A[++l], pivot));
		while ((l < r) && Comp::prior(pivot, A[--r]));
		swap(A, l, r);
	} while (l < r);
	return l;
}

template <typename E>
inline int findpivot(E A[], int i, int j)
{
	return (i + j) / 2;
}

template <typename E,typename Comp>
void qsort(E A[], int i, int j) {
	if (j <= i) return;
	int pivotindex = findpivot(A, i, j);
	swap(A, pivotindex, j);
	int k = partition<E, Comp>(A, i - 1, j, A[j]);
	swap(A, k, j);
	qsort<E, Comp>(A, i, k - 1);
	qsort<E, Comp>(A, k + 1, j);
}

void qsort(int n) {
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
	qsort<int, minintCompare>(bestArraydata, 0, n - 1);
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
	qsort<int, minintCompare>(worstArraydata,  0, n - 1);
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
		qsort<int, minintCompare>(averArraydata, 0, n - 1);
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
		delete[]averArraydata;
	}
	cout << "the aver situation n=" << n << endl;
	cout << "time use=" << sum_time / number << "ms" << endl;
}
/*
int main()
{
	qsort(10);
	qsort(100);
	qsort(1000);
	qsort(10000);
	qsort(100000);
}
*/