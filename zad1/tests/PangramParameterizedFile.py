import unittest
from sample.Pangram import *

class PangramParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/pangram_data_test")
      tmpPangram = Pangram()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(";")
            inp, result = data[0], data[1].strip("\n")
            self.assertEqual(tmpPangram.check(inp), result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
