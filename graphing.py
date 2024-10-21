import time
import matplotlib.pyplot as plt
from simple_pid import PID

kP = 0.9
kI = 0
kD = 0

pid = PID(kP, kI, kD)
pid.setpoint = 25
pid.sample_time = 0.01 

t=0
val = 0 
values = []
time_steps = []

while val < 24.9:
    output = pid(val) 
    
    t+=0.01
    val += output * 0.1 

    values.append(val)
    time_steps.append(t * pid.sample_time)

    time.sleep(pid.sample_time)

plt.plot(time_steps, values, label='System Value')
plt.axhline(y=pid.setpoint, color='r', linestyle='--', label='Setpoint')
plt.xlabel('Time (seconds)')
plt.ylabel('Value')
plt.title('PID Control System Response')
plt.legend()
plt.show()
