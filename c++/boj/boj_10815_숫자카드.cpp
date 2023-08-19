#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> tempArr;

int findTarget(int targetNum) {
    int l = 0;
    int r = tempArr.size() - 1;
    
    while (l <= r) {
        int mid = (l + r) / 2;
        if (tempArr[mid] == targetNum) return 1;

        if (tempArr[mid] > targetNum) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int a;
    cin >> a;

    for(int i=0;i<a;i++) {
        int k;
        cin >> k;
        tempArr.push_back(k);
    }
    sort(tempArr.begin(), tempArr.end());
    int count;
    cin >> count;
    for(int i=0;i<count;i++) {
        int target;
        cin >> target;
        cout << findTarget(target) << " ";
    }
    
    return 0;
}