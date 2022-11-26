#include <iostream>
#include <cmath>
using namespace std;
int prinnt(int n, int a=1, int b=2, int c=3){
    if (n == 1){
        cout << n << ' ' << a << ' ' << c << '\n';
        return 0;
    }
    else{
        prinnt(n-1, a, c, b);
        cout << n << ' ' << a << ' ' << c << '\n';
        prinnt(n-1, b, a, c);
}
}
int main() {
    int n;
    cin >> n;
    prinnt(n);
}