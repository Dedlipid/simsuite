#include "integrators.h"

void euler_step(system_t *system, double dt, int steps) {
    for (int i = 0; i < system->size[0]; i++) {
        system->q[i] += system->acc[i] * dt;
        system->p[i] += system->q[i] * dt;
    }
}
