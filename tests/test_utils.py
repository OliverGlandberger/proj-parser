import unittest
import os
import tempfile
import shutil  # Import the shutil module
from src.utils import generate_directory_tree

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.cleanup_directory(self.test_dir)

        # Create subdirectories and files for testing
        os.makedirs(os.path.join(self.test_dir, 'subdir1'), exist_ok=True)
        os.makedirs(os.path.join(self.test_dir, 'subdir2'), exist_ok=True)
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("Test file 1")
        with open(os.path.join(self.test_dir, 'subdir1', 'file2.txt'), 'w') as f:
            f.write("Test file 2")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def cleanup_directory(self, directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def test_generate_directory_tree_without_exclusions(self):
        tree = generate_directory_tree(self.test_dir)
        self.assertIn('subdir1', tree, "Subdirectory should be listed in the tree")
        self.assertIn('file1.txt', tree, "File should be listed in the tree")

    def test_generate_directory_tree_with_exclusions(self):
        exclusions = ['subdir1', 'file1.txt']
        tree = generate_directory_tree(self.test_dir, exclude=exclusions)
        self.assertNotIn('subdir1', tree, "Excluded directory should not be listed in the tree")
        self.assertNotIn('file1.txt', tree, "Excluded file should not be listed in the tree")

if __name__ == '__main__':
    unittest.main()
