import tkinter as tk

def start_timer():
    global seconds_left
    minutes = int(entry.get())
    seconds_left = minutes * 60
    update_timer()

def update_timer():
    global seconds_left
    if seconds_left > 0:
        mins, secs = divmod(seconds_left, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timeformat)
        seconds_left -= 1
        root.after(1000, update_timer)  # Update every 1000 ms (1 second)
    else:
        timer_label.config(text="Timer is up!")

root = tk.Tk()
root.title("Simple Timer")

label = tk.Label(root, text="Enter minutes:")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

timer_label = tk.Label(root, text="00:00")
timer_label.pack()

root.mainloop()
