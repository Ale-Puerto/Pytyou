from tkinter import *
from interfaces import Window



if __name__ == "__main__":
    root = Tk()
    root.title('pyotu')
    root.geometry('650x400')
    root.configure(bg='white')
    app = Window(root)
    root.mainloop()