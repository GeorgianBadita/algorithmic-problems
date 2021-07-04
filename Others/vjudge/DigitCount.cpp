#include <bits/stdc++.h>

using namespace std;

int M, N;
int dp[11][11];
bool checkDigit(int val, int pos)
{
    return (val & (1 << pos)) != 0;
}

int solve(int ind, int parent, int digits)
{
    if (ind == N) {
        return 1;
    }
    if (dp[ind][parent] != -1) {
        return dp[ind][parent];
    }
    int cnt = 0;
    for (int i = 0; i < 10; i++) {
        if (!checkDigit(digits, i)) continue;
        if (parent == 0 || abs(i - parent) < 3) {
            cnt += solve(ind + 1, i, digits);
        }
    }
    return dp[ind][parent] = cnt;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> M >> N;
        int digits = 0;
        for (int i = 0; i < M; i++) {
            int d;
            cin >> d;
            digits |= (1 << d);
        }
        memset(dp, -1, sizeof(dp));
        cout << "Case " << i << ": " << solve(0, 0, digits) << '\n';
    }
}