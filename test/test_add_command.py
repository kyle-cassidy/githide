import os
import unittest
from githide.add_command import add

class TestAddCommand(unittest.TestCase):
    def setUp(self):
        self.test_file = '.gitignore.local'
        # Ensure the test file is clean before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        # Clean up the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add(self):
        add('test_file.txt')
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertIn('test_file.txt\n', content)

if __name__ == '__main__':
    unittest.main()
