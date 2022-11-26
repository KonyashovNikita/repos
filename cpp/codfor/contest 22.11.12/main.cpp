#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int k;
    cin >> k;
    for (int i  = 0; i < k; i++){
        double n;
        cin >> n;
        cout << int(ceil(n/2)) << endl;
    }
}