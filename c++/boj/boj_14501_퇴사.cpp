#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int totalHap = 0;
int N;
vector<pair<int, int>> world(0);

int max_num(int x, int y) {
    if (x > y) return x;
    return y;
}

void dfs(int day, int currentHap) {
    if (day >= N) {
        totalHap = max_num(totalHap, currentHap);
        return;
    }

    if (day + world[day].first <= N) {
        dfs(day + world[day].first, currentHap + world[day].second);
    }
    //  else {
        dfs(day+1, currentHap);
    // }
    
}

int main(void) {
    cin >> N;

    for (int i=0;i<N;i++) {
        pair<int, int> temp;
        cin >> temp.first >> temp.second;
        world.push_back(temp);
    }

    vector<int> answer(N, 0);
    answer[0] = world[0].second;

    dfs(0, 0);
    cout << totalHap;

}
