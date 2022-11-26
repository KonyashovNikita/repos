#include <iostream>
using namespace std;

bool is_diverse(string s){
    int l = 0;
    int kol[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = 0; i < s.length(); i++){
        int a = int(s[i]) - '0';
        if (kol[a] == 0) l += 1;
        kol[a] += 1;
    }
    int maxim = 0;
    for (int i = 0; i < 10; i++){
        if (kol[i] > maxim) maxim = kol[i];
    }
    return maxim <= l;
}

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n, kol = 0;
        string s;
        cin >> n >> s;
        for (int k = 0; k < n; k++){
            for (int m = 1; m < min(n-k+1,101); m++){
                if (is_diverse(s.substr(k,m))){
                    kol++;
                }
            }
        }
        cout << kol << endl;
}
}