#include <bits/stdc++.h>

int largestSubset(std::vector<int> nums, int k)
{
    if (k == 0 || k == 1) {
        return 1;
    }
    std::set<int> notToTake = {};
    std::unordered_map<int, int> freq = {};

    for (const auto &num : nums) {
        if (freq.find(num % k) != freq.end()) {
            freq[num % k] += 1;
        }
        else {
            freq[num % k] = 1;
        }
    }

    int longest = freq.find(0) != freq.end() ? 1 : 0;

    for (int i = 1; i <= k / 2; i++) {
        if (i != k - i) {
            int iDivs = freq.find(i) != freq.end() ? freq[i] : 0;
            int kiDivs = freq.find(k - i) != freq.end() ? freq[k - i] : 0;
            longest += std::max(iDivs, kiDivs);
        }
        else {
            longest += 1;
        }
    }

    return longest;
}

int main()
{
    int n, k;
    std::vector<int> set;

    std::cin >> n >> k;

    for (int i = 0; i < n; i++) {
        int num;
        std::cin >> num;
        set.push_back(num);
    }
    std::cout << largestSubset(set, k);
    return 0;
}