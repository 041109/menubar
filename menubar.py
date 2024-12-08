from tkinter import*
window = Tk()
window.geometry("200x200")
window.title("Menubar")

# creating Menubar
menubar = Menu(window)

# Adding File menu
file = Menu(menubar)
menubar.add_cascade(label = 'File' , menu = file)
file.add_cascade(label = "New File" , command=None)
file.add_cascade(label = "Open" , command=None)
file.add_cascade(label = "Save" , command=None)
file.add_separator()
file.add_cascade(label = "Exit" , command=window.destroy)

# Adding Edit bar
edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label = "Edit" , menu=edit)
edit.add_cascade(label = "Cut" , command=None)
edit.add_cascade(label = "Copy" , command=None)
edit.add_cascade(label = "Paste" , command=None)
edit.add_cascade(label = "Select All" , command=None)
edit.add_cascade(label = "Find" , command=None)
edit.add_cascade(label = "Replace" , command=None)

# Adding Help bar
help = Menu(menubar,tearoff=1)
menubar.add_cascade(label = "Help" , menu=help)
help.add_cascade(label = "Take Help",command=None)
help.add_cascade(label = "Exit" , command=window.destroy)




window.config(menu=menubar)

window.mainloop()