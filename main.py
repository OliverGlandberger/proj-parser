import logging
from src.settings import Settings
from src.utils import generate_directory_tree

def main():
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("proj_struct.log", mode='w'),
                            logging.StreamHandler()
                        ])

    settings = Settings()

    while True:
        print("\nAvailable commands: run | add [exclusion] | query | exit")
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
            tree = generate_directory_tree('.', exclude=exclusions)
            print(tree)
        elif command == "add" and len(commands) > 1:
            exclusion = commands[1]
            settings.add_exclusion(exclusion)
            logging.info(f"Added exclusion: {exclusion}")
        elif command == "query":
            exclusions = settings.get_exclusions()
            print("Current exclusions:", exclusions)
        else:
            logging.error("Unknown command. Please try again.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
