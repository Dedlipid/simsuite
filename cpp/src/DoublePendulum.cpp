#include "DoublePendulum.h"
#include <iostream>
#include <cmath>

DoublePendulum::DoublePendulum(double length1, double length2, double mass1, double mass2, double angle1, double angle2, 
                               double angularVelocity1, double angularVelocity2, double gravity)
: props{length1, length2, mass1, mass2, gravity}, q{angle1, angle2, angularVelocity1, angularVelocity2, 0, 0}
{
    // Initialization is already done in the member initializer list
}

void DoublePendulum::computeAccelerations() {
    auto l1 = props[0];
    auto l2 = props[1];
    auto m1 = props[2];
    auto m2 = props[3];
    auto g = props[4];
    
    double num1 = -g * (2 * m1 + m2) * sin(q[0]);
    double num2 = -m2 * g * sin(q[0] - 2 * q[1]);
    double num3 = -2 * sin(q[0] - q[1]) * m2;
    double num4 = q[3] * q[3] * l2 + q[2] * q[2] * l1 * cos(q[0] - q[1]);
    double den = l1 * (2 * m1 + m2 - m2 * cos(2 * q[0] - 2 * q[1]));
    q[4] = (num1 + num2 + num3 * num4) / den;

    num1 = 2 * sin(q[0] - q[1]);
    num2 = (q[2] * q[2] * l1 * (m1 + m2));
    num3 = g * (m1 + m2) * cos(q[0]);
    num4 = q[3] * q[3] * l2 * m2 * cos(q[0] - q[1]);
    den = l2 * (2 * m1 + m2 - m2 * cos(2 * q[0] - 2 * q[1]));
    q[5] = (num1 * (num2 + num3 + num4)) / den;
}

void DoublePendulum::printState() const {
    std::cout << q[0] << "," << q[1] << "," << q[2] << "," << q[3] << std::endl;
}

std::vector<double> DoublePendulum::getStates() {
    return std::vector<double>{q[0], q[1], q[2], q[3]};
}