from random import randint


def simulator(number_of_dice: int = 1) -> list[int]:
    return [randint(1, 6) for _ in range(number_of_dice)]


if __name__ == '__main__':
    while True:
        try:
            user_input = input("Enter the number of dice you want to roll or 'exit': ").strip().lower()
            if user_input == "exit":
                print("Exiting...")
                break
            num_dice = int(user_input)
            if num_dice < 0:
                raise ValueError("Number of dice cannot be negative")
            elif num_dice == 0:
                print("No dice to roll")
            else:
                print(*simulator(num_dice), sep=", ")
        except ValueError as e:
            print(e)
