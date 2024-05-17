import unittest
from githide import init_command
import os

class TestInitCommand(unittest.TestCase):
    def test_init_creates_gitignore_local(self):
        # Ensure the .gitignore.local file is created
        init_command.init()
        self.assertTrue(os.path.exists('.gitignore.local'))

if __name__ == '__main__':
    unittest.main()

