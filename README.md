# Brownian Motion Simulation

## Overview
This project simulates the random movement of particles in a fluid, a phenomenon known as Brownian Motion. Brownian Motion describes the random, erratic behavior of microscopic particles suspended in a fluid, as they constantly collide with the much smaller molecules of the fluid. This simulation models that behavior on a macro scale, using a point/circle to represent the particle moving within a square boundary or "arena."

## Brownian Motion
Brownian Motion is a fundamental concept in physics and chemistry, illustrating how microscopic particles move through a medium. The motion is caused by the collision of the particles with the atoms or molecules of the fluid in which they are suspended. This project uses a simplified model to simulate this complex process, offering a visual and interactive way to understand and observe Brownian Motion.

## Project Implementation
The simulation is implemented in Python, utilizing the numpy library for numerical computations and matplotlib for visualization and animation. The simulated "particle" (or robot, in the context of this application) starts in the middle of the arena and moves in a straight line until it hits the boundary, at which point it randomly changes direction and continues moving.

### Key Features:
- A point/circle represents the robot or particle.
- The arena is a square boundary within which the particle moves.
- Particle starts in the middle and moves in a straight line at the beginning.
- Upon collision with a boundary, the particle randomly changes direction.

### Links
- **Simulation Code:** [brownian_motion.py](https://github.com/Henrysssong/brownian_motion/blob/main/brownian_motion.py)
- **Simulation Output (GIF):** ![Brownian Motion Simulation](https://github.com/Henrysssong/brownian_motion/blob/main/brownian_motion.gif)

## Getting Started
To run this simulation on your own machine, ensure you have Python installed, along with the numpy and matplotlib libraries. Clone this repository, navigate to the directory containing `brownian_motion.py`, and run the script:

```bash
python brownian_motion.py
