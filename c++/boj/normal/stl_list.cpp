#include <iostream>
#include <list>

using namespace std;

int main(void) {
    list<int> L = {1, 2};
    list<int>::iterator tempIter = L.begin();
    while (tempIter != L.end()) {
        cout << *tempIter <<" ";
        tempIter++;
        
    }

    /* L.front(), L.back()은 원소를 직접 참조함 */

    /* L.begin()은 맨 앞의 원소를 가리키는 iter */
    /* L.end() 는 맨 마지막의 다음 원소를 가리키는 iter */

    // for(auto l: L) cout << l << " ";
    // printf("%d\n", L.size()); // 갯수 return
    // printf("%d\n", L.front()); // 제일 앞 값 return

    // printf("%d\n", *L.begin()); // 제일 앞 iterator return
}