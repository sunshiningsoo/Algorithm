#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int target;
    cin >> target;
    cout << target;
    
    vector<vector<int>> temp(target + 1, vector<int>(target+1, 0));
    temp[0][0] = 1;
    for(int i=0;i<target+1;i++) temp[i][0] = 1;
    
    for (int i=1;i<target+1;i++) {
        for (int j=1;j<target+1;j++) {
            temp[i][j] = temp[i-1][j-1] + temp[i-1][j];
        }
    }

    for(int i=0;i<target+1;i++) {
        for(int j=0;j<target+1;j++) {
            cout << temp[i][j] << " ";
        }
        cout << endl;
    }

    int hap = 0;
    for (int i=0;i<target+1;i++) {
        hap += temp[target][i];
    }
    // int max = *max_element(temp[target].begin(), temp[target].end());
    // cout << max;

    cout << hap;
}