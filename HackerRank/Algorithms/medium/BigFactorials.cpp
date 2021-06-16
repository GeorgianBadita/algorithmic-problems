#include<bits/stdc++.h>

class BigInteger {
private:
    std::vector<int> num;

    std::vector<int> assignNum(int number) {
        std::vector<int> tmpNum = std::vector<int>{};
        while(number != 0) {
            tmpNum.push_back(number % 10);
            number /= 10;
        }
        return tmpNum;
    }

public:
    BigInteger(int number) {
        this->num = assignNum(number);
    }

    BigInteger(std::vector<int> num) {
        this->num = num;
    }

    //    Complex<T> operator*(Complex<T> const& rhs) const;

    const std::vector<int>& getNum() const {
        return this->num;
    }

    BigInteger operator*(BigInteger const& rhs) const {
        std::vector<int> A = this->num;
        std::vector<int> B = rhs.getNum();
        std::vector<int> C = std::vector<int>(A.size() + B.size() - 1, 0);
        
        for(int i = 0; i < A.size(); i++) {
            for(int j = 0; j < B.size(); j++) {
                C[i + j] += A[i] * B[j];
            }
        }

        int T = 0;
        for(int i = 0; i < C.size(); i++) {
            int currSum = C[i] + T;
            T = currSum / 10;
            C[i] = currSum % 10;
        }

        if(T) {
            C.push_back(T);
        }

        return BigInteger{C};
    }

    std::string printNum() {
        std::string str;
        for(const auto& elem: this->num) {
            str = std::to_string(elem) + str;
        }

        return str + "\n";
    }
};

void extraLongFactorials(int n) {
    if(n == 0) {
        std::cout << 1;
        return;
    }

    if(n < 3) {
        std::cout << n;
        return;
    }
    BigInteger result = {1};
    for(int i = 2; i <= n; i++) {
        BigInteger current = {i};
        result = result * current;
    }
    std::cout << result.printNum();
}

int main() {
    int n;
    std::cin >> n;
    extraLongFactorials(n);
    return 0;
}