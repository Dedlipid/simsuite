#ifndef INTEGRATORS_H
#define INTEGRATORS_H

#include "systems.h"

void euler_step(system_t *system, double dt, int steps);

#endif
