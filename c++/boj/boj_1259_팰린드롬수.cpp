#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
    while (true) {
        bool checked = false;
        string str;
        cin >> str;
        if (str == "0") break;
        for (int i=0;i<str.length()/2;i++) {
            if (str[i] != str[str.length()-i-1]) {
                cout << "no\n";
                checked = true;
                break;
            }
        }
        if (checked == false) {
            cout << "yes\n";
        }
    }
}
