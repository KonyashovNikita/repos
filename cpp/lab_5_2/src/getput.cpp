// Файл getput.cpp с функциями ввода и вывода
#include "getput.h"
#include <iostream>

using namespace std;

// Определение функции ввода
void getXYA(double& x, double& y, double& a){
    setlocale(LC_ALL,"rus");
    cout << "Введите x, y, a\n";
    cin >> x >> y >> a;
}

// Определение функции вывода
void putTN(double t, int n){
    setlocale(LC_ALL,"rus");
    cout << "Ответ t= " << t << endl;
    cout << "Номер ветки разветвления " << n << endl;
}