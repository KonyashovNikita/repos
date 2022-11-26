// Файл getput.cpp с функциями ввода и вывода
#include "getput.h"
#include <iostream>

using namespace std;

// Определение функции ввода
void getXY(double& x, double& y){
    cout << "Введите значение x:" ;
    cin >> x;
    cout << "Введите значение y:";
    cin >> y;
}

// Определение функции вывода
void put(double b, double x, double y){
    setlocale(LC_ALL,"rus");
    cout<<" Точка с координатами ( "<<x<<" ,"<<y<<" )"<<endl;
    if (b) cout<<"попала в заданную область"<<endl;
    else cout<<"не попала в заданную область"<<endl;
}