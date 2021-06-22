#include<bits/stdc++.h>
using namespace std;

vector<int> A;

int main() {
    int N;
    cin >> N;
    A.resize(N);
    
    for(int i = 0; i < N; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    long long totalPairs = (A.size() * (A.size() - 1)) / 2;
    long long currentEqual = 1;
    for(int i = 0; i < N; i++) {
        if(A[i] == A[i + 1]) {
            currentEqual ++;
        } else {
            totalPairs -= (currentEqual - 1) * currentEqual / 2;
            currentEqual = 1;
        }
    }
    cout << totalPairs;
    return 0;
}