#include <iostream>
#include <vector>

using namespace std;

bool checked = false;

void DFS(int prev, int depth, vector<int> &isVisited, vector<vector<int>> &peopleMap) {
    isVisited[prev] = 1;
    if (depth == 5) {
        checked = true;
        return;
    }
    for(auto i: peopleMap[prev]) {
        if (isVisited[i] == 0) {
            DFS(i, depth + 1, isVisited, peopleMap);
            isVisited[i] = 0;
        }
    }

}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int people, count;
    cin >> people >> count;

    vector<vector<int>> peopleMap(people);
    vector<int> isVisited(people, 0);

    while (count--) {
        int a, b;
        cin >> a >> b;
        peopleMap[a].push_back(b);
        peopleMap[b].push_back(a);
    }

    for (int i=0;i <people;i++) {
        isVisited = vector<int>(people, 0);
        DFS(i, 1, isVisited, peopleMap);
        if (checked) break;
    }

    if (checked) cout << "1";
    else cout << "0";

}