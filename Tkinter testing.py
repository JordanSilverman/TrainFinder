import Tkinter
import tkFont
top = Tkinter.Tk()


w = Text(master, "#000000", font, "#fff")
#master, background color, font, font color
w.insert(INSERT, "This is the departure board")
font = tkFont.Font(family = "Helvetica", size = 36, weight = "bold")


top.mainloop(w)
