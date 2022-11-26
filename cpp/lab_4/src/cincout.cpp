#include "cincout.h"
#include <iostream>
using namespace std;

void CIN(double& a, double& b, double& c){
    cout << "Введите стороны треугольника abc, чтобы посчитать его углы" << endl << "Введите сторону a: ";
    cin  >> a;
    cout << "Введите сторону b: ";
    cin >> b;
    cout << "Введите сторону C: ";
    cin >> c;
}
void COUT(double a, double b, double c){
    if (a == a && b == b && c == c){
        cout << "Угол лежащий напротив стороны a равен: " << a << endl;
        cout << "Угол лежащий напротив стороны b равен: " << b << endl;
        cout << "Угол лежащий напротив стороны c равен: " << c << endl;
    }
    else{
        cout << "Такого треугольника не существует!" << endl;
    }
}