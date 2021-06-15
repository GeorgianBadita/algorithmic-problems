#include<bits/stdc++.h>

using namespace std;

bool isPrime(long long x) {
    if(x < 2) {
        return false;
    }
    if(x == 2) {
        return true;
    }
    if(x % 2 == 0) {
        return false;
    }

    for(int i = 3; i * i <= x; i += 2) {
        if(x % i == 0) {
            return false;
        }
    }
    return true;
}

unsigned long long nextPrime(unsigned long long current) {
    while(true) {
        current ++;
        if(isPrime(current)) {
            return current;
        }
    }
}

/*
 * Complete the 'primeCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts LONG_INTEGER n as parameter.
 */

int primeCount(long n) {
    if(n < 2) {
        return 0;
    }
    if(n == 2) {
        return 1;
    }

    unsigned long long prod = 1;
    unsigned long long currentPrime = 2;
    int count = 0;
    while(prod <= n) {
        prod *= currentPrime;
        currentPrime = nextPrime(currentPrime);
        count += 1;
    }
    return count - 1;
}

int main() {
    cout << primeCount(10000000000);
    return 0;
}