import ctypes
import settings
import os

cwd = os.getcwd()
cpp_path = os.path.join(cwd, settings.CPP_FILENAME)
cpp_file = ctypes.CDLL(cpp_path, winmode=0)

cpp_file.getRangeSquares.argtypes = [ctypes.c_int]
cpp_file.getRangeSquares.restype = ctypes.POINTER(ctypes.c_long)