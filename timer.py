import tkinter as tk

def start_timer():

    minutes = int(entry.get())
    seconds = minutes * 60
    

root = tk.Tk()
root.title("Simple Timer")


label = tk.Label(root, text="Enter minutes:")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()


root.mainloop()
