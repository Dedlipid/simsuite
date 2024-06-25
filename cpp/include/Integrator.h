#ifndef INTEGRATOR_H
#define INTEGRATOR_H

#include "System.h"

class Integrator {
public:
    virtual void integrate(System& system, double timeStep, int steps) = 0;
};

class EulerIntegrator : public Integrator {
public:
    void integrate(System& system, double timeStep, int steps) override;
};

class LeapFrogIntegrator : public Integrator {
public:
    void integrate(System& system, double timeStep, int steps) override;
};

#endif // INTEGRATOR_H
