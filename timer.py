import tkinter as tk
import winsound

class Timer:
    def __init__(self, master):
        self.master = master
        self.seconds = 0
        self.timer_running = False
        self.timer_label = tk.Label(master, text='00:00', font=('Arial', 24), width=10)
        self.start_button = tk.Button(master, text='Start', command=self.start_timer)
        self.stop_button = tk.Button(master, text='Stop', command=self.stop_timer, state=tk.DISABLED)
        self.reset_button = tk.Button(master, text='Reset', command=self.reset_timer, state=tk.DISABLED)

        self.timer_entry_label = tk.Label(master, text='Set Timer (secs):')
        self.timer_entry = tk.Entry(master, width=10)
        self.set_timer_button = tk.Button(master, text='Set', command=self.set_timer)

        self.timer_label.pack(pady=10)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        self.reset_button.pack(side=tk.LEFT, padx=5)
        self.timer_entry_label.pack(side=tk.LEFT, padx=5)
        self.timer_entry.pack(side=tk.LEFT, padx=5)
        self.set_timer_button.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        if self.seconds > 0:
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

    def set_timer(self):
        self.seconds = int(self.timer_entry.get())
        self.timer_label.config(text='{0:02d}:{1:02d}'.format(self.seconds//60, self.seconds%60))

    def play_sound(self):
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        #winsound.Beep(frequency, duration)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

    def update_timer(self):
        if self.timer_running:
            self.seconds -= 1
            if self.seconds == 0:
                self.play_sound()
                self.timer_running = False
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                self.reset_button.config(state=tk.DISABLED)
            else:
                minutes = self.seconds // 60
                seconds = self.seconds % 60
                time_string = '{:02d}:{:02d}'.format(minutes, seconds)
                self.timer_label.config(text=time_string)
                self.master.after(1000, self.update_timer)

root = tk.Tk()
root.title('Timer')

timer_frame = tk.Frame(root)
timer_frame.pack(pady=20)
timer = Timer(timer_frame)

root.mainloop()
