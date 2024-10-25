import pybullet as p
import pybullet_data
import time
import numpy as np
import matplotlib.pyplot as plt

def run_simulation(times,positions,velocities):
    # Initialize physics simulation
    physicsClient = p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Use PyBullet data for plane

    # Load a simple plane and a sphere (as an example)
    plane_id = p.loadURDF("plane.urdf")
    sphere_id = p.loadURDF("sphere2.urdf", [0, 0, 1], p.getQuaternionFromEuler([0, 0, 0]))

    # Simulation parameters
    time_step = 1 / 240.0
    p.setGravity(0, 0, -9.81)

    # Initialize Matplotlib graph
    plt.ion()  # Interactive mode on
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))

    start_time = time.time()

    # Run simulation loop
    for i in range(1000):
        p.stepSimulation()

        # Get current time
        current_time = time.time() - start_time
        times.append(current_time)

        # Get sphere state: position and velocity
        pos, ori = p.getBasePositionAndOrientation(sphere_id)
        vel, ang_vel = p.getBaseVelocity(sphere_id)

        positions.append(pos[2])  # Only track Z-axis position
        velocities.append(vel[2])  # Only track Z-axis velocity

        # Plotting Position
        ax[0].cla()  # Clear the subplot
        ax[0].plot(times, positions, label="Position (Z-axis)", color="blue")
        ax[0].set_title("Position over Time")
        ax[0].set_xlabel("Time (s)")
        ax[0].set_ylabel("Position (m)")
        ax[0].legend()
        ax[0].grid(True)

        # Plotting Velocity
        ax[1].cla()  # Clear the subplot
        ax[1].plot(times, velocities, label="Velocity (Z-axis)", color="green")
        ax[1].set_title("Velocity over Time")
        ax[1].set_xlabel("Time (s)")
        ax[1].set_ylabel("Velocity (m/s)")
        ax[1].legend()
        ax[1].grid(True)

        # Draw the plot
        plt.pause(0.01)

        time.sleep(time_step)

    # Keep the plot open
    plt.ioff()
    plt.show()

    # Disconnect physics simulation
    p.disconnect()

# Run the simulation with real-time graph
run_simulation([],[],[])
