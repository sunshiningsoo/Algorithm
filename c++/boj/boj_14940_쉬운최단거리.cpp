#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    int garo, sero;
    cin >> garo >> sero;
    vector<vector<int>> map(garo, vector<int>(sero, 0));
    vector<vector<int>> value(garo, vector<int>(sero, 0));
    int startx, starty;
    vector<pair<int, int>> q;

    for (int i=0;i<garo;i++) {
        for (int j=0;j<sero;j++) {
            cin >> map[i][j];
            if (map[i][j] == 2) {
                startx = i;
                starty = j;
            }
            if (map[i][j] == 0) {
                value[i][j] = -5;
            }
        }
    }

    int count = 0;
    vector<vector<int>> isVisited(garo, vector<int>(sero, 0));
    q.push_back({startx, starty});

    
    
    map[startx][starty] = 0;

    while (q.size()) {
        int x = q[0].first;
        int y = q[0].second;
        q.erase(q.begin());
        isVisited[x][y] = 1;
        for (int i=0;i<4;i++) {
            int dxx = x + dx[i];
            int dyy = y + dy[i];
            if (dxx < 0 || dxx >= garo || dyy < 0 || dyy >= sero) continue;
            if (isVisited[dxx][dyy] != 1 and map[dxx][dyy] != 0) {
                isVisited[dxx][dyy] = 1;
                q.push_back({dxx, dyy});
                // map[dxx][dyy] = map[x][y] + 1 > count ? count : map[x][y]+1;
                map[dxx][dyy] = map[x][y]+1;
            }
        }
    }

    for (int i=0;i<garo;i++) {
        for (int j=0;j<sero;j++) {
            if (value[i][j] != -5 && isVisited[i][j] == 0) {
                cout << -1 << " ";
            } else {
                cout << map[i][j] << " ";
            }
        }
        cout << "\n";
    }

}