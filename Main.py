import tkinter as tk
import json
import threading

from simple_pid import PID
from write_to_urdf import write

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

def save_to_json():
    width = entry_width.get()
    length = entry_length.get()
    weight = entry_weight.get()

    data = {
        "width": width,
        "length": length,
        "weight": weight
    }

    with open('dimensions.json', 'w') as file:
        json.dump(data, file, indent=4)
    write(entry_length.get(), entry_width.get(), entry_weight.get())

def startPIDsim(kP, kI, kD):
    import sim
    sim_thread = threading.Thread(target=sim.run_simulation)
    sim_thread.start()
    print("thread started - code")
    entry_width.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

root = tk.Tk()
root.title("Dimension Input")
root.geometry("1300x700")
root.configure(bg="black")

label_width = tk.Label(root, text="Width:")
label_width.grid(row=0, column=0)
entry_width = tk.Entry(root)
entry_width.grid(row=0, column=1)

label_length = tk.Label(root, text="Length:")
label_length.grid(row=1, column=0)
entry_length = tk.Entry(root)
entry_length.grid(row=1, column=1)

label_weight = tk.Label(root, text="Weight:")
label_weight.grid(row=2, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=2, column=1)

save_button = tk.Button(root, text="Save Arm measurements", command=save_to_json)
save_button.grid(row=3, column=0, columnspan=2)

label_p = tk.Label(root, text="kP:")
label_p.grid(row=4, column=0)
entry_p = tk.Entry(root)
entry_p.grid(row=4, column=1)

label_I = tk.Label(root, text="kI:")
label_I.grid(row=5, column=0)
entry_I = tk.Entry(root)
entry_I.grid(row=5, column=1)

label_D = tk.Label(root, text="kD:")
label_D.grid(row=6, column=0)
entry_D = tk.Entry(root)
entry_D.grid(row=6, column=1)



def display_plot():
    #kP = float(entry_p.get())
    #kI = float(entry_I.get())
    #kD = float(entry_D.get())

    #pid = PID(kP, kI, kD)
    pid = PID(0.7, 0, 0)
    
    pid.setpoint = 10
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

    fig, ax = plt.subplots()
    ax.plot(time_steps, values, label='System Value')
    ax.axhline(y=pid.setpoint, color='r', linestyle='--', label='Setpoint')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Value')
    ax.set_title('PID Control System Response')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

plot_button = tk.Button(root, text="Display PID Plot", command=display_plot)
plot_button.grid(row=7, column=0, columnspan=2)

#sim_button = tk.Button(root, text="Start Simulation", command=startPIDsim(kP,kI,kD))
#sim_button.grid(row=8, column=0, columnspan=2)

root.mainloop()
