import tkinter as tk
from tkinter import ttk
import datetime 


root = tk.Tk()

class Application:
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.tabs()
        self.labels()
        self.clock()
        root.mainloop()
    def window(self):
        self.root.title("Clock")
        self.root.geometry("500x250")
        
    def tabs(self):
        self.tab_parent = ttk.Notebook(self.root)
        self.clock_tab = ttk.Frame(self.tab_parent)
        self.alarm_tab = ttk.Frame(self.tab_parent)
        self.stopwatch_tab = ttk.Frame(self.tab_parent)
        self.timer_tab = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.clock_tab, text="Clock")
        self.tab_parent.add(self.alarm_tab, text="Alarm")
        self.tab_parent.add(self.stopwatch_tab, text="Stopwatch")
        self.tab_parent.add(self.timer_tab, text="Timer")
        self.tab_parent.pack(expand=1, fill="both")

    def labels(self):
        self.clock_label = tk.Label(self.clock_tab, font='calibri 40 bold', foreground='black')
        self.clock_label.pack(anchor='center')

        self.date_label = tk.Label(self.clock_tab, font='calibri 40 bold', foreground='black')
        self.date_label.pack(anchor='s')

    def clock(self):
        self.date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        self.date, self.time1 = self.date_time.split()
        self.time2, self.time3 = self.time1.split('/')
        self.hour, self.minute, self.second = self.time2.split(":")
        if int(self.hour) > 12 and int(self.hour) < 24:
            self.time = str(int(self.hour) - 12) + ':' + self.minute + ':' + self.second + ' ' + self.time3
        else:
            self.time = self.time2 + ' ' + self.time3

        self.clock_label.config(text = self.time)
        self.date_label.config(text = self.date)
        self.clock_label.after(1000, self.clock)





Application(root)
