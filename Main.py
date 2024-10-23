import tkinter as tk
import json
import threading
from PIL import ImageTk, Image

from simple_pid import PID
from write_to_urdf import write
import graphing

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

def startPIDsim():
    import sim
    sim_thread = threading.Thread(target=sim.run_simulation())
    sim_thread.start()
    print("thread started - code")
    entry_width.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

root = tk.Tk()
root.title("Dimension Input")
root.geometry("1300x700")
root.configure(bg="black")

#robot arm measurements
label_width = tk.Label(root, text="Width:")
label_width.pack(side="top", anchor="nw")
entry_width = tk.Entry(root)
entry_width.pack(side="top", anchor="nw")

label_length = tk.Label(root, text="Length:")
label_length.pack(side="top", anchor="nw")
entry_length = tk.Entry(root)
entry_length.pack(side="top", anchor="nw")

label_weight = tk.Label(root, text="Weight:")
label_weight.pack(side="top", anchor="nw")
entry_weight = tk.Entry(root)
entry_weight.pack(side="top", anchor="nw")

save_button = tk.Button(root, text="Save Arm measurements", command=save_to_json)
save_button.pack(side="top", anchor="nw")

#PID measurements
label_p = tk.Label(root, text="kP:")
label_p.pack(side="top", anchor="nw")
entry_p = tk.Entry(root)
entry_p.pack(side="top", anchor="nw")

label_I = tk.Label(root, text="kI:")
label_I.pack(side="top", anchor="nw")
entry_I = tk.Entry(root)
entry_I.pack(side="top", anchor="nw")

label_D = tk.Label(root, text="kD:")
label_D.pack(side="top", anchor="nw")
entry_D = tk.Entry(root)
entry_D.pack(side="top", anchor="nw")

label_sp = tk.Label(root, text="setpoint:")
label_sp.pack(side="top", anchor="nw")
entry_sp = tk.Entry(root)
entry_sp.pack(side="top", anchor="nw")

kP = 0
kI = 0
kD = 0
setpoint = 0

x = False

def display_plot():
    
    canvas = FigureCanvasTkAgg(graphing.plotPID(0.7,0,0,10,0.5), master = root)
    canvas.draw()
    canvas.get_tk_widget().pack()

plot_button = tk.Button(root, text="Display PID Plot", command=display_plot)
plot_button.pack(side="top", anchor="nw")

sim_button = tk.Button(root, text="Start Simulation", command=startPIDsim)
sim_button.pack(side="top", anchor="nw")

root.mainloop()
