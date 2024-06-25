#ifndef SYSTEMS_H
#define SYSTEMS_H

typedef struct {
    double *p;   // Position array
    double *q;   // Velocity array
    double *acc; // Acceleration array
    double *prop;  // Array of system properties
    int size[2]; // Number of elements in the system and size of properties
} system_t;

void pendulum_acc(system_t *system);
void double_pendulum_acc(system_t *system);

system_t* create_pendulum_system(double length, double g, double initial_angle, double initial_velocity);
system_t* create_double_pendulum_system(double m1, double m2, double l1, double l2, double g, 
                                        double initial_theta1, double initial_theta2, double initial_omega1, double initial_omega2);
void free_system(system_t *system);

#endif
