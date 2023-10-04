#include <iomanip>
#include <iostream>
#include <math.h>

// https://codeforces.com/problemset/problem/1182/A
// this was BS

using namespace std;

int main() {
  int size;
  cin >> size;
  if (size % 2 == 1) {
    cout << 0;
    return 0;
  }
  cout << fixed << setprecision(0) << pow(2, size / 2);
}
