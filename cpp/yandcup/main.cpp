#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <iostream>
#pragma comment(linker, "/STACK:2222222222")

using namespace std;

typedef long long ll;
typedef long double ld;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        ll a;
        int b, r, k;
        cin >> a >> b;
        r = int(log10(a));
        int max_d = int(9/b) + 1;
        int num = max(int(a/pow(10,r)), 1)*pow(max_d, r-1);
        int temp = 1;
        while (a != 0){
            temp *= (int((a % 10)/b) + 1);
            a = int(a/10);
        }
        num += temp;
        cout << temp << endl;
    }
}