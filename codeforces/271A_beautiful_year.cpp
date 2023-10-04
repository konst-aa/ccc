#include <set>
#include <iostream>
using namespace std;

int main() {
  int year;
  cin >> year;
  while (true) {
    year++;
    int t = year;
    set<int> s;
    for (int i=0; i<4; i++) {
      s.insert(t % 10);
      t /= 10;
    }
    if (s.size() == 4) {
      cout << year;
      break;
    }
  }
}

