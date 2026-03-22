from tkinter import *

screen = Tk()
screen.title("Line Editor")

screen.geometry("800x500")

label1 = Label(screen, text = "Line Editor", font = ("Arial", 20, "bold"))
label1.pack(pady = 5)

def update1():
    box.delete(ANCHOR)
    box.insert(ANCHOR, Entry1.get())
    Entry1.delete(0, END)


update = Button(screen, text = "Update" , width = 15, command = update1)
update.pack(padx = 5, pady = 5)

x = StringVar()

Entry1 = Entry(screen, width = 35 , textvariable = x)
Entry1.pack(pady = 5, padx = 5)

frame = Frame(screen)
frame.pack(pady = 5, padx = 5)

ScrollBar = Scrollbar(frame, orient = VERTICAL)
ScrollBar.pack(side = RIGHT, fill = Y)

box = Listbox(frame, width = 70, bg = "yellow", yscrollcommand = ScrollBar.set)

x = box.get(ANCHOR)

box.insert(END, "Item 1")
box.insert(END, "Item 2")
box.insert(END, "Item 3")

box.pack(pady = 25)

ScrollBar.config(command = box.yview)

screen.mainloop()
