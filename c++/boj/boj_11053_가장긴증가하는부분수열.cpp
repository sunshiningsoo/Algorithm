#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(void) {
    int count;
    cin >> count;
    vector<int> numList;
    
    vector<int> dp(count, 1);

    for(int i=0;i<count;i++) {
        int temp;
        cin >> temp;
        numList.push_back(temp);
    }

    for (int i=1;i<count;i++) {
        for (int j=0;j<i;j++) {
            if (numList[j] < numList[i]) {
                if (dp[j] >= dp[i]) {
                    dp[i] = dp[j]+1;
                    
                }
            }
        }
    }

    cout << *max_element(dp.begin(), dp.end());

}