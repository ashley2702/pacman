class Menu:
    def __init__(self):
        self.options = ["Start Game", "Quit"]

    def display(self):
        print("=== Pac-Man Menu ===")
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option}")

    def select_option(self):
        while True:
            try:
                choice = int(input("Select an option (1-2): "))
                if choice == 1:
                    print("Starting the game...")
                    return "start"
                elif choice == 2:
                    print("Quitting. Bye!")
                    exit()
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
