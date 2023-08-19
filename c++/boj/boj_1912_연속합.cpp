//
// Created by 박성수 on 2023/08/20.
//
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int arrLen;
    cin >> arrLen;
    vector<int> v;
    for(int i=0;i<arrLen;i++) {
        int k;
        cin >> k;
        v.push_back(k);
    }
    vector<int> temp(v.size(), 0);

    temp[0] = v[0];
    for (int i=1; i<v.size();i++) {
        temp[i] = max(temp[i-1] + v[i], v[i]);
    }
    printf("%d", *max_element(temp.begin(), temp.end()));


    return 0;
}