from urllib.parse import uses_query

import art
import game_data
import random

print(art.logo)

final_score=0

def format_name(dish):
    return f"{dish['name']} - {dish['description']}"


def compare_dish(dishA,dishB):
    if dishA['search_volume'] > dishB['search_volume']:
        return int(dishA['search_volume'])
    else:
        return int(dishB['search_volume'])

def play_game():

    dish_A = random.choice(game_data.game_data)

    dish_B = random.choice(game_data.game_data)
    userinput = 0
    higher = 0
    while userinput == higher:
        if dish_A == dish_B:
            dish_B = random.choice(game_data.game_data)
        print("\n*****************************************************************************************************")
        print(f"Compare A: {format_name(dish_A)}")
        print(art.vs)
        print(f"Against B:{format_name(dish_B)}")

        guess = input("\nWhich dish appeared most in Google searches 2024? Type 'A' or 'B'")

        if guess == 'A':
            userinput = int(dish_A['search_volume'])
        elif guess == 'B':
            userinput = int(dish_B['search_volume'])
        else:
            print("Please give correct input A or B" )

        higher = compare_dish(dish_A,dish_B)

        if userinput == higher:
            global final_score
            final_score= final_score +1
            print(f"Your guess is correct. Current score is {final_score}")
            dish_A = dish_B
            dish_B = random.choice(game_data.game_data)
        else:
            print("Sorry!! Your guess is wrong")

play_game()
print(f"Your final score is :{final_score}")