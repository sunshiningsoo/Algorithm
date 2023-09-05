#include <iostream>
#include <vector>
#include <string>

using namespace std;

int dx[4] = {0, 0, 1, 1}; // 아래
int dy[4] = {0, 1, 0, 1}; // 옆
int count = 0;
int r;
int c;
// Z 탐색을 큰 덩이부터 쭉쭉 내려가면 되겠다!

void findZ(int currentX, int currentY, vector<vector<int>>& temp, int size) {

    for(int i=0;i<4;i++) {
        if (size == 2) {
            int dxx = dx[i] + currentX;
            int dyy = dy[i] + currentY;
            temp[dxx][dyy] = ::count;
            ::count++;
        } else if (size != 2) {
            findZ(currentX, currentY, temp, size / 2);
            findZ(currentX, currentY+size/2, temp, size / 2);
            findZ(currentX+size/2, currentY, temp, size / 2);
            findZ(currentX+size/2, currentY+size/2, temp, size / 2);
            return;
        }
    }

}

int main(void) {
    int n;
    int size;
    cin >> n >> r >> c;
    size = (1<<n);

    vector<vector<int>> temp((1<<n), vector<int>((1<<n), 0));

    findZ(0, 0, temp, size);

    // for(int i=0;i<(1<<n);i++) {
    //     for(int j=0;j<(1<<n);j++) {
    //         cout << temp[i][j]<<" ";
    //     }
    //     cout << "\n";
    // }

    cout << temp[r][c];


    // cout << (1<<3); 2의 3승임
}