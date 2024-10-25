from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import math
from simple_pid import PID

#graphing ideal PID
def plotPID(kP, kI, kD, sp):
    fig = Figure(figsize = (8,4), dpi = 100)

    fig.clear()

    pid = PID(kP, kI, kD)
    pid.setpoint = sp + (math.pi * 0.01)
    pid.sample_time = 0.01 
    t=0
    val = 0 
    values = []
    outputs = []
    time_steps = []

    while val < (sp - (math.pi * 0.01)):
        output = pid(val) 
        
        t+=pid.sample_time
        val += (output * 0.1)

        values.append(val)
        outputs.append(output)
        time_steps.append(t * 0.01)

        print(val)
        time.sleep(pid.sample_time)

    plot1 = fig.add_subplot(1,2,1)
    plot1.plot(time_steps, values, color='red')
    plot2 = fig.add_subplot(1,2,2)
    plot2.plot(time_steps, outputs, color='red')
    return fig

#graphing simulation
def plotSim():
    fig = Figure(figsize = (5,10), dpi = 100)
    plot1 = fig.add_subplot(1,2,1)
    plot1.set_title("Displacement")
    plot1.plot(time_steps, values, color='red')
    print("Plotted graph 1")
    plot2 = fig.add_subplot(1,2,2)
    plot2.set_title("PID output")
    plot2.plot(time_steps, outputs, color='red')
    print("Plotted graph 2")
    return fig

