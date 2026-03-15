from tkinter import *
import time
import tkinter.messagebox

screen = Tk()
screen.title("Time Counter")
screen.geometry("400x400")

screen.configure(bg = "lightblue")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please enter a valid number")
    
    while temp > -1:
        mins,secs = divmod(temp, 60)
        
        hours = 00
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        screen.update()
        time.sleep(1)

        if (temp == 00):
            tkinter.messagebox.showinfo("Time Countdown", "Time's up")
            exit()

        temp -= 1

hourEntry = Entry(screen, textvariable = hour, font = ("Arial", 18, ""), width = 3)
hourEntry.place(x = 80, y = 20)

minuteEntry = Entry(screen, textvariable = minute, font = ("Arial", 18, ""), width = 3)
minuteEntry.place(x = 130, y = 20)

secondEntry = Entry(screen, textvariable = second, font= ("Arial", 18, ""), width = 3)
secondEntry.place(x = 180, y = 20)

btn = Button(screen, text = "Set Time Countdown", bd = "5", command = submit)
btn.place(x = 70, y = 120)

screen.mainloop()