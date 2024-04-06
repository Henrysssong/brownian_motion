import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arena_size = 100
robot_position = np.array([arena_size / 2, arena_size / 2])
step_size = 1
movement_direction = np.array([1, 0])

def move_robot(position, direction):
    new_position = position + step_size * direction
    
    # Check for collision with boundaries
    collision = False
    if new_position[0] <= 0 or new_position[0] >= arena_size:
        direction[0] = -direction[0]
        collision = True
    if new_position[1] <= 0 or new_position[1] >= arena_size:
        direction[1] = -direction[1]
        collision = True

    if collision:
        # Apply some randomness to the new direction
        angle = np.random.uniform(-np.pi/4, np.pi/4)
        cos_angle = np.cos(angle)
        sin_angle = np.sin(angle)
        new_direction = np.array([
            cos_angle * direction[0] - sin_angle * direction[1],
            sin_angle * direction[0] + cos_angle * direction[1]
        ])
        new_direction /= np.linalg.norm(new_direction)
        new_position = position + step_size * new_direction
        return new_position, new_direction
    else:
        return new_position, direction

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, arena_size)
ax.set_ylim(0, arena_size)
robot, = ax.plot(robot_position[0], robot_position[1], 'bo')

# Animation function
def animate(i):
    global robot_position, movement_direction
    robot_position, movement_direction = move_robot(robot_position, movement_direction)
    robot.set_data(robot_position[0], robot_position[1])
    return robot,

# Run the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=50, blit=True)
plt.show()
