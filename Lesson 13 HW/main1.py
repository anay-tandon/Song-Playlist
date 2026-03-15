from tkinter import *

screen = Tk()
screen.title("Music Player")

screen.geometry("800x500")

def play():
    label.config(text = "Now Playing: " + box.get(ANCHOR))

Play = Button(screen, text = "Play" , width = 15, command = play)
Play.pack(padx = 5, pady = 5)

frame = Frame(screen)
frame.pack(pady = 5, padx = 5)
ScrollBar = Scrollbar(frame, orient = VERTICAL)
ScrollBar.pack(side = RIGHT, fill = Y)

box = Listbox(frame, width = 70, bg = "yellow", yscrollcommand = ScrollBar.set)

box.insert(END, "Song 1")
box.insert(END, "Song 2")
box.insert(END, "Song 3")
box.insert(END, "Song 4")
box.insert(END, "Song 5")

label = Label(frame, font = ("Arial", 15, "bold"))
label.pack(padx = 5, pady = 5)

box.pack(pady = 25)

ScrollBar.config(command = box.yview)

screen.mainloop()