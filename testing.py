from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
from simple_pid import PID

def plotPID(kP, kI, kD, sp, tol):
    fig = Figure(figsize = (10,5), dpi = 100)

    pid = PID(kP, kI, kD)
    print("pid init")
    pid.setpoint = sp
    pid.sample_time = 0.01 
    t=0
    val = 0 
    values = []
    outputs = []
    time_steps = []
    print("pid setup")

    while val < (sp - tol):
        output = pid(val) 
        
        t+=0.01
        val += output * 0.1 

        values.append(val)
        outputs.append(output)
        time_steps.append(t * 0.01)

        print(val)
        time.sleep(pid.sample_time)

    plot1 = fig.add_subplot(1,2,1)
    plot2 = fig.add_subplot(1,2,2)

    print(time_steps)
    print("\b")
    print(outputs)
    print(len(time_steps))
    print(len(values))
    print(len(outputs))

    plot1 = fig.add_subplot(1,2,1)
    plot1.plot(time_steps, values, color='red')
    print("Plotted graph 1")
    plot2 = fig.add_subplot(1,2,2)
    plot2.plot(time_steps, outputs, color='red')
    print("Plotted graph 2")
    return fig

root = Tk()
canvas = FigureCanvasTkAgg(plotPID(0.7,0,0,10,0.5), master = root)
canvas.draw()
canvas.get_tk_widget().pack()

canvas.title("plotting")
canvas.geometry("1000x600")

plot_button = Button(master = root,  
                    command = plotPID(0.7,0,0,10,0.5), 
                    height = 2,  
                    width = 10, 
                    text = "Plot") 

plot_button.pack()

root.mainloop()
