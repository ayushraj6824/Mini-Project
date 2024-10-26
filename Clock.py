import tkinter as tk
from datetime import datetime
import time

# Main window
root = tk.Tk()
root.title("Digital Clock and Stopwatch")
root.geometry("300x200")

# Global variable to control stopwatch state
stopwatch_running = False
stopwatch_time = 0

### Digital Clock ###
def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)  

clock_label = tk.Label(root, font=("Arial", 18), fg="blue")
clock_label.pack(pady=10)
update_clock()  

### Stopwatch ###
def update_stopwatch():
    global stopwatch_time
    if stopwatch_running:
        minutes, seconds = divmod(stopwatch_time, 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        stopwatch_time += 1
        root.after(1000, update_stopwatch)  

def start_stopwatch():
    global stopwatch_running
    if not stopwatch_running:
        stopwatch_running = True
        update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_time
    stopwatch_time = 0
    stopwatch_label.config(text="00:00:00")

# Stopwatch display and controls
stopwatch_label = tk.Label(root, font=("Arial", 18), fg="green", text="00:00:00")
stopwatch_label.pack(pady=10)

start_button = tk.Button(root, text="Start", command=start_stopwatch)
start_button.pack(side="left", padx=10)

stop_button = tk.Button(root, text="Stop", command=stop_stopwatch)
stop_button.pack(side="left", padx=10)

reset_button = tk.Button(root, text="Reset", command=reset_stopwatch)
reset_button.pack(side="left", padx=10)

# Start the main loop
root.mainloop()
