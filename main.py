from tkinter import *
import datetime


root = Tk()

class Application:
    def __init__(self, master=None):
        self.root = root
        self.window()
        self.labels()
        self.clock()
        root.mainloop()

    def window(self):
        self.root.title("Clock")
        self.root.geometry("500x250")

    def labels(self):
        self.clock_label = Label(self.root, font='arial 40', foreground='black')
        self.clock_label.pack(anchor='center')

        self.date_label = Label(self.root, font='arial 30', foreground='black')
        self.date_label.pack(anchor='s')

    def clock(self):
        self.date_time = datetime.datetime.now().strftime("%A %d-%m-%Y %H:%M:%S/%p")
        self.today, self.date, self.time1 = self.date_time.split()
        self.time2, self.time3 = self.time1.split('/')
        self.time = self.time2 + ' ' + self.time3

        self.clock_label.config(text = self.time)
        self.clock_label.after(1000, self.clock)

        self.date_label.config(text = self.date + '\n' + self.today)
        
Application(root)
