#include<iostream>
#include<stdlib.h>
#include"compare.h"
#include<ctime>
#include<Windows.h>
using namespace std;

template <typename E,typename getKey>
void radix(E A[], E B[], int n, int k, int r, int cnt[]) {
	int j;
	for (int i = 0, rtoi = 1; i < k; i++, rtoi *= r) {
		for (j = 0; j < r; j++) cnt[j] = 0;
		for (j = 0; j < n; j++) cnt[(getKey::key(A[j]) / rtoi) % r]++;
		for (j = 1; j < r; j++) cnt[j] = cnt[j - 1] + cnt[j];
		for (j = n - 1; j >= 0; j--)
			B[--cnt[(getKey::key(A[j]) / rtoi % r)]] = A[j];
		for (j = 0; j < n; j++) A[j] = B[j];                    
	}
}

void radixsort(int n) {
	LARGE_INTEGER freq_;
	QueryPerformanceFrequency(&freq_);
	LARGE_INTEGER begin_time;
	LARGE_INTEGER end_time;
	double ns_time;
	
	//best
	int* bestArraydata = new int[100000];
	int* bestemptyarray = new int[100000];
	int* bestcnt = new int[10];
	for (int i = 0; i < n; i++) {
		bestArraydata[i] = i;
	}
	cout << "the best situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	radix<int, getIntKey>(bestArraydata,bestemptyarray ,n,10,10,bestcnt);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	delete[]bestArraydata;
	delete[]bestemptyarray;
	delete[]bestcnt;

	//worst
	int* worstArraydata = new int[100000];
	int* worstemptyarray = new int[100000];
	int* worstcnt = new int[10];
	for (int i = 0; i < n; i++) {
		worstArraydata[i] = n - i - 1;
	}
	cout << "the worst situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	radix<int, getIntKey>(worstArraydata,worstemptyarray, n,10,10,worstcnt);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	delete[]worstArraydata;
	delete[]worstemptyarray;
	delete[]worstcnt;
	
	//aver
	int number = 10; //取10次平均
	double sum_time = 0;
	for (int j = 0; j < number; j++)
	{
		int* averArraydata = new int[100000]; //存放数组
		int* averemptyarray = new int[100000];
		int* avercnt = new int[10];
		for (int i = 0; i < n; i++) {
			int temp = rand() % 1000; //1-100取随机数
			averArraydata[i] = temp;
		}
		QueryPerformanceCounter(&begin_time);
		radix<int, getIntKey>(averArraydata,averemptyarray, n,10,10,avercnt);
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

int main()
{
	radixsort(10);
	radixsort(100);
	radixsort(1000);
	radixsort(10000);
	radixsort(100000);
}
