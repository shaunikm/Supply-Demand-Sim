import c_loader as cl

def getRangeSquares(start, end):
    squares = cl.cpp_file.getRangeSquares(start, end)
    result = squares[:end-start]
    del squares
    return result