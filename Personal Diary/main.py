# Develop a personal diary application where users can write and save daily entries.


import datetime
import os
import tkinter as tk


# define a function to create a directory to store our diary entries.by using OS module 
# to create a directory with the current date as the name.

def create_directory():
    current_date = datetime.date.today()
    directory_name = current_date.strftime('%Y-%m-%d')
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)



# Define a Function save our diary entries.
def save_entry():
    current_date_time = datetime.datetime.now()
    file_name = current_date_time.strftime('%Y-%m-%d %H-%M-%S')
    entry = text_entry.get('1.0', 'end-1c')
    directory_name = current_date_time.strftime('%Y-%m-%d')
    file_path = os.path.join(directory_name, file_name + '.txt')
    with open(file_path, 'w') as file:
        file.write(entry)




root = tk.Tk()
root.title('Diary')

text_entry = tk.Text(root, height=20, width=50)
text_entry.pack()

save_button = tk.Button(root, text='Save', command=save_entry)
save_button.pack()

quit_button = tk.Button(root, text='Quit', command=root.quit)
quit_button.pack()

create_directory()

root.mainloop()