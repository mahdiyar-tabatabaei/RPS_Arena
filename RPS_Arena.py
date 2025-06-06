import random

results = []

choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

def get_choice_name(choice):
    return choices.get(choice, "Unknown")

def determine_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "User"
    else:
        return "Computer"

def print_menu():
    print("--------| Rock Paper Scissors Game |--------")
    print("1. New game")
    print("2. Show the result of the last game")
    print("3. Show all results")
    print("4. Exit the program")

def game():
    user_name = input("Enter your name: ").strip()

    while True:
        try:
            rounds_count = int(input("Enter how many rounds you want to play: ").strip())
            if rounds_count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nStarting a {rounds_count}-round game for {user_name}!\n")

    user_wins = 0
    computer_wins = 0
    draws = 0

    for round_num in range(1, rounds_count + 1):
        print(f"--- Round {round_num} ---")
        while True:
            try:
                user_choice = int(input("Choose: 1 (Rock), 2 (Paper), 3 (Scissors): "))
                if user_choice not in choices:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        computer_choice = random.randint(1, 3)

        print(f"{user_name} chose: {get_choice_name(user_choice)}")
        print(f"Computer chose: {get_choice_name(computer_choice)}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "Draw":
            result = "Draw"
            draws += 1
        elif winner == "User":
            result = f"{user_name} wins!"
            user_wins += 1
        else:
            result = "Computer wins!"
            computer_wins += 1

        print(f"Result: {result}\n")

        result_record = f"Round {round_num}: {user_name} ({get_choice_name(user_choice)}) vs Computer ({get_choice_name(computer_choice)}) → {result}"
        results.append(result_record)

    print(f"=== Game Over ===")
    print(f"{user_name}'s wins: {user_wins}")
    print(f"Computer's wins: {computer_wins}")
    print(f"Draws: {draws}")

def show_last_result():
    if results:
        print(f"\nLast game result:\n{results[-1]}")
    else:
        print("\nNo results to show yet.")

def show_all_results():
    if results:
        print("\nAll game results:")
        for idx, res in enumerate(results, start=1):
            print(f"{idx}. {res}")
    else:
        print("\nNo results to show yet.")

while True:
    print_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        game()
    elif choice == 2:
        show_last_result()
    elif choice == 3:
        show_all_results()
    elif choice == 4:
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid option. Please choose from the menu.")
