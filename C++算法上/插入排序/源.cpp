#include<iostream>
#include<ctime>
#include<Windows.h>
#include"compare.h"
#include"book.h"
using namespace std;
int Data[1000000];
int comps, swaps;
template <class T,class Comp>
void inssort(T A[], int n) {
	for (int i = 1; i < n; i++)
		for (int j = i; (j > 0) && (Comp::prior(A[j], A[j - 1])); j--)
			swap(A, j, j - 1);
}
//为了统计次数不影响统计时间,故写统计次数用的排序算法
template <class T, class Comp>
void inssort_frequencyStatistics(T A[], int n) {
	comps = 0;
	swaps = 0;
	for (int i = 1; i < n; i++)
		for (int j = i; comps++, (j > 0) && (Comp::prior(A[j], A[j - 1])); j--) {
			swap(A, j, j - 1);
			swaps++;
		}
}


void timeStatistics(int n) {
	LARGE_INTEGER freq_;
	QueryPerformanceFrequency(&freq_);
	LARGE_INTEGER begin_time;
	LARGE_INTEGER end_time;
	double ns_time;

	//best
	for (int i = 0; i < n; i++) {
		Data[i] = i;
	}
	cout << "The best situation for n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	inssort<int, minintCompare>(Data, n);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	//ave 取m次做平均
	int m = 100;
	double sum_time = 0;
	for (int j = 0; j < m; j++) {
		srand(time(0));
		for (int i = 0; i < n; i++) {
			Data[i] = Random(n);
		}
		QueryPerformanceCounter(&begin_time);
		inssort<int, minintCompare>(Data, n);
		QueryPerformanceCounter(&end_time);
		ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
		sum_time += ns_time;
	}
	cout << "The ave situation for n=" << n << endl;
	cout << "time use=" << sum_time / m << "ms" << endl;
	//worst
	for (int i = 0; i < n; i++) {
		Data[i] = n - i - 1;
	}
	cout << "The worst situation for n=" << n << endl;
	QueryPerformanceCounter(&begin_time);
	inssort<int, minintCompare>(Data, n);
	QueryPerformanceCounter(&end_time);
	ns_time = (end_time.QuadPart - begin_time.QuadPart) * 1000.0 / freq_.QuadPart;
	cout << "time use=" << ns_time << "ms" << endl;
	cout << endl;
}
void frequencyStatistics(int n) {
	//best
	for (int i = 0; i < n; i++) {
		Data[i] = i;
	}
	cout << "The best situation for n=" << n << endl;
	inssort_frequencyStatistics<int,minintCompare>(Data, n);
	cout << "comps=" << comps << endl;
	cout << "swaps=" << swaps << endl;
	//ave 取m次做平均
	int m = 100;
	int sum_comps = 0;
	int sum_swaps = 0;
	for (int j = 0; j < m; j++) {
		srand(time(0));
		for (int i = 0; i < n; i++) {
			Data[i] = Random(n);
		}
		inssort_frequencyStatistics<int, minintCompare>(Data, n);
		sum_comps += comps;
		sum_swaps += swaps;
	}
	cout << "The ave situation for n=" << n << endl;
	cout << "comps=" << sum_comps / m << endl;
	cout << "swaps=" << sum_swaps / m << endl;
	//worst
	for (int i = 0; i < n; i++) {
		Data[i] = n - i - 1;
	}
	cout << "The worst situation for n=" << n << endl;
	inssort_frequencyStatistics<int, minintCompare>(Data, n);
	cout << "comps=" << comps << endl;
	cout << "swaps=" << swaps << endl;
	cout << endl;
}

int main() {
	//frequencyStatistics(10);
	//frequencyStatistics(100);
	//frequencyStatistics(1000);
	timeStatistics(10);
	timeStatistics(100);
	timeStatistics(1000);
	timeStatistics(10000);
	timeStatistics(100000);
	timeStatistics(1000000);
}