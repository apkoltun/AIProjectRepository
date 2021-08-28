import unittest
import translator

class testEN_FR(unittest.TestCase):
    def testEN_FR_Null(self):
        self.assertNotEqual(translator.english_to_french(None),"Bonjour")
        self.assertEqual(translator.english_to_french(None),"")
    
    def testEN_FR(self):
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')

class testFR_EN(unittest.TestCase):
    def testFR_EN_Null(self):
        self.assertNotEqual(translator.french_to_english(None),"Bonjour")
        self.assertEqual(translator.french_to_english(None),"")
    def testFR_EN(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')

unittest.main()