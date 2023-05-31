import tkinter as tk

class Timer:
    def __init__(self, master):
        self.master = master
        self.seconds = 0
        self.timer_running = False
        self.timer_label = tk.Label(master, text='00:00', font=('Arial', 24), width=10)
        self.start_button = tk.Button(master, text='Start', command=self.start_timer)
        self.stop_button = tk.Button(master, text='Stop', command=self.stop_timer, state=tk.DISABLED)
        self.reset_button = tk.Button(master, text='Reset', command=self.reset_timer, state=tk.DISABLED)

        self.timer_label.pack(pady=10)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.timer_running = False
        self.seconds = 0
        self.timer_label.config(text='00:00')
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            time_string = '{:02d}:{:02d}'.format(minutes, seconds)
            self.timer_label.config(text=time_string)
            self.master.after(1000, self.update_timer)

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.seconds = 0
        self.stopwatch_running = False
        self.stopwatch_label = tk.Label(master, text='00:00', font=('Arial', 24), width=10)
        self.start_button = tk.Button(master, text='Start', command=self.start_stopwatch)
        self.stop_button = tk.Button(master, text='Stop', command=self.stop_stopwatch, state=tk.DISABLED)
        self.reset_button = tk.Button(master, text='Reset', command=self.reset_stopwatch, state=tk.DISABLED)

        self.stopwatch_label.pack(pady=10)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def start_stopwatch(self):
        self.stopwatch_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.update_stopwatch()

    def stop_stopwatch(self):
        self.stopwatch_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.seconds = 0
        self.stopwatch_label.config(text='00:00')
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def update_stopwatch(self):
        if self.stopwatch_running:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            time_string = '{:02d}:{:02d}'.format(minutes, seconds)
            self.stopwatch_label.config(text=time_string)
            self.master.after(1000, self.update_stopwatch)

root = tk.Tk()
root.title('Timer and Stopwatch')

timer_frame = tk.Frame(root)
timer_frame.pack(pady=20)
timer = Timer(timer_frame)

stopwatch_frame = tk.Frame(root)
stopwatch_frame.pack(pady=20)
stopwatch = Stopwatch(stopwatch_frame)

root.mainloop()
