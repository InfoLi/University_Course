// From the software distribution accompanying the textbook
// "A Practical Introduction to Data Structures and Algorithm Analysis,
// Third Edition (C++)" by Clifford A. Shaffer.
// Source code Copyright (C) 2007-2011 by Clifford A. Shaffer.

// Some definitions for Comparator classes
#include <string.h>

// For use with min-heap and sorting
class minintCompare {
public:
  static bool prior(int x, int y) { return x < y; }
};

// For use with max-heap and heapsorting
class maxintCompare {
public:
  static bool prior(int x, int y) { return x > y; }
};

// Compare two ints
class intintCompare { // Comparator class for integer keys
public:
  static bool lt(int x, int y) { return x < y; }
  static bool eq(int x, int y) { return x == y; }
  static bool gt(int x, int y) { return x > y; }
};

class CCCompare { // Compare two character strings
public:
  static bool lt(char* x, char* y)
    { return strcmp(x, y) < 0; }
  static bool eq(char* x, char* y)
    { return strcmp(x, y) == 0; }
  static bool gt(char* x, char* y)
    { return strcmp(x, y) > 0; }
};

// Get the key for a character string.
// The key is just the string itself.
class getCKey {
public:
  static char* key(char* x) { return x; }
};
