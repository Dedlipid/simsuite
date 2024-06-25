#include <stdio.h>
#include <stdlib.h>
#include "integrators.h"
#include "systems.h"

void simulate(system_t *system, void (*update_acc)(system_t *),
              int steps, double dt, const char *output_filename)
{
    FILE *file = fopen(output_filename, "w");

    for (int i = 0; i < steps; i++)
    {
        update_acc(system);
        euler_step(system, dt, 1);
        for (int j = 0; j < system->size[0]; j++)
        {
            fprintf(file, "%lf %lf %lf ", system->p[j], system->q[j], system->acc[j]);
        }
        fprintf(file, "\n");
    }

    fclose(file);
}

int main()
{
    double length = 1.0;
    double g = 9.81;
    system_t *pendulum = create_pendulum_system(length, g, 0.1, 0.0);

    double m1 = 1.0, m2 = 1.0, l1 = 1.0, l2 = 1.0;
    system_t *double_pendulum = create_double_pendulum_system(m1, m2, l1, l2, g, 0.1, 0.0, 0.0, 0.0);

    int steps = 1000;
    double dt = 0.01;

    simulate(pendulum, pendulum_acc, steps, dt, "../../data/pendulum_output.txt");
    simulate(double_pendulum, double_pendulum_acc, steps, dt, "../../data/double_pendulum_output.txt");

    free_system(pendulum);
    free_system(double_pendulum);

    return 0;
}
