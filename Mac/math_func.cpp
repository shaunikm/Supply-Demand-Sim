/**
 * This file contains the functions to be used in main.py
 * 
 * @author Shaunik Musukula
 * @version 1.1
*/
#include <cmath>

extern "C" {
    long* getRangeSquares(int start, int end) {
        long* squares = new long[end-start+1];

        for (long i=start; i < end+1; i++) {
           squares[i - start] = pow(i, 2);
        }

        return squares;
    }
}