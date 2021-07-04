#include <bits/stdc++.h>

using namespace std;

int main()
{
    int coins[11], S;
    memset(coins, 0, sizeof(coins));
    coins[0] = 1;
    coins[1] = 1;
    for (int i = 2; i < 11; i++) {
        coins[i] = i * coins[i - 1];
    }

    cin >> S;
    int best = 1;
    while (coins[best] < S && best != 10) {
        best++;
    }
    int ans = 0;
    if (coins[best] == S) {
        ans = 1;
    }
    else {
        while (S != 0) {
            if (S - coins[best] >= 0) {
                S -= coins[best];
                ans++;
            }
            else {
                best -= 1;
            }
        }
    }
    cout << ans;
    return 0;
}