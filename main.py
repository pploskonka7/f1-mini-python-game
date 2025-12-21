def show_menu():
    print("1. Start wyścigu\n2. Statystyki kierowcy\n3. Zapisz grę\n4. Wczytaj grę\n5. Wyjście\n")
    choice = input("Wybierz opcję: ")
    return choice

def main():
    print("Welcome to the F1 game!")
    while True:
        show_menu()

if __name__ == "__main__":
    main()
