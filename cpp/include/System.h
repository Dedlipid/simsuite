#ifndef SYSTEM_H
#define SYSTEM_H

#include <vector>

class System {
public:
    virtual void computeAccelerations() = 0;
    virtual void printState() const = 0;

    virtual std::vector<double>& getStates() = 0;
    virtual std::vector<double>& getVelocities() = 0;
    virtual std::vector<double>& getAccelerations() = 0;
};

#endif // SYSTEM_H
