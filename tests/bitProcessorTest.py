"""
Pruebas unitarias para corroborar el correcto funcionamiento de 'procesadorBitsTest'
@author MarioLetepichia
"""

import unittest
import sys
sys.path.append('src')
import bitProcessor as bit

class BitsTest(unittest.TestCase):
    def testAsciiToBinary(self):
        a = 5
        try:
            if(bit.asciiToBinary(5) != bin(ord(a))):
                raise AssertionError
            bit.asciiToBinary(True)
            raise AssertionError
        except ValueError:
            pass
        word = "Gatos#"
        wordBinaries = [71,97,116,111,115,35]
        binArray = []
        for i in range(0, len(word)):
            binArray.append(bit.asciiToBinary(word[i]))
            
        for j in range(0,len(word)):
            if(format(wordBinaries[i], '08b') != bit.asciiToBinary(word[i])):
                raise AssertionError

    def testModifyLSB(self):
        try:
            bit.modifyLSB("hola", "adios")
            raise AssertionError
        except ValueError:
            pass
        numberEx = 186
        self.assertTrue(bit.modifyLSB(numberEx, '1') == numberEx + 1)
        numberEx = 185
        self.assertTrue(bit.modifyLSB(numberEx, '0') == numberEx - 1)
        #Modifica el valor original
        self.assertFalse(numberEx == bit.modifyLSB(numberEx, '0'))
        numberEx = 156
        self.assertFalse(numberEx == bit.modifyLSB(numberEx, '1'))

if __name__ == '__main__':
   unittest.main()