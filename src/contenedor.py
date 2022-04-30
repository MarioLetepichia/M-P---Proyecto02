import tkinter
from tkinter import messagebox

def contact():
    messagebox.showinfo("How contact me", "liahutaislinn@ciencias.unam.mx")
    print("liahutaislinn@ciencias.unam.mx");

def about():
    messagebox.showinfo("About Program", "This program is a test")
    print("About")

def modoDevelar():
    print("");
    window.destroy()
    import modo_develar

def hide():
    print("Hide")

window = tkinter.Tk()
window.title('Esteganografía por el método LSB')
window.geometry("850x500")
window.resizable(width= True, height= True)
menubar = tkinter.Menu(window, background = "#000000", foreground="black" )
mode = tkinter.Menu(menubar)
mode.add_command(label= "Ocultar", command=hide)
mode.add_command(label= "Develar", command=modoDevelar)
menubar.add_cascade(label="Modo", menu=mode)
help = tkinter.Menu(menubar)
help.add_command(label= "About", command=about)
help.add_command(label= "Contact", command=contact)
menubar.add_cascade(label="Help", menu=help)
window.config(menu=menubar)

