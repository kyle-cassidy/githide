import unittest
from githide import init_command
import os

class TestInitCommand(unittest.TestCase):
    def test_init_creates_gitignore_local_and_updates_exclude(self):
        # Ensure the .gitignore.local file is created and added to .git/info/exclude
        init_command.init()
        self.assertTrue(os.path.exists('.gitignore.local'))
        with open('.git/info/exclude', 'r') as f:
            self.assertIn('.gitignore.local', f.read())

if __name__ == '__main__':
    unittest.main()

