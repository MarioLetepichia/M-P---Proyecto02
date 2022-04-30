import tkinter
from tkinter import messagebox
from tkinter import LEFT, filedialog

#window = tkinter.Tk()

def contact():
    messagebox.showinfo("How contact me", "liahutaislinn@ciencias.unam.mx")
    print("liahutaislinn@ciencias.unam.mx");

def about():
    messagebox.showinfo("About Program", "This program is a test")
    #print("About")

def modoOcultar():
    print("Cambiar a ocultar");
    window.destroy()
    import interfaz

def hide():
    print("Hide")

def cargarImagen():
    print("Hide")
    filename = filedialog.askopenfilename(title="open")
    print(filename)

def cargarMensajeSecreto():
    text_box =tkinter.Text(window, height=10, width=30)
    text_box.insert(tkinter.END,"mensaje secreto")
    text_box.pack()



window = tkinter.Tk()
window.title('Esteganografía por el método LSB')
window.geometry("850x500")
window.resizable(width= True, height= True)
menubar = tkinter.Menu(window, background = "#000000", foreground="black" )
mode = tkinter.Menu(menubar)
mode.add_command(label= "Ocultar", command=modoOcultar)
mode.add_command(label= "Develar")
menubar.add_cascade(label="Modo", menu=mode)
help = tkinter.Menu(menubar)
help.add_command(label= "About", command=about)
help.add_command(label= "Contact", command=contact)
menubar.add_cascade(label="Help", menu=help)
window.config(menu=menubar)

modalidadOcultar = "Modalidad develar"
ocultarLabel = tkinter.Label(window,text=modalidadOcultar ,font="Arial 26").pack(side=tkinter.TOP)

btn_hide = tkinter.Button(window, text="Abrir imagen con mensaje oculto",command=cargarImagen)
btn_hide.pack(side=tkinter.TOP)
btn_hide = tkinter.Button(window, text="Develar mensaje",command=cargarMensajeSecreto)
btn_hide.pack(side=tkinter.TOP)

# modalidadOcultar = "Modalidad develar"
# ocultarLabel = tkinter.Label(window,text=modalidadOcultar ,font="Arial 26").pack(SIDE=tkinter.TOP)

window.mainloop()