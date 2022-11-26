#include <iostream>
#include <cmath>
#include "func.h"
#include "cincout.h"
using namespace std;
#define _USE_MATH_DEFINES

int main(){
    double a, b, c, ang_a, ang_b, ang_c;
    CIN(a, b, c);
    calc_ang(a, b, c, ang_a, ang_b, ang_c);
    COUT(ang_a, ang_b, ang_c);
}