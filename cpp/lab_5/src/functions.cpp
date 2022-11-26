// Файл с функциями решения задачи, реализующими функциональные алгоритмы
#include "functions.h"
#include <cmath>

// 1-ый способ – стандартное разветвление с логическими операциями
bool resh1(double x, double y){
    if (abs(x) <= 1 && sqrt(1 - x*x) >= y && y >= 2*abs(x) - 2){
        return true;
    }
    else{
        return false;
    }
}

// 2-ой способ – вложенные разветвления только с помощью операций отношения
bool resh2(double x, double y){
    if (abs(x) <= 1)
        if (sqrt(1 - x*x) >= y)
            if (y >= 2*abs(x) - 2)
                return true;
    return false;
}

// 3-ой способ – только сложное логические выражения
bool resh3(double x, double y){
    return abs(x) <= 1 && sqrt(1 - x*x) >= y && y >= 2*abs(x) - 2;
}