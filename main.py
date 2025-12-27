def show_menu():
    print("\n===== F1 Game Menu =====\n1. Start wyścigu\n2. Statystyki kierowcy\n3. Zapisz grę\n4. Wczytaj grę\n5. Wyjście\n")
    choice = input("Wybierz opcję: ")
    return choice

def main():
    print("Welcome to the F1 game!")
    while True:
        choice = show_menu()
        if choice == '1':
            print("Starting race...")
        elif choice == '2':
            print("Showing driver statistics...")
        elif choice == '3':
            print("Saving game...")
        elif choice == '4':
            print("Loading game...")
        elif choice == '5':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
