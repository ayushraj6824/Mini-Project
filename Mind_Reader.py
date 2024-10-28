import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time

def read_mind():
    # Get the user's input number
    number = entry.get()
    
    # Check if the input is a number between 1 and 10
    if not number.isdigit() or not (1 <= int(number) <= 100):
        messagebox.showwarning("Warning", "Please enter a number between 1 and 100.")
        return

    # Simulate "decoding thoughts" with a progress bar
    progress_label.config(text="Decoding thoughts...")
    progress_bar['value'] = 0
    root.update_idletasks()
    
    for i in range(100):
        time.sleep(0.02)  # Adjust speed of progress bar filling
        progress_bar['value'] += 1
        root.update_idletasks()
    
    progress_label.config(text="")  # Clear progress label
    
    # Show the "predicted" number (the user's input)
    messagebox.showinfo("Mind Reader", f"You're thinking of the number {number}.")

# Set up the main window
root = tk.Tk()
root.title("Mind Reader")
root.geometry("300x150")

# Instruction label
instruction_label = tk.Label(root, text="Think of a number between 1 and 100:", font=("Arial", 12))
instruction_label.pack(pady=5)

# Entry box for user to input their number
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

# Progress label and bar
progress_label = tk.Label(root, text="", font=("Arial", 10))
progress_label.pack()

progress_bar = Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=5)

# Button to "read" the user's mind
button = tk.Button(root, text="Read my mind", command=read_mind, font=("Arial", 12))
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

