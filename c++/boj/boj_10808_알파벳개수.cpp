// https://www.acmicpc.net/problem/10808

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    string target;
    cin >> target;

    int arr[26] = {0, };
    for(char t: target) {
        arr[t - 'a'] += 1;
    }
    for(int i=0;i<26;i++) cout << arr[i] << " ";

    return 0;
}