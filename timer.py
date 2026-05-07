import tkinter as tk
from tkinter import ttk, messagebox

class UrchTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Urch Pro Timer")
        self.root.geometry("300x250")
        
        self.seconds_left = 0
        self.running = False
        self._setup_ui()

    def _setup_ui(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True)

        ttk.Label(self.main_frame, text="Minutes:", font=("Arial", 10)).pack()
        
        self.entry = ttk.Entry(self.main_frame, justify="center")
        self.entry.pack(pady=5)
        self.entry.insert(0, "25")

        self.timer_label = ttk.Label(self.main_frame, text="00:00", font=("Arial", 30, "bold"))
        self.timer_label.pack(pady=15)

        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.pack(pady=5)

        self.start_btn = ttk.Button(btn_frame, text="Start", command=self.start_timer)
        self.start_btn.pack(side="left", padx=2)

        self.reset_btn = ttk.Button(btn_frame, text="Reset", command=self.reset_timer)
        self.reset_btn.pack(side="left", padx=2)

    def start_timer(self):
        if not self.running:
            try:
                if self.seconds_left <= 0:
                    self.seconds_left = int(self.entry.get()) * 60
                
                self.running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

    def reset_timer(self):
        self.running = False
        self.seconds_left = 0
        self.timer_label.config(text="00:00")

    def update_timer(self):
        if self.running and self.seconds_left > 0:
            mins, secs = divmod(self.seconds_left, 60)
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}")
            self.seconds_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.seconds_left == 0:
            self.running = False
            self.timer_label.config(text="Time's up!")
            messagebox.showinfo("Urch Timer", "Session Complete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = UrchTimer(root)
    root.mainloop()
