#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void) {
    int N, X;
    vector<int> temp;
    cin >> N >> X;
    for (int i=0;i<N;i++) {
        int k;
        cin >> k;
        if (k < X) cout << k << " ";
    }
}