#include <bits/stdc++.h>
using namespace std;

int main() {
  long long cases, cols;
  cin >> cases;
  for (long long c = 0; c < cases; c++) {
    cin >> cols;
    vector<long long> health(cols);
    vector<long long> spells(cols);
    for (int j = 0; j < cols; j++)
      cin >> health[j];
    for (int j = 0; j < cols; j++)
      cin >> spells[j];

    auto it = max_element(spells.begin(), spells.end());
    int midpoint = distance(spells.begin(), it);
    long long total = 0;

    for (int j = 0; j < midpoint; j++) {
      total += health[j] + spells[j];
    }
    for (int j = cols - 1; j > midpoint; j--) {
      total += health[j] + spells[j];
    }
    total += health[midpoint];
    cout << total << endl;
  }
}
