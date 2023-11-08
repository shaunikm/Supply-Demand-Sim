#if defined(_WIN32)
#  if defined(DLL01_EXPORTS)
#    define DLL01_EXPORT_API __declspec(dllexport)
#  else
#    define DLL01_EXPORT_API __declspec(dllimport)
#  endif
#else
#  define DLL01_EXPORT_API
#endif


DLL01_EXPORT_API void dll01Func00();