import unittest
import unittest 
from main import do_stuff

class MainTest(unittest.TestCase):
    def setUp(self):
        print("This is usefull to do some initial setup before Test run.")

    def testcase1(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def testcase2(self):
        test_param = "HI"
        result = do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def testcase3(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def testcase4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'Please Enter the number')

    def testcase4(self):
        test_param = 0
        result = do_stuff(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):
        print("Some clean up")

if __name__ == "__main__":
    unittest.main()