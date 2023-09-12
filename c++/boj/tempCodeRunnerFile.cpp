#include <iostream>
#include <vector>

using namespace std;



void DFS(int current, vector<int> &isVisited) {
    isVisited[current] = 1;
    for (int i=0;i<isVisited.size();i++) {
        if (isVisited[i] == 0 && current != i) {
            DFS(i, isVisited);
        }
    }

}

int main(void) {
    int people, count;
    cin >> people >> count;

    vector<vector<int>> peopleMap(people, vector<int>(people, 0));
    vector<int> isVisited(people, 0);

    while (count--) {
        int a, b;
        cin >> a >> b;
        peopleMap[a][b] = 1;
        peopleMap[b][a] = 1;
    }

    DFS(0, isVisited);

    int sum=0;
    for(auto i: isVisited) {
        sum += i;
    }
    if (sum == isVisited.size()) cout << "1";
    else cout << "0";

}