#include <iostream>
#include <vector>

using namespace std;

void swap(vector<int>& target, int left, int right) {
    int temp = target[right];
    target[right] = target[left];
    target[left] = temp;
}

int main(void) {
    int N, M;
    cin >> N >> M;

    vector<int> temp(N);
    for(int i=0;i<N;i++) {
        temp[i] = i+1;
    }
    for(int i=0;i<M;i++) {
        int a, b;
        cin >> a >> b;
        swap(temp, temp[a-1], temp[b-1]);
    }

    for(auto i: temp) cout << i << " ";

}