import unittest
import os
from src.settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings_file = 'test_settings.json'
        self.settings = Settings(self.settings_file)

    def tearDown(self):
        if os.path.exists(self.settings_file):
            os.remove(self.settings_file)

    def test_initial_exclusions(self):
        self.assertEqual(self.settings.get_exclusions(), ["settings.json", "main.py"], "Initial exclusions should be empty")

    def test_add_exclusion_and_save(self):
        self.settings.add_exclusion('test_file.txt')
        self.assertIn('test_file.txt', self.settings.get_exclusions(), "Exclusion should be added")
        # Reload settings to test persistence
        new_settings = Settings(self.settings_file)
        self.assertIn('test_file.txt', new_settings.get_exclusions(), "Exclusions should persist after reloading")

    def test_default_settings_on_missing_file(self):
        # Ensure the settings file is removed if it exists
        if os.path.exists(self.settings_file):
            os.remove(self.settings_file)
        # Re-initialize settings to simulate loading from a missing file
        new_settings = Settings(self.settings_file)
        # Check that the default exclusions are set as expected
        self.assertEqual(new_settings.get_exclusions(), ["settings.json", "main.py"], "Should revert to default exclusions if settings file is missing")

if __name__ == '__main__':
    unittest.main()
