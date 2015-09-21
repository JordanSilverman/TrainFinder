from Tkinter import *
from Departure_Board_HGY import *


root = Tk()

my_label = Label(root, text = HGY_dep_board())
root.title("Departure Board")

root.mainloop()
