"""
Modulo que se encarga de procesar codigos ASCII en binario
@author MarioLetepichia
"""

def getASCIIcharacter(listInt):
    '''Recibe un str de bits para convertirlos en un binario y entregar el caracter en formato ASCII

    Parameters
    ----------
    listInt : Str que contiene los bits a procesar

    Returns
    -------
    Caracter asociado al numero
    '''

    binary = '0b' + listInt
    return chr(int(binary,2))

def getASCIIcode(character):
    '''De caracter a int

    Parameters
    ----------
    character: Caracter a procesar
    
    Returns
    -------
    Numero int asociado a 'character'
    '''

    return ord(character)


def getLSB(int):
    '''Busca el Bit Menos Significativo

    Parameters
    ----------
    int: Numero del que se quiere buscar su LSB
    
    Returns
    -------
    LSB de 'int'
    '''

    if(int&1 == 0):
        return '0'
    else:
        return '1'


def asciiToBinary(currCharacter):
    '''Recibe un caracter para entragar su codigo ASCII en binario

    Parameters
    ----------
    currCharacter: Caracter a procesar
    
    Returns
    -------
    Representacion en binario de 'currCharacter'
    '''

    if(type(currCharacter) != str and type(currCharacter != int)):
        raise ValueError
    binaryResult = bin(getASCIIcode(currCharacter))
    binaryResult = binaryResult[2:len(binaryResult)]
    compensationBits = 8 - len(binaryResult)
    extraBits = ''
    for i in range(0, compensationBits):
        extraBits += '0'
    return extraBits + binaryResult
    

def modifyLSB(modifiedInt, newLSB):
    '''Modifica el LSB para que corresponda con 'newLSB'

    Parameters
    ----------
    modifiedInt: Numero que sera modificado
    newLSB: Estado deseado del LSB de 'int'

    Returns
    -------
    Numero, en bits, modificado
    '''
    
    if(type(modifiedInt) != int or type(newLSB) != str):
        raise ValueError
    #Hay que encender el bit
    if(newLSB == '1'):
        return modifiedInt|0b00000001
    else:
        return modifiedInt&0b11111110