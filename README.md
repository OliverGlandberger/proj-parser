# Project Parser

**Proj Parser** is a command-line tool for generating a visual representation of directory structures while allowing for customizable exclusions via the ability to update a settings file, either manually or through the command-line tool.

## Downloading & Running

If you'd like the executable directly, without the need to build, switch to the **compiled** branch in this repository and download the executable directly.

## Getting Started (_Development_)

On the other hand, if you want to build the project yourself, these instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or newer
- PyInstaller (_for building the executable_)

## Running the Tests

To run the tests in Visual Studio Code, follow these steps:

1. Open the Command Palette **(Ctrl+Shift+P)**.
2. Type `Python: Discover Tests`.
3. Choose `unittest` as the testing framework.
4. Configure the test directory to `./tests`.
5. Click the `Run Tests` icon in the left sidebar.

## Building the Installer

To build the executable with PyInstaller in the Visual Studio Code command line:

1. Open the terminal in Visual Studio Code and make sure you're in the root folder of the project.
2. Run the following command:

```bash
pyinstaller --onefile main.py
```

3. The executable will be located in the `dist` directory.

## Troubleshooting

### Installing PyInstaller

If you haven't installed PyInstaller yet, you can do so using pip:

```bash
pip install pyinstaller
```

### ModuleNotFoundError

If you encounter a `ModuleNotFoundError`, ensure that your Python interpreter is correctly set up in Visual Studio Code and that all dependencies are installed in the environment you're using.

### Test Discovery Fails

Make sure your test files are located in the `./tests` directory and prefixed with `test_`. Ensure that unittest discovery settings in Visual Studio Code are correctly configured as mentioned in the "Running the Tests" section.

## Contributing

Contributions are always welcome, simple as that! Feel free to fork the repository, make changes, and then submit a pull request to the target branch with your proposed changes.

## License

This work is licensed under the terms of the MIT license.
For a copy, see https://opensource.org/licenses/MIT.
