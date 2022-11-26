// Файл Raz с функциями Razv, Razm, maxMy и minMy
#include "Raz.h"
#include <cmath>

// Определение ф-ции с вложенными разветвлениями,без дополнительных функций
double Razv(double x, double y, double a, int& n){
    double t; // Локальная переменная ФУНКЦИИ
    if (x*y < 0){
        t = 1 - sqrt(x*x + a);
        if (x > y) t *= x;
        else t *= y;
        n = 1;
    }
    else{
        if (x*y > 2){
            t = x*x;
            double t1 = sin(y), t2 = cos(a*x);// Локальные переменные БЛОКА
            if (t1 < t) t = t1;
            if (t2 < t) t = t2;
            n = 2;
        }
        else{
            t = a*a + x / y;
            n = 3;
        }
        return t;
    }
}

// Описания (прототипы) функций maxMy и minMy
double maxMy(double, double);
double minMy(double, double);

// Определение ф-ции с вложенными разветвлениями,использующей maxMy и minMy
double Razm(double x, double y, double a, int& n){
    if (x*y < 0){
        n = 1;
        return (1 - sqrt(x*x + a)) * maxMy(x, y);
    }
    else{
        if (x*y > 2){
            n = 2;
            return minMy(x*x, minMy(sin(y), cos(a*y)));
        }
        else{
            n = 3;
            return a*a + x/y;
        }
    }
}

// Определение функции maxMy
double maxMy(double x, double y){
    double f;
    if (x > y) f = x; else f = y;
    return f;
}

// Определение функции minMy
double minMy(double x, double y){
    double f;
    if (x < y) f = x; else f = y;
    return f;
}