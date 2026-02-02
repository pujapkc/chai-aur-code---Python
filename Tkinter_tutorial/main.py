import tkinter


window = tkinter.Tk()

window.title("My first GUI Program")

window.minsize(height=300,width=200)

# label


my_label = tkinter.Label(text="My first label", font=("Arial", 24))

my_label.pack()


window.mainloop()
