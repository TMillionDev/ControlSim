import math
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import pybullet as p
import time
import pybullet_data
import time
import os


from simple_pid import PID

running_simulation = True
def run_simulation(kP, kI, kD, sp):
    global running_simulation
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)
        
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))
    
    planeId = p.loadURDF("plane.urdf")
    bodyApos = [0, 0, 4]
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])
    
    bodyA = p.loadURDF("arm.urdf", bodyApos, startOrientation)
    p.changeDynamics(bodyA, -1, lateralFriction=0.1, spinningFriction=0.1, rollingFriction=0.01)
    
    pos = [0]
    vels=[0]
    t=[0]
    pid = PID(kP, kI, kD)
    pid.setpoint = sp + (0.01*math.pi)
    pid.sample_time=0.01

    plt.ion()  # Interactive mode on

    if (sp < (2*math.pi)):
        while (p.getJointState(bodyUniqueId=bodyA,jointIndex=4)[0] < (sp-(0.01*math.pi))):
            t.append(t[len(t)-1] + pid.sample_time)
            velocity = pid(pos[len(pos) - 1])
            vels.append(velocity)
            pos.append(p.getJointState(bodyUniqueId=bodyA,jointIndex=4)[0])
            p.setJointMotorControl2(bodyUniqueId=bodyA, jointIndex=4, controlMode=p.VELOCITY_CONTROL, targetVelocity=velocity)
            print(p.getJointState(bodyUniqueId=bodyA,jointIndex=4))
            p.stepSimulation()

            ax[0].cla()  # Clear the subplot
            ax[0].plot(t, pos, label="Position (Z-axis)", color="blue")
            ax[0].set_title("Position over Time")
            ax[0].set_xlabel("Time (s)")
            ax[0].set_ylabel("Position (radians)")
            ax[0].legend()
            ax[0].grid(True)

            # Plotting Velocity
            ax[1].cla()  # Clear the subplot
            ax[1].plot(t, vels, label="Velocity (Z-axis)", color="green")
            ax[1].set_title("Velocity over Time")
            ax[1].set_xlabel("Time (s)")
            ax[1].set_ylabel("Velocity (m/s)")
            ax[1].legend()
            ax[1].grid(True)

            plt.pause(pid.sample_time)
            time.sleep(pid.sample_time)

    else:
        while (p.getJointState(bodyUniqueId=bodyA,jointIndex=4)[0] < math.pi * 2):
            t.append(t[len(t)-1] + pid.sample_time)
            velocity = pid(pos[len(pos) - 1])
            vels.append(velocity)
            pos.append(p.getJointState(bodyUniqueId=bodyA,jointIndex=4)[0])
            p.setJointMotorControl2(bodyUniqueId=bodyA, jointIndex=4, controlMode=p.VELOCITY_CONTROL, targetVelocity=velocity)
            print(p.getJointState(bodyUniqueId=bodyA,jointIndex=4))
            p.stepSimulation()

            ax[0].cla()  # Clear the subplot
            ax[0].plot(t, pos, label="Position (Z-axis)", color="blue")
            ax[0].set_title("Position over Time")
            ax[0].set_xlabel("Time (s)")
            ax[0].set_ylabel("Position (radians)")
            ax[0].grid(True)

            # Plotting Velocity
            ax[1].cla()  # Clear the subplot
            ax[1].plot(t, vels, label="Velocity (Z-axis)", color="green")
            ax[1].set_title("Velocity over Time")
            ax[1].set_xlabel("Time (s)")
            ax[1].set_ylabel("Velocity (m/s)")
            ax[1].grid(True)
            plot1 = fig.add_subplot(1,2,1)
            plot1.plot(t, vels, color='red')
            plot2 = fig.add_subplot(1,2,2)
            plot2.plot(t, pos, color='red')

            plt.pause(pid.sample_time)
            time.sleep(pid.sample_time)

    plt.ioff()
    plt.show()
    p.disconnect()
    os.remove("arm.urdf")
    return fig

def stop_simulation():
    global running_simulation
    running_simulation = False

run_simulation(0.7,0.1,0.1,1.5)