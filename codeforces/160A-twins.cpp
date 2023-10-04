#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> coins(n);
  int total = 0;
  for (int i = 0; i < n; i++) {
    cin >> coins[i];
    total += coins[i];
  }
  int taker_total = 0;
  sort(coins.begin(), coins.end(), greater<>());
  for (int i=0; i<n; i++) {
    taker_total += coins[i];
    total -= coins[i];
    if (taker_total > total) {
      cout << i+1;
      return 0;
    }
  }
}
