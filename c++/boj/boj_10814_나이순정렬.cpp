#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool comp(pair<int, string> a, pair<int, string> b) {
    return a.first < b.first;
}

int main(void) {
    int count;
    cin >> count;

    pair<int, string> mem;
    vector<pair<int, string>> mem_map;

    while (count--) {
        cin >> mem.first >> mem.second;
        mem_map.push_back(mem);
    }

    stable_sort(mem_map.begin(), mem_map.end(), comp);

    for(int i=0;i<mem_map.size();i++) {
        cout << mem_map.at(i).first << " " << mem_map.at(i).second<<"\n";
    }


}