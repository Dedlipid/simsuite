#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include <getopt.h>
#include <cstdlib>
#include "DoublePendulum.h"
#include "Integrator.h"

struct SimulationOptions {
    std::unique_ptr<Integrator> integrator;
    std::unique_ptr<System> system;
    double gravity;
    double time_step = .005;
    double sim_time = 30;
    int simulation_steps = sim_time / time_step;
};

int main(int argc, char* argv[]) {
    SimulationOptions options;
    options.gravity = 9.81; // Default gravitational acceleration
    std::string integratorType = "leapfrog"; // Default integrator
    std::string systemType = "dblpndlm"; // Default system

    int opt;
    while ((opt = getopt(argc, argv, "i:s:g:")) != -1) {
        switch (opt) {
            case 'i':
                integratorType = optarg;
                break;
            case 's':
                systemType = optarg;
                break;
            case 'g':
                options.gravity = std::atof(optarg);
                break;
            default:
                std::cerr << "Usage: " << argv[0] << " [-i integrator] [-s system] [-g gravity]" << std::endl;
                return 1;
        }
    }

    // Set the integrator and system based on command-line arguments
    if (integratorType == "euler") {
        options.integrator = std::make_unique<EulerIntegrator>();
    } else if (integratorType == "leapfrog") {
        options.integrator = std::make_unique<LeapFrogIntegrator>();
    } else {
        std::cerr << "Unknown integrator type: " << integratorType << ". Defaulting to LeapFrog." << std::endl;
        options.integrator = std::make_unique<LeapFrogIntegrator>();
    }

    if (systemType == "dblpndlm") {
        options.system = std::make_unique<DoublePendulum>(2.0, 1.0, 1.5, 0.5, 0.0, 0.0, options.gravity);
    } else {
        std::cerr << "Unknown system type: " << systemType << ". Defaulting to DoublePendulum." << std::endl;
        options.system = std::make_unique<DoublePendulum>(2.0, 1.0, 1.5, 0.5, 0.0, 0.0, options.gravity);
    }

    // Grid search parameters
    double start_a1 = -.01;
    double end_a1 = .01;
    double start_a2 = .99;
    double end_a2 = 1.01;
    int num_points = 4; 
    double step_a1 = (end_a1 - start_a1) / (num_points - 1);
    double step_a2 = (end_a2 - start_a2) / (num_points - 1);
    // Clear the data directory
    system("rm ../data/*");

    for (int i = 0; i < num_points; ++i) {
        for (int j = 0; j < num_points; ++j) {
            double initial_a1 = start_a1 + i * step_a1;
            double initial_a2 = start_a2 + j * step_a2;
            int id = i * num_points + j;

            // Recreate the system with initial conditions
            options.system = std::make_unique<DoublePendulum>(4.0, 1.0, 1.5, 6.5, initial_a1, initial_a2, options.gravity);

            std::string filename = "../data/pendulum_data_" + std::to_string(id) + ".csv";

            // Open the file in overwrite mode
            std::ofstream outfile(filename, std::ios::trunc);
            if (!outfile.is_open()) {
                std::cerr << "Error opening file for writing!" << std::endl;
                return 1;
            }
            outfile << "time,a1,a2,v1,v2,initial_a1,initial_a2\n";
            
            int steps_per_loop = 25;

            for (int step = 0; step < (options.simulation_steps) / steps_per_loop; ++step) {
                double current_time = step * options.time_step * steps_per_loop;
                options.integrator->integrate(*options.system, options.time_step, steps_per_loop);
                auto& states = (options.system)->q;
                auto& velocities = (options.system).p;
                outfile << current_time << "," << states[0] << "," << states[1] << 
                "," << velocities[0] << "," << velocities[1] << "," << initial_a1 << 
                "," << initial_a2 << "\n";
            }

            outfile.close();
        }
    }

    return 0;
}
