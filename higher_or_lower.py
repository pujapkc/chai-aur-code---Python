from game_data import data
import random

score = 0
should_continue = True


def format_data(celeb):
    celeb_name = celeb["name"]
    celeb_description = celeb["description"]
    celeb_country = celeb["country"]
    return f"{celeb_name}, a {celeb_description}, from {celeb_country}"


def check_answer(guessing, celeb1_followers, celeb2_followers):
    if celeb1_followers > celeb2_followers:
        return guessing == "a"
    else:
        return guessing == "b"


# Generate first random celeb
celeb2 = random.choice(data)

while should_continue:

    celeb1 = celeb2
    celeb2 = random.choice(data)

    while celeb1 == celeb2:
        celeb2 = random.choice(data)

    print(f"Compare A: {format_data(celeb1)}")
    print("VS")
    print(f"Against B: {format_data(celeb2)}")

    guessing = input("Who has more followers? 'A' or 'B': ").lower()

    celeb1_followers = celeb1["follower_count"]
    celeb2_followers = celeb2["follower_count"]

    is_correct = check_answer(guessing, celeb1_followers, celeb2_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
