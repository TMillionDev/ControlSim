import pybullet as p
import pybullet_data
import time

# Connect to PyBullet and load a simulation
p.connect(p.GUI)  # Use p.DIRECT for a headless simulation
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Set gravity (not crucial here but good practice)
p.setGravity(0, 0, -9.8)

# Create the ground plane
plane_id = p.loadURDF("plane.urdf")

# Create a simple robot with a revolute joint (hinge joint)
# Load a basic URDF with a revolute joint
# This URDF creates a single link connected by a joint
robot_id = p.loadURDF(
    "arm.urdf",  # You can replace this with your URDF containing a revolute joint if you want custom behavior
    basePosition=[0, 0, 4]
)

# Set the joint motor control to apply a velocity to a specific joint index (0 in this case)
p.setJointMotorControl2(
    bodyUniqueId=robot_id,
    jointIndex=0,  # Index of the joint to control
    controlMode=p.VELOCITY_CONTROL,
    targetVelocity=1.0,  # Set the desired joint rotation speed (radians per second) 
    force=500
)
print("")

# Run the simulation loop
for _ in range(1000):
    p.stepSimulation()
    time.sleep(1. / 240.)  # Maintain a real-time simulation speed

# Disconnect the simulation
p.disconnect()
