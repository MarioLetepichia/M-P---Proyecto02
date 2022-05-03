"""
Modulo encargado de procesar la imagen para ocultar texto o descifrarlo
@author MarioLetepichia
"""
from PIL import Image
import bitProcessor as bit

def readImage(img):
    '''Lee un archivo imagen

    Parameters
    ----------
    img: Dirreccion de la imagen

    Returns
    -------
    Objeto 'Image' con el cual se podra procesar a 'img'
'''

    if(img[len(img)- 4:len(img)] != '.png'):
        raise FileNotFoundError
    return Image.open(img)


def hideMessage(text, img, resultImg):
    '''Oculta un texto en la imagen utilizando estenografia por LSB

    Parameters
    ----------
    img: Direccion de la imagen
    text: Direccion del texto a ocultar
    resultImg: Direccion donde se desea guardar la imagen resultante
'''

    png = readImage(img)
    with open(text) as f:
        textList = f.readlines()
    width = png.width
    height = png.height
    copy = png.copy()
    x, y, n, m= 0 , 0 , 1, 0
    for i in range(len(textList)):
        line = textList[i]
        for j in range(len(line)):
            symbol = bit.asciiToBinary(line[j])
            pixel1 = png.getpixel((x,y))
            pixel2 = png.getpixel((n,m))
            newPixels = modifyPixels(pixel1, pixel2, symbol)
            #DEBUG
            print('===============')
            print(' (x,y)   (n,m)')
            print((x,y), (n,m))
            print(pixel1, pixel2)
            print('---------------')
            print(newPixels[0], newPixels[1])
            print(symbol + '   ' + bit.getASCIIcharacter(symbol))
            copy.putpixel((x,y), newPixels[0])
            copy.putpixel((n,m), newPixels[1])
            x+= 2
            if(x >= width):
                x = x%width
                y += 1
            n += 2
            if(n >= width):
                n = n%width
                m += 1
            if(m >= height or y >= height):
                print("Ya no quedan mas pixeles por procesar.")
                print(symbol)
    pixel1 = png.getpixel((x,y))
    pixel2 = png.getpixel((n,m))
    newPixels = modifyPixels(pixel1, pixel2, "00000000")
    copy.putpixel((x,y), newPixels[0])
    copy.putpixel((n,m), newPixels[1])
    copy.save(resultImg)

def readMessage(img, resultText):
    '''Procesa una imagen para recuperar los LSB y generar un texto a partir de ellos.

    Parameters
    ----------
    img: Direccion de la imagen
    resultText: Direccion en la que se desea guardar el texto resultante
'''

    text = ''
    png = readImage(img)
    width = png.width
    height = png.height
    x, y, n, m= 0 , 0 , 1, 0
    characterBin = '1'
    while(characterBin != '00000000'):
        pixel1 = png.getpixel((x,y))
        pixel2 = png.getpixel((n,m))
        characterBin = ''
        for i in range(4):
            characterBin += bit.getLSB(pixel1[i])
        for i in range(4):
            characterBin += bit.getLSB(pixel2[i])
        finalChar = bit.getASCIIcharacter(characterBin)
        if(ord(finalChar) != 0):
            text += finalChar
        x += 2
        if(x >= width):
            x = x%width
            y += 1
        n += 2
        if(n >= width):
            n = n%width
            m +=1
        if(m >= height or y >= height):
            print("Ya no quedan mas pixeles por procesar.")

    file2write = open(resultText, 'w')
    file2write.write(text)
    file2write.close()

def modifyPixels(p1, p2, symb):
    '''Modifica los LSB de los bits dentro de los pixeles recibidos para almacenar
un codigo ASCII. Para esto necesita dos pixeles

    Parameters
    ----------
    p1: Pixel #1 a procesar
    p2: Pixel #2 a procesar
    symb: Representacion binaria del codigo ASCII que se almanecera en 'p1' y 'p2'
'''

    red1 = bit.modifyLSB(p1[0], symb[0])
    green1 = bit.modifyLSB(p1[1], symb[1])
    blue1 = bit.modifyLSB(p1[2], symb[2])
    transparency1 = bit.modifyLSB(p1[3], symb[3])
    newPixel1 = (red1, green1, blue1, transparency1)
    red2 = bit.modifyLSB(p2[0], symb[4])
    green2 = bit.modifyLSB(p2[1], symb[5])
    blue2 = bit.modifyLSB(p2[2], symb[6])
    transparency2 = bit.modifyLSB(p2[3], symb[7])
    newPixel2 = (red2, green2, blue2, transparency2)
    return [newPixel1, newPixel2]