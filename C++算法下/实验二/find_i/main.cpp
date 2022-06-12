#include<iostream>
#include <ctime>
using namespace std;
//从小到大
int find(int num[], int n, int m, int i) {
	//只有一个值的时候返回
	if (m < n + 1) {
		return num[m];
	}
	int p = num[n];//轴值
	//进行排序
	int left = n + 1;
	int right = m;
	int temp;
	while (left != right)
	{
		while (num[left] <= p && left != right)//需要保证不超界
			left++;
		while (num[right] > p && right != left)
			right--;
		temp = num[left];
		//交换left和right
		num[left] = num[right];
		num[right] = temp;
	}
	//将轴值放入
	if (p > num[left])
	{
		num[n] = num[left];
		num[left] = p;
		//选择合适的位置进行遍历
		if (left == i)
			return num[i];
		else if (left > i)
			return find(num, n, left - 1, i);
		else
			return find(num, left + 1, m, i);
	}
	else
	{
		num[n] = num[left - 1];
		num[left - 1] = p;

		if (left - 1 == i)
			return num[i];
		else if (left - 1 > i)
			return find(num, n, left - 2, i);
		else
			return find(num, left, m, i);
	}
}

int main() {
	int *num;
	num = new int[10];
	srand(time(NULL));
	int size = 4000;
	for (int i = 0; i < 1; i++)
	{
		clock_t start, finish;
		double  duration;
		start = clock();
		//多次遍历取平均值
		for (int j = 0; j < 1000; j++)
		{
			num = new int[size];
			srand(time(NULL));
			//生成初始数组
			for (int m = 0; m < size; m++)
			{
				num[m] = rand();
			}
			//查找第i个最小值
			find(num, 0, size - 1, rand()%size);
			delete[]num;
		}
		finish = clock();
		duration = (double)(finish - start) / CLOCKS_PER_SEC;
		printf("%f seconds\n", duration/1000);
	}
	return 0;
}