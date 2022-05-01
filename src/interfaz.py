import tkinter
from PIL import ImageTk, Image
from tkinter import LEFT, filedialog
from tkinter import messagebox
from tkinter import ttk
import os
# print(os.path.abspath(os.getcwd()))
#import cv2

#window = tkinter.Tk()

def insert_img():
    global img_adress
    img_adress = filedialog.askopenfilename(title="open")
    # img_adress = Image.open(filename)
    print(img_adress)
   # img_show= img_show.resize((350,350),Image.ANTIALIAS)
    # img_show_tk = ImageTk.PhotoImage(img_adress)
    # panel = tkinter.Label(tabOcultar,image=img_show_tk)
    # panel.image = img_show_tk
    # panel.place(relx=0.1,rely=0.2 )
    #panel.pack()
   

def insert_text():
    print("Text")
    global file_adress
    file_adress = filedialog.askopenfilename(title="open")
    text_box =tkinter.Text(tabOcultar,height=30, width=30)
    text_box.place(relx=0.1,rely=0.2,relwidth=0.4,relheight=0.5)
    text = open(file_adress, "r")
    lines = text.read()
    text_box.insert(tkinter.END,lines)
    print(lines)


def ocultar_procesar():
    global dirname_adress
    name=textExample.get("1.0","end")
    name=name.rstrip()
    if(name == ""):
        messagebox.showinfo("!", "No ingresaste nombre del archivo, no se ha procesado la imagen:")
        return
    
    print(name)
    dirname_adress = filedialog.askdirectory(initialdir="/",  title='selecciona donde quieres guardar la nueva imagén')
    print(dirname_adress)
    messagebox.showinfo("", "El texto ha sido ocultado en la imagen,se encuentra en la ruta:")
   

def cargar_imagen_():
    print("Hide")
    global img_with_secret_adress 
    img_with_secret_adress = filedialog.askopenfilename(title="open")
    print(img_with_secret_adress)

def contact():
    messagebox.showinfo("How contact me", "liahutaislinn@ciencias.unam.mx")
    print("liahutaislinn@ciencias.unam.mx");

def about():
    messagebox.showinfo("About Program", "This program is a test")


# def modoDevelar():
#     print("cambiar a develar");
#     window.destroy()
#     import modo_develar
   

# def hide():
#     print("Hide")



def cargarMensajeSecreto():
    
    messagebox.showinfo("intrucciones", "A continuación eligiras la dirección del directorio que deseas generar el nuevo archivo , para ponerle nombre al nuevo archivo, despues del último / agrega el nombre")
    #new_text_adress = filedialog.askopenfilename(title="selecciona donde deseas guardar el texto con el menaje develado")
    new_text_adress  = filedialog.askdirectory(initialdir="/",  title='selecciona donde deseas guardar el texto mas el nombre del archivo')
    #mandar a llamar readMessage
    # file_Secret = llamar metodo de mario pra obtener new file texto_develado
    
    #text = open(file_adress, "r")
    #ines = text.read()
    #text_box.insert(tkinter.END,lines)
    text_box.delete("1.0", "end") 
    text_box.insert(tkinter.END,"mensaje secreto")
    text_box.pack()
    print(new_text_adress)
    

#creación de pantalla
window = tkinter.Tk()
window.title('Esteganografía por el método LSB')
window.geometry("850x500")
window.configure(background='dark turquoise')
window.resizable(width= True, height= True)
menubar = tkinter.Menu(window, background = "#000000", foreground="black" )
#tabs
tabControl= ttk.Notebook(window)
tabOcultar = ttk.Frame(tabControl)
tabControl.add(tabOcultar,text="Ocultar")
tabControl.pack(expand=.5,fill="both")
tabDevelar = ttk.Frame(tabControl)
tabControl.add(tabDevelar,text="Develar")
tabControl.pack(expand=.1, fill="both")

# btn_Ocultar = tkinter.Button(tabControl).pack()


# mode = tkinter.Menu(menubar)
# mode.add_command(label= "Ocultar", command=hide)
# mode.add_command(label= "Develar", command=modoDevelar)

help = tkinter.Menu(menubar)
help.add_command(label= "About", command=about)
help.add_command(label= "Contact", command=contact)
menubar.add_cascade(label="Help", menu=help)
window.config(menu=menubar)

modalidadOcultar = "Modalidad ocultar"

ocultarLabel = tkinter.Label(tabOcultar,text=modalidadOcultar ,font="Arial 26")
ocultarLabel.pack(side=tkinter.TOP)
file_adress=""
img_adress=""
dirname_adress=""
img_with_secret_adress=""
#ocultarLabel.pack()
btn_image = tkinter.Button(tabOcultar, text="Abrir imagen",command=insert_img)
btn_image.place(relx=0.57,rely=0.1,relwidth=0.13,relheight=0.08)
# btn_image.pack()
btn_text = tkinter.Button(tabOcultar, text="Abrir texto",command=insert_text)
btn_text.place(relx=0.22,rely=0.1,relwidth=0.13,relheight=0.08)
btn_hide = tkinter.Button(tabOcultar, text="Ocultar mensaje y generar imagén",command=ocultar_procesar)
btn_hide.pack(side=tkinter.BOTTOM)
#mini input
textExample=tkinter.Text(tabOcultar, height=1.5, width=29)
textExample.pack(side=tkinter.BOTTOM )
#textExample.pack()
indicaciones = "Ingresa el nombre del nuevo archivo de la imagen"
indicacionesLabel = tkinter.Label(tabOcultar,text=indicaciones,justify=tkinter.LEFT).pack(side=tkinter.BOTTOM)

modalidadOcultar = "Modalidad develar"

ocultarLabel = tkinter.Label(tabDevelar,text=modalidadOcultar ,font="Arial 26").pack(side=tkinter.TOP)
btn_hide = tkinter.Button(tabDevelar, text="Abrir imagen con mensaje oculto",command=cargar_imagen_)
btn_hide.pack(side=tkinter.TOP)
#btn_hide.pack()
btn_hide = tkinter.Button(tabDevelar, text="Develar mensaje",command=cargarMensajeSecreto)
btn_hide.pack(side=tkinter.TOP)
text_box =tkinter.Text(tabDevelar, height=10, width=30)

#btn_hide.pack()

window.mainloop()