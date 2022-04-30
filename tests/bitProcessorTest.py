"""
Pruebas unitarias para corroborar el correcto funcionamiento de 'procesadorBitsTest'
@author MarioLetepichia
"""

import unittest
import sys
sys.path.append('src')
import bitProcessor as bit

class BitsTest(unittest.TestCase):
    def asciiToBinaryTest(self):
        #Cuando recibe un int & bool
        a = 5
        try:
            if(bit.asciiToBinary(5) != bin(ord(a))):
                raise AssertionError
            bit.asciiToBinary(True)
            raise AssertionError
        except ValueError:
            pass
        #Una palabras; es decir, lista de binarios
        word = "Gatos#"
        wordBinaries = [71,97,116,111,115,35]
        binArray = []
        for i in range(0, len(word)):
            binArray.append(bit.asciiToBinary(word[i]))
            
        for j in range(0,len(word)):
            if(bin(wordBinaries[i]) != bit.asciiToBinary(word[i])):
                raise AssertionError

    def modifyLSBTest(self):
        #El binario recibido tiene que tener exactamente len()=10
        self.assertRaises(ValueError, bit.modifyLSB("hola"))
        self.assertRaises(ValueError, bit.getASCII("0b1111101111101"))
        #El LSB ya tiene el valor indicado por 'newLSB'
        binary = "0b1011101101"
        self.assertTrue(bit.modifyLSB(binary, 1) == binary)
        binary = "0b1011100000"
        self.assertTrue(bit.modifyLSB(binary, 0) == binary)
        #Modifica el valor original
        binary = "0b1011101101"
        self.assertFalse(binary == bit.modifyLSB(binary, 0))
        binary = "0b1011101000"
        self.assertFalse(binary == bit.modifyLSB(binary, 1))
    
if __name__ == '__main__':
   unittest.main()