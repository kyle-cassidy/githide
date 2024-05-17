import os
import unittest
from githide.init_command import init

class TestInitCommand(unittest.TestCase):
    def setUp(self):
        self.test_file = '.gitignore.local'
        self.exclude_file = '.git/info/exclude'
        # Ensure the test files are clean before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.exclude_file):
            with open(self.exclude_file, 'r') as f:
                lines = f.readlines()
            with open(self.exclude_file, 'w') as f:
                for line in lines:
                    if line.strip() != self.test_file:
                        f.write(line)

    def tearDown(self):
        # Clean up the test files after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.exclude_file):
            with open(self.exclude_file, 'r') as f:
                lines = f.readlines()
            with open(self.exclude_file, 'w') as f:
                for line in lines:
                    if line.strip() != self.test_file:
                        f.write(line)

    def test_init(self):
        init()
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.exclude_file, 'r') as f:
            content = f.read()
        self.assertIn(self.test_file, content)

if __name__ == '__main__':
    unittest.main()
