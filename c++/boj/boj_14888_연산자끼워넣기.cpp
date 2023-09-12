#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int max_num = -1000000000;
int min_num = 1000000000;
vector<int> numbers(0);
vector<int> opsFlatten(0);
int N;

void DFS(int current, int currentHap, vector<int> &isVisited) {
    if (current == N) {
        max_num = max_num < currentHap ? currentHap : max_num;
        min_num = min_num > currentHap ? currentHap : min_num;
        return;
    }
    for(int i=0;i<opsFlatten.size();i++) {
        if (isVisited[i]==1) continue;
        isVisited[i] = 1;
        if (opsFlatten[i]==1) DFS(current+1, currentHap + numbers[current], isVisited);
        else if (opsFlatten[i]==2) DFS(current+1, currentHap - numbers[current], isVisited);
        else if (opsFlatten[i]==3) DFS(current+1, currentHap * numbers[current], isVisited);
        else if (opsFlatten[i]==4) DFS(current+1, currentHap / numbers[current], isVisited);
        isVisited[i] = 0;
    }
}

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    numbers = vector<int>(N, 0);
    int ops[4] = {0,};
    for(int i=0;i<N;i++) cin >> numbers[i];
    for(int i=0;i<4;i++) {
        cin >> ops[i];
        for (int j=0;j<ops[i];j++) {
            if (i==0) opsFlatten.push_back(1); // +
            else if (i==1) opsFlatten.push_back(2); // -
            else if (i==2) opsFlatten.push_back(3); // *
            else if (i==3) opsFlatten.push_back(4); // /
        }
    }
    vector<int> isVisited(opsFlatten.size(), 0);

    for(int i=0;i<numbers.size();i++) {
        // isVisited[i] = 1;
        DFS(1, numbers[0], isVisited);
        // isVisited[i] = 0;
    }
    cout << max_num<<"\n";
    cout << min_num<<"\n";

}