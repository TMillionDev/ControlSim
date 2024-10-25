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

root = tk.Tk()
root.title("Dimension Input")
root.geometry("1300x700")
root.configure(bg="black")

kP = 0
kI = 0
kD = 0
setpoint = 0

image = Image.open("Icon.png")
img = image.resize((150, 40))
photo = ImageTk.PhotoImage(img)
icon = tk.Label(root, image=photo)
icon.pack(side="top",anchor="nw",pady=5)

measurementFrame = tk.Frame(root)
measurementFrame.config(bg="black")
widthFrame = tk.Frame(measurementFrame)
lengthFrame = tk.Frame(measurementFrame)
weightFrame = tk.Frame(measurementFrame)

pFrame = tk.Frame(root)
iFrame = tk.Frame(root)
dFrame = tk.Frame(root)
spFrame = tk.Frame(root)
graphFrame = tk.Frame(root)

#robot arm measurements
label_width = tk.Label(root, text="Width:")
label_width.grid(in_=widthFrame, row=1, column=0, columnspan=2)
label_width.config(font=('Arial',14,'bold'))
label_width.config(bg='black')
label_width.config(fg='white')
entry_width = tk.Entry(root)
entry_width.grid(in_=widthFrame, row=1, column=3, columnspan=2)
widthFrame.pack(side="top",pady=5)

label_length = tk.Label(root, text="Length:")
label_length.grid(in_=lengthFrame, row=1, column=0, columnspan=2)
label_length.config(font=('Arial',14,'bold'))
label_length.config(bg='black')
label_length.config(fg='white')
entry_length = tk.Entry(root)
entry_length.grid(in_=lengthFrame, row=1, column=3, columnspan=2)
lengthFrame.pack(side="top",pady=5)

label_weight = tk.Label(root, text="Weight:")
label_weight.grid(in_=weightFrame, row=1, column=0, columnspan=2)
label_weight.config(font=('Arial',14,'bold'))
label_weight.config(bg='black')
label_weight.config(fg='white')
entry_weight = tk.Entry(root)
entry_weight.grid(in_=weightFrame, row=1, column=3, columnspan=2)
weightFrame.pack(side="top",pady=5)

save_button = tk.Button(root, text="Save Arm measurements", command=save_to_json)
save_button.pack(in_=measurementFrame,pady=5)
measurementFrame.pack(side="top",anchor="nw",pady=5)

imageEQ = Image.open("PIDequation.png")
imgEQ = imageEQ.resize((300, 50))
EQphoto = ImageTk.PhotoImage(imgEQ)
eq = tk.Label(root, image=EQphoto)
eq.pack(side="top",anchor="nw",pady=5)

#PID measurements
label_p = tk.Label(root, text="kP:")
label_p.grid(in_=pFrame, row=1, column=0, columnspan=2)
label_p.config(font=('Arial',14,'bold'))
label_p.config(bg='black')
label_p.config(fg='white')
entry_p = tk.Entry(root)
entry_p.grid(in_=pFrame, row=1, column=3, columnspan=2)
pFrame.pack(side="top",anchor="nw",pady=5)

label_I = tk.Label(root, text="kI:")
label_I.grid(in_=iFrame, row=1, column=0, columnspan=2)
label_I.config(font=('Arial',14,'bold'))
label_I.config(bg='black')
label_I.config(fg='white')
entry_I = tk.Entry(root)
entry_I.grid(in_=iFrame, row=1, column=3, columnspan=2)
iFrame.pack(side="top",anchor="nw",pady=5)

label_D = tk.Label(root, text="kD:")
label_D.grid(in_=dFrame, row=1, column=0, columnspan=2)
label_D.config(font=('Arial',14,'bold'))
label_D.config(bg='black')
label_D.config(fg='white')
entry_D = tk.Entry(root)
entry_D.grid(in_=dFrame, row=1, column=3, columnspan=2)
dFrame.pack(side="top",anchor="nw",pady=5)

label_sp = tk.Label(root, text="setpoint (radians):")
label_sp.grid(in_=spFrame, row=1, column=0, columnspan=2)
entry_sp = tk.Entry(root)
entry_sp.grid(in_=spFrame, row=1, column=3, columnspan=2)
spFrame.pack(side="top",anchor="nw",pady=5)

def display_idealplot():
    kP = float(str(entry_p.get()))
    kI = float(str(entry_I.get()))
    kD = float(str(entry_D.get()))
    sp = float(str(entry_sp.get()))
    canvas = FigureCanvasTkAgg(graphing.plotPID(kP, kI, kD, sp), master = root)
    canvas.draw()
    canvas.get_tk_widget().pack(in_=graphFrame,anchor="nw")
    print("graphed ideal graph")

def startPIDsim():
    kP = float(str(entry_p.get()))
    kI = float(str(entry_I.get()))
    kD = float(str(entry_D.get()))
    sp = float(str(entry_sp.get()))
    import sim
    sim_thread = threading.Thread(target=sim.run_simulation(kP, kI, kD, setpoint))
    sim_thread.start()
    print("thread started - code")
    entry_width.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    entry_weight.delete(0, tk.END)

plot_button = tk.Button(root, text="Display PID Plot", command=display_idealplot)
plot_button.pack(side="top",anchor="nw",pady=5)

labelFrame = tk.Frame(root)
sim_button = tk.Button(root, text="Start Simulation", command=startPIDsim)
sim_button.pack(in_=labelFrame,anchor="nw",pady=5)
simGraph_label = tk.Label(root, text="Simulation Graphs")
labelFrame.pack(side="top",anchor="nw",pady=5)
graphFrame.pack(side="top",anchor="nw")

root.mainloop()
