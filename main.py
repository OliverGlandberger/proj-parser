import logging
from src.settings import Settings
from src.utils import generate_directory_tree, parse_gitignore

def main():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("proj_struct.log", mode='w'),
                            logging.StreamHandler()
                        ])

    settings = Settings()

    while True:
        print("\nAvailable commands: run | add [exclusion] | toggle [setting] | query | exit")
        command_input = input("Enter a command: ").strip().lower()
        commands = command_input.split()

        if not commands:
            continue

        command = commands[0]
        if command == "exit":
            break
        elif command == "run":
            logging.info("Generating directory tree...")
            exclusions = settings.get_exclusions()
            use_gitignore = settings.settings.get('use_gitignore', False)
            if use_gitignore:
                try:
                    exclusions.extend(parse_gitignore('.gitignore'))
                    print("HERE")
                    print(exclusions)
                except Exception as e:
                    logging.error(f"Failed to parse .gitignore: {e}")
                    print(f"Error: Failed to parse .gitignore: {e}")

            tree = generate_directory_tree('.', exclude=exclusions)
            print(tree)
            logging.info("\n" + tree)
        elif command == "add" and len(commands) > 1:
            exclusion = commands[1]
            settings.add_exclusion(exclusion)
            logging.info(f"Added exclusion: {exclusion}")
        elif command == "toggle" and len(commands) > 1:
            setting = commands[1]
            settings.toggle_setting(setting)
            logging.info(f"Toggled setting: {setting}")
        elif command == "query":
            exclusions = settings.get_exclusions()
            print("Current exclusions:", exclusions)
            use_gitignore = settings.settings.get('use_gitignore', False)
            print("Use .gitignore:", use_gitignore)
        else:
            logging.error("Unknown command. Please try again.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
