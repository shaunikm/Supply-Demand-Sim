import c_loader as cl

def getRangeSquares(start, end):
    squares = cl.cpp_file.getRangeSquares(start, end)
    result = [squares[i] for i in range(end-start+1)]
    del squares
    return result