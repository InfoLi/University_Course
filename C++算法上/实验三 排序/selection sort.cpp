#include<iostream>
#include<stdlib.h>
#include"compare.h"
#include<ctime>
#include<Windows.h>
using namespace std;

template<typename E,typename Comp>
void selsort(E A[], int n) {
	for (int i = 0; i < n - 1; i++) {
		int lowindex = i;
		for (int j = n - 1; j > i; j--) {
			if (Comp::prior(A[j], A[lowindex])) {
				lowindex = j;
			}
		}
		swap(A, i, lowindex);
	}
}

template<typename E, typename Comp>
void selsortcount(E A[], int n,int a[]) {
	int swapcount = 0;
	int compcount = 0;
	for (int i = 0; i < n - 1; i++) {
		int lowindex = i;
		for (int j = n - 1; j > i; j--) {
			if (Comp::prior(A[j], A[lowindex]),compcount++) {
				lowindex = j;
			}
		}
		swapcount++;
		swap(A, i, lowindex);
	}
	a[0] = swapcount;
	a[1] = compcount;
}

void selsort(int n) {
	LARGE_INTEGER freq_;
	QueryPerformanceFrequency(&freq_);
	LARGE_INTEGER begin_time;
	LARGE_INTEGER end_time;
	double ns_time;

	int a[2] = { 0,0 }; //存储交换和比较次数

	//best
	int* bestArraydata = new int[100000];
	int* bestArraydatacount = new int[100000];
	for (int i = 0; i < n; i++) {
		bestArraydata[i] = i;
		bestArraydatacount[i] = i;
	}
	cout << "the best situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	selsort<int, minintCompare>(bestArraydata, n);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	selsortcount<int, minintCompare>(bestArraydatacount, n, a);
	cout << "swapcount: " << a[0] << endl;
	cout << "compcount: " << a[1] << endl;
	a[0] = 0; //clear
	a[1] = 0;
	delete[]bestArraydata;
	delete[]bestArraydatacount;

	//worst
	int* worstArraydata = new int[100000];
	int* worstArraydatacount = new int[100000];
	for (int i = 0; i < n; i++) {
		worstArraydata[i] = n - i - 1;
		worstArraydatacount[i] = n - i - 1;
	}
	cout << "the worst situation n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	selsort<int, minintCompare>(worstArraydata, n);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	selsortcount<int, minintCompare>(worstArraydatacount, n, a);
	cout << "swapcount: " << a[0] << endl;
	cout << "compcount: " << a[1] << endl;
	a[0] = 0; //clear
	a[1] = 0;
	delete[]worstArraydata;
	delete[]worstArraydatacount;

	//aver
	int number = 10; //取10次平均
	double sum_time = 0;
	int sum_swapcount = 0;
	int sum_compount = 0;
	for (int j = 0; j < number; j++)
	{
		int* averArraydata = new int[100000]; //存放数组
		int* averArraydatacount = new int[100000];
		for (int i = 0; i < n; i++) {
			int temp = rand() % 100; //1-100取随机数
			averArraydata[i] = temp;
			averArraydatacount[i] = temp;
		}
		QueryPerformanceCounter(&begin_time);
		selsort<int, minintCompare>(averArraydata, n);
		QueryPerformanceCounter(&end_time);
		ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
		sum_time = sum_time + ns_time;
		selsortcount<int, minintCompare>(averArraydatacount, n, a);
		sum_swapcount = sum_swapcount + a[0];
		sum_compount = sum_compount + a[1];
		/* test01
		cout << "swap" << a[0] << "somp" << a[1] << endl;
		cout << "sumtime" << sum_time << endl;
		for (int k = 0; k < n; k++)
		{
			cout << averArraydata[k] << " ";
		}
		cout << j << endl;
		*/
		/* test02
		for (int k = 0; k < n; k++)
		{
			cout << averArraydata[k] << " ";
		}
		cout << endl << j<<endl;
		*/
		a[0] = 0; //clear
		a[1] = 0;
		delete[]averArraydata;
		delete[]averArraydatacount;
	}
	cout << "the aver situation n=" << n << endl;
	cout << "time use=" << sum_time / number << "ms" << endl;
	cout << "swapcount: " << sum_swapcount / number << endl;
	cout << "compcount: " << sum_compount / number << endl;
}
/*
int main() {
	selsort(10);
	selsort(100);
	selsort(1000);
	selsort(10000);
}
*/