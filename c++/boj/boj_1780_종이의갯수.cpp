#include <iostream>
#include <vector>

using namespace std;

int oneCount, zeroCount, minusCount = 0;
vector<vector<int>> world;

vector<int> checkHap(int x, int y, int width) {
    vector<int> arr(3, 0);
    
    // boolean 값으로도 체크 가능함
    bool checked = false;

    for (int i=x;i<x+width;i++) {
        for (int j=y;j<y+width;j++) {
            if (world[i][j] == 1) arr[2] += 1;
            else if (world[i][j] == 0) arr[1] += 1;
            else if (world[i][j] == -1) arr[0] += 1;
        }
    }

    return arr;
}

void cut(int x, int y, int width) {
    vector<int> temp = checkHap(x, y, width);
    if (temp[1] == 0 && temp[2] == 0) {
        minusCount += 1;
        return;
    }
    if (temp[0] == 0 && temp[2] == 0) {
        zeroCount += 1 ;
        return;
    }
    if (temp[0] == 0 && temp[1] ==0) {
        oneCount += 1;
        return;
    }
    

    cut(x, y, width/3);
    cut(x, y + width/3, width/3);
    cut(x, y+ width*2/3, width/3);
    
    cut(x + width/3, y, width/3);
    cut(x + width/3, y+ width/3, width/3);
    cut(x + width/3, y+ width*2/3, width/3);
    
    cut(x + width*2/3, y, width/3);
    cut(x + width*2/3, y+ width/3, width/3);
    cut(x + width*2/3, y+ width*2/3, width/3);
    
}

int main(void) {
    int N;
    cin >> N;
    world = vector<vector<int>>(N, vector<int>(N, 0));

    for (int i=0;i<N;i++) {
        for (int j=0;j<N;j++) {
            cin >> world[i][j];
        }
    }

    cut(0, 0, N);
    cout << minusCount<<"\n";
    cout << zeroCount<<"\n";
    cout << oneCount<<"\n";
    
    


}