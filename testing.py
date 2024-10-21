from simple_pid import PID
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Global variables to store PID simulation data
t = 0
val = 0
values = []
time_steps = []
canvas = None  # Variable to hold the canvas

# Function to run the PID simulation in non-blocking intervals
def run_pid_simulation(pid):
    global t, val, values, time_steps, canvas

    if val < 24.9:
        output = pid(val)
        t += 0.01
        val += output * 0.1

        values.append(val)
        time_steps.append(t * pid.sample_time)

        # Update the plot dynamically
        update_plot()

        # Continue PID simulation after 10 ms
        root.after(int(pid.sample_time * 1000), lambda: run_pid_simulation(pid))

# Function to display the plot
def display_plot():
    global t, val, values, time_steps, canvas

    # Reset simulation variables
    t = 0
    val = 0
    values.clear()
    time_steps.clear()

    # Initialize PID controller with fixed parameters
    pid = PID(0.7, 0, 0)
    pid.setpoint = 10
    pid.sample_time = 0.01

    # Start the PID simulation
    run_pid_simulation(pid)

# Function to create or update the plot on the Tkinter canvas
def update_plot():
    global canvas

    # Create a new figure for plotting
    fig, ax = plt.subplots()
    ax.plot(time_steps, values, label='System Value')
    ax.axhline(y=10, color='r', linestyle='--', label='Setpoint')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Value')
    ax.set_title('PID Control System Response')
    ax.legend()

    # Clear the previous canvas if it exists
    if canvas is not None:
        canvas.get_tk_widget().pack_forget()

    # Create and display the canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Main Tkinter window setup
root = tk.Tk()
root.title("PID Control Plot in Tkinter")
root.geometry("1300x700")
root.configure(bg="black")

# Button to trigger the plot
plot_button = tk.Button(root, text="Display PID Plot", command=display_plot)
plot_button.grid(row=1, column=0, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
