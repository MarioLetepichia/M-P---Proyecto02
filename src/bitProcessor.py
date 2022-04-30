"""
Modulo que se encarga de procesar codigos ASCII en binario
@author MarioLetepichia
"""

'''Recibe un str de bits para convertirlos en un binario y entregar el caracter en formato ASCII

    Parameters
    ----------
    listInt : Str que contiene los bits a procesar

    Returns
    -------
    Caracter asociado al numero
'''
def getASCIIcharacter(listInt):
    binary = '0b' + listInt
    return chr(int(binary,2))

'''De caracter a int

    Parameters
    ----------
    character: Caracter a procesar
    
    Returns
    -------
    Numero int asociado a 'character'
'''
def getASCIIcode(character):
    return ord(character)

'''Busca el Bit Menos Significativo

    Parameters
    ----------
    int: Numero del que se quiere buscar su LSB
    
    Returns
    -------
    LSB de 'int'
'''
def getLSB(int):
    if(int&1 == 0):
        return '0'
    else:
        return '1'

'''Recibe un caracter para entragar su codigo ASCII en binario

    Parameters
    ----------
    currCharacter: Caracter a procesar
    
    Returns
    -------
    Representacion en binario de 'currCharacter'
'''
def asciiToBinary(currCharacter):
    if(type(currCharacter) != str and type(currCharacter != int)):
        raise ValueError
    binaryResult = bin(getASCIIcode(currCharacter))
    binaryResult = binaryResult[2:len(binaryResult)]
    compensationBits = 8 - len(binaryResult)
    extraBits = ''
    for i in range(0, compensationBits):
        extraBits += '0'
    return extraBits + binaryResult
    

'''Modifica el LSB para que corresponda con 'newLSB'

    Parameters
    ----------
    int: Numero que sera modificado
    newLSB: Estado deseado del LSB de 'int'

    Returns
    -------
    Numero, en bits, modificado
'''
def modifyLSB(int, newLSB):
    #Hay que encender el bit
    if(newLSB == '1'):
        return int|0b00000001
    else:
        return int&0b11111110