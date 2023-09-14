#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int directions[4] = {0, 1, 2, 3};
vector<vector<int>> map;
int cleaned = 0;

int main(void) {
    int row, col;
    cin >> row >> col;
    map = vector<vector<int>>(row, vector<int>(col, 0));
    vector<vector<int>> isVisited(row, vector<int>(col, 0));

    int startX, startY, currentDirection;
    cin >> startX >> startY >> currentDirection;

    for (int i=0;i<row;i++) {
        for (int j=0;j<col;j++) {
            cin >> map[i][j];
        }
    }

    vector<pair<int, int>> q;
    q.push_back(make_pair(startX, startY));
    while (q.size() != 0) {
        int x = q[0].first;
        int y = q[0].second;
        q.erase(q.begin());
        cout << x << " "<< y<<"\n";

        if (isVisited[x][y] == 0) {
            cleaned += 1;
            isVisited[x][y] = 1;
        }
        int temp = 0;
        for (int i=0;i<4;i++) {
            int dxx = x + dx[i];
            int dyy = y + dy[i];
            if (dxx<0 || dxx>=row || dyy <0 || dyy >= col) continue;
            if (isVisited[dxx][dyy] == 0 && map[dxx][dyy] == 0) temp += 1;

        }
        if (temp == 0) {
            if (0<= x-dx[currentDirection] && x-dx[currentDirection] < row && 0<=y-dy[currentDirection] && y-dy[currentDirection] < col && map[x-dx[currentDirection]][y-dy[currentDirection]]!=1) {
                q.push_back(make_pair(x-dx[currentDirection], y - dy[currentDirection]));
            } else {
                break;
            }
        } else {
            if (currentDirection == 0) {
                currentDirection = 3;
            } else {
                currentDirection -= 1;
            }
            if (0<= x+dx[currentDirection] && x+dx[currentDirection] < row && 0<=y+dy[currentDirection] && y+dy[currentDirection] < col) {
                if (isVisited[x+dx[currentDirection]][y+dy[currentDirection]] == 0 && map[x+dx[currentDirection]][y+dy[currentDirection]] != 1) {
                    q.push_back(make_pair(x+dx[currentDirection], y+dy[currentDirection]));
                } else {
                    q.push_back(make_pair(x, y));
                }
            }
        }
        
        
        
    }
    cout << cleaned;


}