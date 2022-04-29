import sys
import imageProcessor as png
import bitProcessor as bit

"""
***Proceso para ocultar texto en pixeles
Desde esta clase se le entrega un arreglo con los bits que conforman al # del correspondiente caracter
Si el # es pequeno, seguramente ocupara menos de ocho bits, pero para evitar problemas a la hora de querer recuperar el mensaje se entregara siempre numeros de 8 bits
En la clase principal, teniendo dicho arreglo, se encargara de esconder hasta 4 bits dentro del LSB de cada pixel
Asi hasta que se termine el mensaje
"""

"""
**Proceso para leer mensajes 
Capta los primeros 8 bits de la imagen
De ellos, lee su LSB y los guarda en un string para al final entregar su caracter correspondiente
Repite este proceso hasta que se acaben los bits o el mensaje termine...
"""
def main():
    option = sys.argv[1]
    if(option == 'h'):
        hide(sys.argv[2], sys.argv[3], sys.argv[4])
    elif(option == 'u'):
        read(sys.argv[2], sys. argv[3])
    else:
        print("La opcion recibida ha sido invalida, intenta utiliza uno de los siguientes formatos:")
        print("   - h <../Texto> <../Imagen> <../ImagenResultante>")
        print("   - u <../Imagen> <../TextoResultante>")



def hide(text, img, finalImg):
    with open(text) as f:
        contents = f.readlines()
    png.hideMessage(img, text, finalImg)

def read(img, finalText):
    png.readMessage(img, finalText)

if __name__ == "__main__":
    main()
    

