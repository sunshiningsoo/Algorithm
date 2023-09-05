#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> fiboZeroMap(41, 0);
vector<int> fiboOneMap(41, 0);

int zeroCount = 0;
int oneCount = 0;

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main(void) {
    int count;
    cin >> count;
    fiboZeroMap[0] = 1;
    fiboOneMap[1] = 1;

    for (int i=2;i<41;i++) {
        fiboZeroMap[i] = fiboZeroMap[i-2] + fiboZeroMap[i-1];
        fiboOneMap[i] = fiboOneMap[i-2] + fiboOneMap[i-1];
    }

    while (count--) {
        int current;
        cin >> current;
        cout << fiboZeroMap[current] << " "<< fiboOneMap[current]<< "\n";
    }

}