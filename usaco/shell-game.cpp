#include <bits/stdc++.h>
using namespace std;


int main() {
    ifstream inp;
    ofstream otp;
    inp.open("shell.in");
    otp.open("shell.out");
    
    int n, t, a, b, g;
    inp >> n;
    int state[] = {0, 0, 0, 0};
    for (int i=0; i<n; i++) {
        inp >> a >> b >> g;
        swap(state[a], state[b]);
        state[g]++;
    }
    cout << state[0] << state[1] << state[2] << state[3] << endl;
    otp << *max_element(state, state+4);
    otp.close();

}
