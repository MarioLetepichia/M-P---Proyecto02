"""
Modulo principal que corre el programa
@author MarioLetepichia
"""
import sys
import imageProcessor as png

'''Funcion principal ejecutada al correr el programa; necesita acompanarse de parametros en la linea de 
comando para funcionar correctamente
'''
def main():
    try:
        option = sys.argv[1]
        if(option == 'h'):
            hide(sys.argv[2], sys.argv[3], sys.argv[4])
        elif(option == 'u'):
            read(sys.argv[2], sys. argv[3])
        else:
            raise IndexError
    except IndexError:
        print("La opcion recibida ha sido invalida, intenta utiliza uno de los siguientes formatos:")
        print("    h <../Texto> <../Imagen> <../ImagenResultante>")
        print("    u <../Imagen> <../TextoResultante>")

'''Funcion encargada de llamar a 'imageProcessor' para ocultar texto

    Parameters
    ----------
    text: Direccion del texto a ocultar
    img: Direccion de la imagen en la que se ocultara la informacion
    finalImg: Direccion de la imagen resultante
'''
def hide(text, img, finalImg):
    with open(text) as f:
        contents = f.readlines()
    png.hideMessage(img, contents, finalImg)

'''Funcion encargada de decodificar una imagen para poder leer el texto oculto

    Parameters
    ----------
    img: Direccion de la imagen a procesar
    finalText: Texto resultante de procesar la imagen
'''
def read(img, finalText):
    png.readMessage(img, finalText)


if __name__ == "__main__":
    main()