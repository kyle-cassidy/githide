import os
import unittest
import subprocess

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.test_file = '.gitignore.local'
        # Ensure the test file is clean before each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        # Clean up the test file after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_command(self):
        result = subprocess.run(['python', '-m', 'githide.cli', 'add', 'test_file.txt'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertIn('test_file.txt\n', content)

    def test_init_command(self):
        result = subprocess.run(['python', '-m', 'githide.cli', 'init'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists(self.test_file))

    def test_list_command(self):
        with open(self.test_file, 'w') as f:
            f.write('test_file.txt\n')
        result = subprocess.run(['python', '-m', 'githide.cli', 'list'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('test_file.txt', result.stdout)

    def test_remove_command(self):
        with open(self.test_file, 'w') as f:
            f.write('test_file.txt\n')
        result = subprocess.run(['python', '-m', 'githide.cli', 'remove', 'test_file.txt'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertNotIn('test_file.txt\n', content)

    def test_undo_command(self):
        with open(self.test_file, 'w') as f:
            f.write('test_file.txt\n')
        result = subprocess.run(['python', '-m', 'githide.cli', 'undo'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertNotIn('test_file.txt\n', content)

if __name__ == '__main__':
    unittest.main()
