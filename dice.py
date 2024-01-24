import random


def game_dice():
    """
    Simulates a dice game between the user and computer.

    Rules:
    - Each player chooses two dice from a predefined list.
    - The sum of two random rolls is calculated for both the user and computer.
    - Special conditions: If the sum is 11, the player's total points are multiplied by 11.
                           If the sum is 7, the player's total points are divided by 7.
    - The game continues until one player reaches or exceeds 2001 points.

    Raises:
    KeyboardInterrupt: Raised if the user interrupts the game.
    """
    dice_list = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")
    user_list = []
    computer_list = []
    try:
        while sum(user_list) < 2001 and sum(computer_list) < 2001:
            user_1_dice = input(f"""Choose your dice from {', '.join(map(str, dice_list))}
Choose your a first dice: """)
            user_2_dice = input("Choose your a second dice: ")
            if user_1_dice in dice_list and user_2_dice in dice_list:
                user_1_index = user_1_dice.index("D")
                user_2_index = user_2_dice.index("D")
                for_user_1_index = user_1_dice[user_1_index + 1:]
                for_user_2_index = user_2_dice[user_2_index + 1:]
            else:
                continue

            rounds_sum_1_user = random.randint(1, int(for_user_1_index))
            rounds_sum_2_user = random.randint(1, int(for_user_2_index))
            rounds_sum_3_user = rounds_sum_1_user + rounds_sum_2_user

            if rounds_sum_3_user == 11:
                result = sum(user_list) * 11
                user_list.clear()
                user_list.append(result)
            elif rounds_sum_3_user == 7:
                result = sum(user_list) // 7
                user_list.clear()
                user_list.append(result)
            else:
                user_list.append(rounds_sum_3_user)

            print(f"User: {rounds_sum_3_user}")
            print(f"User have a {sum(user_list)} pts.")

            computer_1_dice = random.choice(dice_list)
            computer_2_dice = random.choice(dice_list)

            computer_1_index = computer_1_dice.index("D")
            computer_2_index = computer_2_dice.index("D")

            for_computer_1_index = computer_1_dice[computer_1_index + 1:]
            for_computer_2_index = computer_2_dice[computer_2_index + 1:]

            rounds_sum_1_computer = random.randint(1, int(for_computer_1_index))
            rounds_sum_2_computer = random.randint(1, int(for_computer_2_index))
            rounds_sum_3_computer = rounds_sum_1_computer + rounds_sum_2_computer

            if rounds_sum_3_computer == 11:
                result_1 = sum(computer_list) * 11
                computer_list.clear()
                computer_list.append(result_1)
            elif rounds_sum_3_computer == 7:
                result_1 = sum(computer_list) // 7
                computer_list.clear()
                computer_list.append(result_1)
            else:
                computer_list.append(rounds_sum_3_computer)

            print(f"Computer: {rounds_sum_3_computer}")
            print(f"Computer have a {sum(computer_list)} pts.")

            if sum(user_list) >= 2001:
                print("User win!")
            elif sum(computer_list) >= 2001:
                print("Computer win!")

    except KeyboardInterrupt:
        print(" Interrupted by user")


game_dice()
