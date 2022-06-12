#include<iostream>
#include <time.h> 
#include<vector>


using namespace std;

void Print(int** T1, int size) {
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            cout << T1[i][j] << " ";
        }
        cout << endl;
    }
    cout << "*********************" << endl;
}


void multiplyMatrix(int** T1, int** T2, int** result, int size) {
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            result[i][j] = 0;

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            for (int k = 0; k < size; k++)
            {
                result[i][j] += T1[i][k] * T2[k][j];
            }
        }
    }
}


void addMatrix(int** T1, int** T2, int** result, int size) {   
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            result[i][j] = T1[i][j] + T2[i][j];
}

void reduceMatrix(int** T1, int** T2, int** result, int size) {

    for (int i = 0; i < size; i++)
        for (int j = 0; j < size; j++)
            result[i][j] = T1[i][j] - T2[i][j];

}


void Strassen(int** T1, int** T2, int** result, int size) {

    int len = size / 2;
    int** A11 = new int* [len], ** A12 = new int* [len], ** A21 = new int* [len], ** A22 = new int* [len];
    int** B11 = new int* [len], ** B12 = new int* [len], ** B21 = new int* [len], ** B22 = new int* [len];
    

    for (int i = 0; i < len; i++)
    {
        A11[i] = T1[i];
        A12[i] = &T1[i][len];
        A21[i] = T1[i + len];
        A22[i] = &T1[i + len][len];
        B11[i] = T2[i];
        B12[i] = &T2[i][len];
        B21[i] = T2[i + len];
        B22[i] = &T2[i + len][len];
    }
    
    int** s1 = new int* [len], ** s2 = new int* [len], ** s3 = new int* [len], ** s4 = new int* [len], ** s5 = new int* [len], ** s6 = new int* [len], ** s7 = new int* [len];

    int** t1 = new int* [len];
    int** t2 = new int* [len];

    for (int i = 0; i < len; i++)
    {
        s1[i] = new int[len];
        s2[i] = new int[len];
        s3[i] = new int[len];
        s4[i] = new int[len];
        s5[i] = new int[len];
        s6[i] = new int[len];
        s7[i] = new int[len];
        t1[i] = new int[len];
        t2[i] = new int[len];
    }

    //s1
    reduceMatrix(A12, A22, t1, len);
    addMatrix(B21, B22, t2, len);
    multiplyMatrix(t1, t2, s1, len);
    //s2
    addMatrix(A11, A22, t1, len);
    addMatrix(B11, B22, t2, len);
    multiplyMatrix(t1, t2, s2, len);
    //s3
    reduceMatrix(A11, A21, t1, len);
    addMatrix(B11, B12, t2, len);
    multiplyMatrix(t1, t2, s3, len);
    //s4
    addMatrix(A11, A12, t1, len);
    multiplyMatrix(t1, B22, s4, len);
    //s5
    reduceMatrix(B12, B22, t1, len);
    multiplyMatrix(A11, t1, s5, len);
    //s6
    reduceMatrix(B21, B11, t1, len);
    multiplyMatrix(A22, t1, s6, len);
    //s7
    reduceMatrix(A21, A22, t1, len);
    multiplyMatrix(t1, B11, s7, len);

    addMatrix(s1, s2, t1, len);
    addMatrix(t1, s6, t2, len);
    reduceMatrix(t2, s4, t1, len);
    for (int i = 0; i < len; i++)
        for (int j = 0; j < len; j++)
            result[i][j] = t1[i][j];
    addMatrix(s4, s5, t1, len);
    for (int i = 0; i < len; i++)
        for (int j = 0; j < len; j++)
            result[i][j+len] = t1[i][j];
    addMatrix(s6, s7, t1, len);
    for (int i = 0; i < len; i++)
        for (int j = 0; j < len; j++)
            result[i + len][j] = t1[i][j];
    addMatrix(s2, s5, t1, len);
    reduceMatrix(t1, s3, t2, len);
    reduceMatrix(t2, s7, t1, len);
    for (int i = 0; i < len; i++)
        for (int j = 0; j < len; j++)
            result[i + len][j + len] = t1[i][j];
}



int main() {
    srand(time(NULL));

	clock_t start, finish;
	double  duration;

    int** A, ** B, ** result;
    int size = 128;

    A = new int* [size];
    B = new int* [size];
    result = new int* [size];
    for (int i = 0; i < size; i++)
    {
        A[i] = new int[size];
        B[i] = new int[size];
        result[i] = new int[size];
    }

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            A[i][j] = rand() % 100;
            B[i][j] = rand() % 100;
            result[i][j] = 0;
        }
    }

	start = clock();

    Strassen(A, B, result, size);
    

    finish = clock();
    duration = (double)(finish - start) / CLOCKS_PER_SEC;
    printf("%f seconds\n", duration);
}