#include "Integrator.h"
#include <stddef.h>

void EulerIntegrator::integrate(System& system, double timeStep, int steps) {
    for (int i = 0; i < steps; ++i) {
        system.computeAccelerations();
        auto& v = system.getStates();

        // Velocity update
        for (size_t j = 0; j < v.size(); ++j) {
            v[j] += acc[j] * timeStep;
        }

        // Position update
        for (size_t j = 0; j < a.size(); ++j) {
            a[j] += v[j] * timeStep;
        }
    }
}

void LeapFrogIntegrator::integrate(System& system, double timeStep, int steps) {
    auto& v = system.getVelocities();
    auto& a = system.getStates();
    auto& acc = system.getAccelerations();

    for (int i = 0; i < steps; ++i) {
        system.computeAccelerations();

        // Half-step velocity update
        for (size_t j = 0; j < v.size(); ++j) {
            v[j] += 0.5 * acc[j] * timeStep;
        }

        // Full-step position update
        for (size_t j = 0; j < a.size(); ++j) {
            a[j] += v[j] * timeStep;
        }

        // Recompute accelerations with updated positions
        system.computeAccelerations();

        // Half-step velocity update
        for (size_t j = 0; j < v.size(); ++j) {
            v[j] += 0.5 * acc[j] * timeStep;
        }
    }
}
