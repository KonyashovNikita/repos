// Файл main.cpp
#include "getput.h"
#include "Raz.h"
#include <iostream>
using namespace std;

int main(){
    double x, y, a, t;
    int n; // Номер ветки
    getXYA(x, y, a); // Вызов функции ввода исходных данных
    int choice; // Вариант выбора решения
    cout<<" Каким способом решать задачу?\n";
    cout<<" 1 - с вложенными разветвлениями ";
    cout<<" без дополнительных функций max и min \n ";
    cout<<"2 - со своими функциями minMy и maxMy \n ";
    cout<<" Что выбираете 1 или 2 ?\n ";
    cin>>choice;
    switch(choice){
        case 1:
            t = Razv(x, y, a, n);
            break;
        case 2:
            t = Razm(x, y, a, n);
            break;
        default:
            cout<<" Вы ввели что-то не то! ";
            cout<<endl;
            return 0;
    }
    putTN(t, n); // Вызов функции вывода результатов
    return 0;
}