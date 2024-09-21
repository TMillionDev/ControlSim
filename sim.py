import pybullet as p
import time
import pybullet_data

def setup_simulation():
    physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)
    
    planeId = p.loadURDF("plane.urdf")
    bodyApos = [0, 0, 5]
    startOrientation = p.getQuaternionFromEuler([0, 0, 0])
    bodyA = p.loadURDF("Models/Arm.urdf", bodyApos, startOrientation)
    joint_index = p.getJointInfo(bodyA, 0)[0]
    # p.resetBasePositionAndOrientation(bodyA, [0, 0, 0], [0, 0, 0, 1])
    p.changeDynamics(bodyA, -1, lateralFriction=1, spinningFriction=0.1, rollingFriction=0.01)
    return bodyA

def run_simulation(bodyA):
    try:
        while True:
            p.applyExternalForce(bodyA, linkIndex=-1, forceObj=[0, 0, (4*9.81)], posObj=[0, 0, 0], flags=p.WORLD_FRAME)
            p.stepSimulation()
            time.sleep(1./240.)
    except KeyboardInterrupt:
        p.disconnect()

if __name__ == "__main__":
    bodyA = setup_simulation()
    run_simulation(bodyA)
