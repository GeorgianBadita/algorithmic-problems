#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'findPoint' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER px
 *  2. INTEGER py
 *  3. INTEGER qx
 *  4. INTEGER qy
 */

vector<int> findPoint(int px, int py, int qx, int qy) {
    return vector<int>{2 * qx - px, 2 * qy - py};
}

int main()
{
    for(const auto elem : findPoint(0, 0, 1, 1)) {
        cout << elem << ' ';
    }
    
    return 0;
}
