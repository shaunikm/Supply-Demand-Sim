/**
 * This file contains the functions to be used in main.py
 * 
 * @author Shaunik Musukula
 * @version 1.1
*/
#include <cmath>
#include <inttypes.h>

# define DLL00_EXPORT_API __declspec(dllexport)

#include "win_math.h"

DLL00_EXPORT_API long* getRangeSquares(int start, int end) {
        long* squares = new long[end-start+1];

        for (int i = start; i < end + 1; i++) {
           squares[i - start] = pow(i, 2);
        }

        return squares;
    }

int main() {}