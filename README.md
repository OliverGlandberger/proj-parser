ProjParser is a command-line tool for generating a visual representation of directory structures while allowing for customizable exclusions via a settings file.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
- Python 3.9 or newer
- PyInstaller (for building the executable)
### Installing Dependencies
To install necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```
## Running the Tests
To run the tests in Visual Studio Code, follow these steps:
1. Open the Command Palette (Ctrl+Shift+P).
2. Type \`Python: Discover Tests\`.
3. Choose \`unittest\` as the testing framework.
4. Configure the test directory to \`./tests\`.
5. Click the \`Run Tests\` icon in the left sidebar.
## Building the Installer
To build the executable with PyInstaller in the Visual Studio Code command line:
1. Open the terminal in Visual Studio Code.
2. Run the following command:
```bash
pyinstaller --onefile main.py
```
3. The executable will be located in the \`dist\` directory.
## Troubleshooting
### Installing PyInstaller
If you haven't installed PyInstaller yet, you can do so using pip:
```bash
pip install pyinstaller
```
### ModuleNotFoundError
If you encounter a \`ModuleNotFoundError\`, ensure that your Python interpreter is correctly set up in Visual Studio Code and that all dependencies are installed in the environment you're using.
### Test Discovery Fails
Make sure your test files are located in the \`./tests\` directory and prefixed with \`test_\`. Ensure that unittest discovery settings in Visual Studio Code are correctly configured as mentioned in the "Running the Tests" section.
## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
## Authors
- **Your Name** - *Initial work* - [YourGitHubUsername](https://github.com/YourGitHubUsername)
See also the list of [contributors](https://github.com/yourproject/contributors) who participated in this project.
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.