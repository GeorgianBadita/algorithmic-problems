#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int S = 0;
    for(int i = 1; i<=N; i++) {
        S += i;
        if(S >= N) {
            cout << i;
            break;
        }
    }
    return 0;
}