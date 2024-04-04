import splitter
import unittest

class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsimplestring(self):
        r= splitter.split("GOOD 100 490.50")
        self.assertEqual(r,['GOOD','100','490.50'])

    def testtypeconvert(self):
        r = splitter.split("GOOD 100 490.50",[str, int, float])
        self.assertEqual(r,['GOOD',100,490.50])

    def testdelimeter(self):
        r = splitter.split("GOOD,100,490.50",delimeter=",")
        self.assertEqual(r,['GOOD','100','490.50'])

if __name__ =="__main__":
    unittest.main()
