#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int count;
vector<int> original;
vector<int> isVisited;
int hap = 0;

int hapReturn(vector<int> temp) {
    int sum=0;
    for(int i=0; i<temp.size();i++) {
        sum += temp[i];
    }
    return sum;
}

void DFS(int prev, vector<int> &isVisited, int currentHap) {
    isVisited[prev] = 1;
    if (hapReturn(isVisited) == ::count) {
        // cout << currentHap<< " ";
        if (currentHap > hap) hap = currentHap;
        return;
    }
    for (int i=0;i<isVisited.size();i++) {
        if (isVisited[i] == 0) {
            DFS(i, isVisited, currentHap + ((original[prev] - original[i]) > 0 ? (original[prev] - original[i]) : -1*(original[prev] - original[i])));
            isVisited[i] = 0;
        }
    }
}

int main(void) {
    cin >> ::count;
    original = vector<int>(::count, 0);
    isVisited = vector<int>(::count, 0);
    for (int i=0;i<::count;i++) cin >> original[i];

    for (int i=0;i<::count;i++) {
        if (isVisited[i] == 0) {
            DFS(i, isVisited, 0);
            isVisited[i] = 0;
        }
    }
    cout << hap;
}