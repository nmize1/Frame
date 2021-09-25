import tkinter as tk
import os
from tkinter import messagebox


class Configure():
    def __init__(self, d):
        self.delay = d

    def delaySet(self, d):
        if d == -1:
            d = cEnt.get()
            d.strip()
            try:
                d = int(d)
            except ValueError as e:
                err = d + " is not a number, setting delay to 1 minute.\n"
                messagebox.showerror("Error", err)
                d = 60

        self.delay = d
        print(self.delay)

    def launch(self):
        if(self.delay == -10):
            messagebox.showerror("Error", "Delay not set. Using default of 1 minute.\n")
            self.delay = 60

        fld = fldEnt.get()

        os.system("python3 Frame.py " + str(self.delay) + " " + fld)
        exit()

cf = Configure(-10)
# WINDOW #
window = tk.Tk()
wLbl = tk.Label(text = "Welcome to Frame", width = 25)

# DELAY SETTINGS #
dFrame = tk.Frame(relief = tk.GROOVE, borderwidth = 5)
dBtnFrame = tk.Frame(master = dFrame, relief = tk.GROOVE, borderwidth = 5)
dEntFrame = tk.Frame(master = dFrame, relief = tk.FLAT, borderwidth = 5)
cLbl = tk.Label(master = dEntFrame, text = "Custom (in seconds):")
cEnt = tk.Entry(master = dEntFrame)

dLbl = tk.Label(master = dFrame, text = "Choose the number of time between images:")
dBtns = [tk.Button(master = dBtnFrame, text = "5 seconds", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(5)),
         tk.Button(master = dBtnFrame, text = "30 seconds", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(30)),
         tk.Button(master = dBtnFrame, text = "1 minute", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(60)),
         tk.Button(master = dBtnFrame, text = "5 minutes", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(300)),
         tk.Button(master = dBtnFrame, text = "10 minutes", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(600)),
         tk.Button(master = dBtnFrame, text = "30 minutes", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(1800)),
         tk.Button(master = dBtnFrame, text = "1 hour", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(3600)),
         tk.Button(master = dBtnFrame, text = "Custom", width = 10, height = 1, relief = tk.RAISED, command = lambda: cf.delaySet(-1))]


# FOLDER SETTINGS #
fldLbl = tk.Label(master = dEntFrame, text = "[Optional] Path to Pictures folder:\n (Uses the current directory by default)")
fldEnt = tk.Entry(master = dEntFrame)
fldEnt.insert(0, "AWSPictures")

# LAUNCH #
LaunchBtn = tk.Button(master = dFrame, text = "Launch Slideshow", width = 20, height = 2, relief = tk.RAISED, command = lambda: cf.launch())

dLbl.pack()
j = 0

for btn in dBtns:
     btn.grid(row = 0, column = j)
     j = j + 1
dBtnFrame.pack()

cLbl.grid(row = 1, column = 0)
cEnt.grid(row = 1, column = 1)
fldLbl.grid(row = 2, column = 0)
fldEnt.grid(row = 2, column = 1)
dEntFrame.pack()

wLbl.pack()
LaunchBtn.pack()
dFrame.pack()

window.mainloop()
