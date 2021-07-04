#include <bits/stdc++.h>
#define NMAX 405

using namespace std;
const long long INF = 1LL << 60;

long long A[NMAX][NMAX] = {0};
int N, M;

void readMatrix()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i != j) {
                A[i][j] = INF;
            }
            else {
                A[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < M; i++) {
        int s, t, c;
        cin >> s >> t >> c;
        A[s - 1][t - 1] = c;
    }
}

long long solve()
{
    long long ans = 0;
    for (int k = 0; k < N; k++) {

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = min(A[i][j], A[i][k] + A[k][j]);
                if (A[i][j] < INF) {
                    ans += A[i][j];
                }
            }
        }
    }
    return ans;
}

int main()
{
    readMatrix();
    cout << solve() << '\n';
    return 0;
}