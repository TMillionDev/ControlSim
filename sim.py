import pybullet as p
import time
import pybullet_data
import time
import os

running_simulation = True
def run_simulation():
    global running_simulation
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)
        
    planeId = p.loadURDF("plane.urdf")
    bodyApos = [0, 0, 5]
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])
    
    bodyA = p.loadURDF("Arm.urdf", bodyApos, startOrientation)
    
    joint_index = p.getJointInfo(bodyA, 0)[0]
    p.changeDynamics(bodyA, -1, lateralFriction=1, spinningFriction=0.1, rollingFriction=0.01)
    
    try:
        while running_simulation:
            #p.applyExternalForce(bodyA, linkIndex=-1, forceObj=[0, 0, (4 * 9.81)], posObj=[0, 0, 0], flags=p.WORLD_FRAME)
            p.stepSimulation()
            time.sleep(1. / 240.)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        p.disconnect()
        os.remove("arm.urdf")

def stop_simulation():
    global running_simulation
    running_simulation = False

run_simulation()
