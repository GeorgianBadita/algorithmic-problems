#include <bits/stdc++.h>

using namespace std;

int N;
long long K;
vector<long long> cit;
vector<long long> initVal;
vector<int> ind;

int main()
{
    cin >> N >> K;
    cit.resize(N);
    ind.resize(N);
    initVal.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> cit[i];
        initVal[i] = cit[i];
        ind[i] = i;
    }

    long long toEveryone = (long long)K / (long long)N;
    K = K % N;

    sort(ind.begin(), ind.end(), [](int i1, int i2) {
        return cit[i1] < cit[i2];
    });

    for (auto &elem : cit) {
        elem += toEveryone;
    }

    for (int i = 0; i < K; i++) {
        cit[ind[i]] += 1;
    }

    for (int i = 0; i < cit.size(); i++) {
        std::cout << cit[i] - initVal[i] << '\n';
    }
    return 0;
}