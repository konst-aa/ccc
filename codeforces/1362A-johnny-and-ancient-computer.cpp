#include <iostream>
using namespace std;


int main() {
  int cases;
  cin >> cases;
  for (int c=0; c<cases; c++) {
    long long n1, n2;
    cin >> n1 >> n2;
    int counter = 0;
    if (n1 < n2) {
      while (n1 < n2) {
        n1 <<= 1;
        counter++;
      }
      if (n1 != n2) {
        counter = 0;
      }
      else {
        cout << "-1";
      }
    }
  }
}
