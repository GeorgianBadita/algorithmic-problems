#include<bits/stdc++.h>
#include<algorithm>

int getSq(int n) {
    int x = 0;
    while(x*x < n) {
        x ++;
    }
    return x;
}

std::string encryption(std::string string) {
    std::vector<std::string> result;
    string.erase(std::remove_if(string.begin(), string.end(), [](unsigned char x) {
        return std::isspace(x);
    }), string.end());

    int sq = getSq(string.size());
    int row = 0, col = 0;
    if(sq * sq == string.size()) {
        row = col = sq;
    } else {
        row = sq - 1;
        col = sq;
    }
    if(row * col < string.size()) {
        row += 1;
    }
    int currentStrPos = 0;
    for(int r = 0; r < row; r ++) {
        std::string current = "";
        for(int c = 0; c < col; c++) {
            if(currentStrPos < string.size()) {
                current += string[currentStrPos];
                currentStrPos += 1;
            }
        }
        if(current.size() == 0) {break;}
        result.push_back(current);
    }
    string = "";
    for(int c = 0; c < col; c ++) {
        for(int r = 0; r < row; r++) {
            if(c < result[r].size()) {
                string += result[r][c];
            }
        }
        if(c != col - 1) {
            string += " ";
        }
    }
    return string;
}


int main() {
    std::string s;
    std::cin >> s;
    std::cout << encryption(s);
    return 0;
}