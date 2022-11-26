#include "func.h"
#include <cmath>
#define _USE_MATH_DEFINES

double angle(double a, double b, double c){
    double p = (a + b + c) / 2;
    double ang_a = atan(sqrt(((p - c) * (p - b))/((p - a) * p))) * 360 / M_PI;
    return ang_a;
}

void calc_ang(double a, double b, double c, double& ang_a, double& ang_b, double& ang_c){
    ang_a = angle(a, b, c);
    ang_b = angle(b, a, c);
    ang_c = angle(c, a, b);
}