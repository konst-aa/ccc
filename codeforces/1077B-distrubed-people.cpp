#include <iostream>
// https://codeforces.com/problemset/problem/1077/B
using namespace std;

int main() {
  int n;
  cin >> n;

  int ppl[n];
  for (int i=0; i<n; i++) {
    cin >> ppl[i];
  }
  int counter = 0;
  for (int i=1; i<n-1; i++) {
    if (ppl[i-1] == 1 && ppl[i] == 0 && ppl[i+1] == 1) {
      ppl[i+1] = 0;
      counter++;
    }
  }
  cout << counter;
}
