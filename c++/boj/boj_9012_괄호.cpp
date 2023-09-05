#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(void) {
    int count;
    cin >> count;

    while(count--) {
        string word;
        bool checked = false;
        cin >> word;
        vector<int> temp;
        for(auto& alpha: word) {
            if (alpha == ')') {
                if (temp.size() != 0) temp.erase(temp.begin()+temp.size()-1);
                else if (temp.size() == 0) {
                    cout<<"NO\n";
                    checked = true;
                    break;
                }
            } else if (alpha == '(') {
                temp.push_back(1);
            }
        }
        if (checked == false) {
            if (temp.size() == 0) {
            cout <<"YES\n";
        } else {
            cout << "NO\n";
        } 
        }
    }
    

}