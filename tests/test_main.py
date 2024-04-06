import unittest
from unittest.mock import patch, MagicMock, call
import main

class TestMain(unittest.TestCase):
    @patch('main.input', side_effect=['exit', ''])
    def test_exit_command(self, mocked_input):
        # Test if the program completes execution gracefully on 'exit' command
        main.main()
        mocked_input.assert_called_with("Press Enter to exit...")  # Ensure the final input call is made

    @patch('main.generate_directory_tree', return_value="Directory Tree")
    @patch('main.Settings')
    @patch('main.input', side_effect=['run', 'exit', ''])
    @patch('main.print')
    def test_run_command(self, mocked_print, mocked_input, mocked_settings, mocked_generate_directory_tree):
        # Test the 'run' command
        mocked_settings.return_value.get_exclusions.return_value = []
        main.main()
        mocked_generate_directory_tree.assert_called_once_with('.', exclude=[])

        # Check that the available commands are printed and the expected tree output
        self.assertIn(call("\nAvailable commands: run | add [exclusion] | query | exit"), mocked_print.call_args_list)
        self.assertIn(call("Directory Tree"), mocked_print.call_args_list)

    @patch('main.Settings')
    @patch('main.input', side_effect=['add test_folder', 'exit', ''])
    @patch('main.print')
    def test_add_exclusion_command(self, mocked_print, mocked_input, mocked_settings):
        # Test the 'add [exclusion]' command
        settings_instance = MagicMock()
        mocked_settings.return_value = settings_instance
        main.main()
        settings_instance.add_exclusion.assert_called_once_with('test_folder')

    @patch('main.Settings')
    @patch('main.input', side_effect=['query', 'exit', ''])
    @patch('main.print')
    def test_query_command(self, mocked_print, mocked_input, mocked_settings):
        # Test the 'query' command
        settings_instance = MagicMock()
        settings_instance.get_exclusions.return_value = ['test_folder']
        mocked_settings.return_value = settings_instance
        main.main()

        # Check that the available commands are printed and the exclusions output
        self.assertIn(call("\nAvailable commands: run | add [exclusion] | query | exit"), mocked_print.call_args_list)
        self.assertIn(call("Current exclusions:", ['test_folder']), mocked_print.call_args_list)

if __name__ == '__main__':
    unittest.main()
