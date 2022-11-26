#include "getput.h"
#include "functions.h"
#include <iostream>
using namespace std;

int main(){
    double x, y;
    bool b; // Признак попадания в заданную область
    getXY(x, y); // Вызов функции ввода исходных данных
    cout << "решение 1 методом";
    b = resh1(x, y); // Вызов 1-й функции решения
    put(b, x, y); // Вызов функции вывода результатов
    cout << "решение 2 методом";
    b = resh2(x, y);// Вызов 2-й функции решения
    put(b, x, y);
    cout << "решение 3 методом";
    b = resh3(x, y);// Вызов 3-й функции решения
    put(b, x, y);
    
}