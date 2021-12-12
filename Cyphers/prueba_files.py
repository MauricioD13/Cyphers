import tkinter
from  tkinter import *
import tkinter.filedialog
root = Tk()
root.directory = tkinter.filedialog.askopenfilename()
print (root.directory)