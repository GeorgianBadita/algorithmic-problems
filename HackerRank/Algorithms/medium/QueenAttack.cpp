#include<bits/stdc++.h>

bool validPosition(std::pair<int, int> position, int n) {
    int x = position.first;
    int y = position.second;

    return x >= 1 && x <= n && y >= 1 && y <= n;
}

int queensAttack(std::set<std::pair<int, int> > obstacles, std::pair<int, int> queenPos, int n) {
    int dx[] = {0, 0, -1, 1, -1, 1, 1, -1};
    int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
    int numPieces = 0;
    for(int dir = 0; dir < 8; dir ++) {
        int offX = dx[dir];
        int offY = dy[dir];
        std::pair<int, int> startPos = std::make_pair(queenPos.first, queenPos.second);
        bool foundObs = false;

        while(validPosition(startPos, n) && !foundObs) {
            if(obstacles.find(startPos) != obstacles.end()) {
                foundObs = true;
                continue;
            }
            numPieces += 1;
            startPos = std::make_pair(startPos.first + offX, startPos.second + offY);
        }
    }
    return numPieces - 8;
}


int main() {
    int n, p;
    int startX, startY;
    std::set<std::pair<int, int> > obstacles;
    std::cin >> n >> p;
    std::cin >> startX >> startY;

    for(int i = 0; i < p; i++) {
        int x, y;
        std::cin >> x >> y;
        obstacles.insert(std::make_pair(x, y));
    }

    std::cout << queensAttack(obstacles, std::make_pair(startX, startY), n);
    return 0;
}