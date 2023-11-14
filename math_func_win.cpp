/**
 * This file contains the functions to be used in main.py
 * 
 * @author Shaunik Musukula and Elliott Barringer
 * @version 1.1
*/
#include <cmath>

extern "C" {
    long* getRangeSquares(int start, int end) {
        long* squares = new long[end-start+1];

        for (int i = start; i < end + 1; i++) {
           squares[i - start] = pow(i, 2);
        }

        return squares;
    }

    const int N = 3;

    int** getArray()
    {
        int** arr = new int*[N];
        for (int i = 0; i < N; ++i) 
        {
            arr[i] = new int[N];
            for (int j = 0; j < N; ++j) 
            {
                arr[i][j] = i + j;
            }
        }
        return arr;
    }
}



// needed to compile
int main() {}