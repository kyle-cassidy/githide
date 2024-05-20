import os
import unittest
from githide.list_command import list


class TestListCommand(unittest.TestCase):
    def setUp(self):
        self.test_file = ".gitignore.local"
        # Ensure the test file is clean before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        with open(self.test_file, "w") as f:
            f.write("test_file.txt\n")

    def tearDown(self):
        # Clean up the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_list_files(self):
        files = list()
        self.assertIn("test_file.txt", files)


if __name__ == "__main__":
    unittest.main()
