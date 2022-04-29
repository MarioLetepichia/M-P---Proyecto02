from PIL import Image
import bitProcessor as bit

def readImage(img):
    if(img[len(img)- 4:len(img)] != '.png'):
        raise FileNotFoundError
    return Image.open(img)

def hideMessage(img, textList, resultImgDir):
    #El procesamiento sera dos pixeles por caracter
    png = readImage(img)
    width = png.width
    height = png.height
    copy = png.copy()
    x, y, m, n= 0 , 0 , 0, 1
    for i in range(len(textList)):
        line = textList[i]
        for j in range(len(line)):
            symbol = bit.asciiToBinary(line[j])
            #Saco los dos primeros pixeles
            pixel1 = png.getpixel((x,y))
            pixel2 = png.getpixel((n,m))
            #los modifico
            red1 = bit.modifyLSB(pixel1[0], symbol[0])
            green1 = bit.modifyLSB(pixel1[1], symbol[1])
            blue1 = bit.modifyLSB(pixel1[2], symbol[2])
            transparency1 = bit.modifyLSB(pixel1[3], symbol[3])
            newPixel1 = (red1, green1, blue1, transparency1)
            red2 = bit.modifyLSB(pixel2[0], symbol[4])
            green2 = bit.modifyLSB(pixel2[1], symbol[5])
            blue2 = bit.modifyLSB(pixel2[2], symbol[6])
            transparency2 = bit.modifyLSB(pixel2[3], symbol[7])
            newPixel2 = (red2, green2, blue2, transparency2)
            copy.putpixel((x,y), newPixel1)
            copy.putpixel((n,m), newPixel2)
            #actualizo correctamente los indices x,y,n,m
            x+= 2
            if(x >= width):
                x = 0
                y += 1
            n += 2
            if(n >= width):
                n = 0
                m += 1
            if(m >= height or y >= height):
                print("Ya no quedan mas pixeles por procesar.")
                print(symbol)
    copy.save(resultImgDir)

def readMessage(img, resultText):
    #Se leen pixeles de dos en dos
    text = ' '
    png = readImage(img)
    width = png.width
    height = png.height
    x, y, m, n= 0 , 0 , 0, 1
    characterBin = '1'
    while(characterBin != "00000000"):
        #Obtenemos los pixeles
        pixel1 = png.getpixel((x,y))
        pixel2 = png.getpixel((n,m))
        print(pixel1)
        print(pixel2)
        #Leemos el contenido de cada uno de ellos
        characterBin = ''
        for i in range(4):
            characterBin += bit.getLSB(pixel1[i])
        for i in range(4):
            characterBin += bit.getLSB(pixel2[i])
        text += bit.getASCIIcharacter(characterBin)
        x += 2
        if(x >= width):
            x = 0
            y += 1
        n += 2
        if(n >= width):
            n = 0
            m +=1
        if(m >= height or y >= height):
            print("Ya no quedan mas pixeles por procesar.")

    file2write = open(resultText, 'w')
    file2write.write(text)
    file2write.close()

##No estoy seguro si los pixeles estan siendo modificados correctamente