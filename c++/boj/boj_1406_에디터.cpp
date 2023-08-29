#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(void) {
    string word;
    cin >> word;
    int num;
    cin >> num;
    list<char> L;

    for (int i=0;i<word.length();i++) L.emplace_back(word[i]);
    list<char>::iterator cursor = L.end();
    
    for (int i=0;i<num;i++) {
        char target;
        cin >> target;    

        if (target == 'L') {
            if (cursor != L.begin()) cursor--;
        } else if (target == 'D') {
            if (cursor != L.end()) cursor++;
        } else if (target == 'B') {
            if (cursor != L.begin()) {
                cursor--;
                cursor = L.erase(cursor);
            }
        } else {
            char k;
            cin >> k;
            L.insert(cursor, k);
        }
    }
    
    for(auto i: L) cout << i;

}