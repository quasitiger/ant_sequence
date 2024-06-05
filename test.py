import unittest
import list_run
import str_run

class FunctionTest(unittest.TestCase):
    def test_list_run(self):
        median_value = list_run.run(5)
        self.assertEqual(median_value,[1,2])

        median_value = list_run.run(8)
        self.assertEqual(median_value,[2,1])

    def test_str_run(self):
        median_value = str_run.run(5)
        self.assertEqual(median_value,'12')

        median_value = str_run.run(8)
        self.assertEqual(median_value,'21')

if __name__ == '__main__':
    unittest.main()