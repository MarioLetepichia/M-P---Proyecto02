"""
Modulo principal que corre el programa
@author MarioLetepichia
"""
import sys
import imageProcessor as png

def main():
    '''Funcion principal ejecutada al correr el programa; necesita acompanarse de parametros en la linea de 
    comando para funcionar correctamente
    '''
    try:
        option = sys.argv[1]
        if(option == 'h'):
            png.hideMessage(sys.argv[2], sys.argv[3], sys.argv[4])
        elif(option == 'u'):
            png.readMessage(sys.argv[2], sys. argv[3])
        else:
            raise IndexError
    except IndexError:
        print("La opcion recibida ha sido invalida, intenta utiliza uno de los siguientes formatos:")
        print("    h <../Texto> <../Imagen> <../ImagenResultante>")
        print("    u <../Imagen> <../TextoResultante>")

if __name__ == "__main__":
    main()