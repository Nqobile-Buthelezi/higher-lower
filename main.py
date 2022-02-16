import random
from art import logo, vs
from game_data import data


def random_option():
    """Returns a random dictionary from the data array in game_data."""
    option = random.choice(data)
    return option


def format_comparison(option):
    """Formats an option's data down into an easy-to-read sentence, and returns it as a statement."""
    statement = f"{option['name']}, a {option['description']} from {option['country']}"
    return statement


def check_if_correct(first_option, second_option, user_guess):
    """Checks whether the user made the right choice and returns True if they did."""
    if first_option["follower_count"] > second_option["follower_count"]:
        return user_guess == "a"
    elif second_option["follower_count"] > first_option["follower_count"]:
        return user_guess == "b"


def game():
    score = 0
    game_running = True

    while game_running:
        option_a = random_option()
        option_b = random_option()
        while option_a == option_b:
            option_b = random_option()
        print(logo)
        print(f"Compare A: {format_comparison(option_a)}")
        print(vs)
        print(f"Against B: {format_comparison(option_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if check_if_correct(option_a, option_b, guess):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_running = False


game()
