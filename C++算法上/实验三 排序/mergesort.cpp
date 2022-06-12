#include<iostream>
#include<stdlib.h>
#include"compare.h"
#include<ctime>
#include<Windows.h>
using namespace std;

template <typename E,typename Comp>
void mergesort(E A[], E temp[], int left, int right) {
	if (left == right) return;
	int mid = (left + right) / 2;
	mergesort<E, Comp>(A, temp, left, mid);
	mergesort<E, Comp>(A, temp, mid + 1, right);
	for (int i = left; i <= right; i++) {
		temp[i] = A[i];
	}
	int i1 = left; int i2 = mid + 1;
	for (int curr = left; curr <= right; curr++) {
		if (i1 == mid + 1)
			A[curr] = temp[i2++];
		else if (i2 > right)
			A[curr] = temp[i1++];
		else if (Comp::prior(temp[i1], temp[i2]))
			A[curr] = temp[i1++];
		else A[curr] = temp[i2++];
	}
}
void mergesort(int n) {
	LARGE_INTEGER freq_;
	QueryPerformanceFrequency(&freq_);
	LARGE_INTEGER begin_time;
	LARGE_INTEGER end_time;
	double ns_time;

	//best
	int* besttemp = new int[100000];
	int* bestArraydata = new int[100000];
	for (int i = 0; i < n; i++) {
		bestArraydata[i] = i;
	}
	cout << "the best situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	mergesort<int, minintCompare>(bestArraydata,besttemp,0, n-1);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	delete[]bestArraydata;
	delete[]besttemp;

	//worst
	int* worsttemp = new int[100000];
	int* worstArraydata = new int[100000];
	for (int i = 0; i < n; i++) {
		worstArraydata[i] = n - i - 1;
	}
	cout << "the worst situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	mergesort<int, minintCompare>(worstArraydata,worsttemp,0, n-1);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	delete[]worstArraydata;
	delete[]worsttemp;

	//aver
	int number = 10; //取10次平均
	double sum_time = 0;
	for (int j = 0; j < number; j++)
	{
		int* avertemp = new int[100000];
		int* averArraydata = new int[100000]; //存放数组
		for (int i = 0; i < n; i++) {
			int temp = rand() % 100; //1-100取随机数
			averArraydata[i] = temp;
		}
		QueryPerformanceCounter(&begin_time);
		mergesort<int, minintCompare>(averArraydata,avertemp,0, n-1);
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
		delete[]avertemp;
	}
	cout << "the aver situation n=" << n << endl;
	cout << "time use=" << sum_time / number << "ms" << endl;
}
/*
int main()
{
	mergesort(10);
	mergesort(100);
	mergesort(1000);
	mergesort(10000);
	mergesort(100000);
}
*/