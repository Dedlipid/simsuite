#ifndef DOUBLEPENDULUM_H
#define DOUBLEPENDULUM_H

#include "System.h"
#include <vector>

class DoublePendulum : public System {
public:
    DoublePendulum(double length1, double length2, double mass1, double mass2, double angle1, double angle2, 
                   double angularVelocity1 = 0.0, double angularVelocity2 = 0.0, double gravity = 9.81);

    void computeAccelerations() override;
    void printState() const override;
    
    std::vector<double>& getStates() override;
    std::vector<double>& getVelocities() override;
    std::vector<double>& getAccelerations() override;

    // Properties of the pendulum (length1, length2, mass1, mass2, gravity) 
    double props[5]; 
    // phase space coordinates (angle1, angle2, angular velocity1, angular velocity2, angular acceleration1, angular acceleration2)
    double q[6]; 
};

#endif // DOUBLEPENDULUM_H
