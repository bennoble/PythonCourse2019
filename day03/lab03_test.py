import unittest
from lab03_ben import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
      self.assertEqual("I AM A CAT", shout("I am a cat"))
      with self.assertRaises(AttributeError): shout(5)
      with self.assertRaises(AttributeError): shout([5, 6])
      with self.assertRaises(TypeError): shout("I am a cat" + 12)

    def test_reverse(self):
      self.assertEqual("tac a ma I", reverse("I am a cat"))
      with self.assertRaises(AttributeError): shout(5)
      with self.assertRaises(AttributeError): shout([5, 6])
      with self.assertRaises(TypeError): shout("I am a cat" + 12)
      
    def test_reversewords(self):
      self.assertEqual("cat a am I", reversewords("I am a cat"))
      with self.assertRaises(AttributeError): shout(5)
      with self.assertRaises(AttributeError): shout([5, 6])
      with self.assertRaises(TypeError): shout("I am a cat" + 12)
      
    def test_reversewordletters(self):
      self.assertEqual("I ma a tac", reversewordletters("I am a cat"))
      with self.assertRaises(AttributeError): shout(5)
      with self.assertRaises(AttributeError): shout([5, 6])
      with self.assertRaises(TypeError): shout("I am a cat" + 12)      

    def test_piglatin(self):
      self.assertEqual("arymay errytay", piglatin("Mary Terry"))
      with self.assertRaises(AttributeError): shout(5)
      with self.assertRaises(AttributeError): shout([5, 6])
      with self.assertRaises(TypeError): shout("I am a cat" + 12)


if __name__ == '__main__':
  unittest.main()

