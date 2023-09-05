#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void) {
    int count;
    cin >> count;
    
    while (count--) {
        int temp;
        cin >> temp;
        vector<int> map(temp+1, 0);
        map[1] = 1;
        map[2] = 2;
        map[3] = 4;
        for(int i=4;i<temp+1;i++) {
            map[i] = map[i-3] + map[i-2] + map[i-1];
        }
        cout << map[temp] << "\n";
    }
}