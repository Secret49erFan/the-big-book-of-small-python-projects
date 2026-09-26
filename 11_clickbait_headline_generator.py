"""Clickbait Headline Generator, by Alex Flores alexflores83 on X
A clickbait headline generator for your soulless content farm website.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, beginner, humor, word"""

import random

# Set up the constants:
OBJECT_PRONOUNS = ["Her", "Him", "Them"]
POSSISIVE_PRONOUNS = ["Her", "His", "Their"]
PERSONAL_PRONOUNS = ["She", "He", "They"]
STATES = ["California", "Texas", "Florida", "New York", "Pennsylvania",
          "Illinois", "Ohio", "Georgia", "North Carolina", "Michigan"]
NOUNS = ["Athlete", "Clown", "Shovel", "Paleo Diet", "Doctor", "Parent",
         "Cat", "Dog", "Chicken", "Robot", "Video Game", "Avocado",
         "Plastic Straw", "Serial Killer", "Telephone Phychic"]
PLACES = ["House", "Attic", "Bank Deposit Box", "School", "Basement",
          "Workplace", "Donut Shop", "Apocalypse Bunker"]
WHEN = ["Soon", "This Year", "Later Today", "RIGHT NOW", "Next Week"]


def main():
    print("Clickbait Headline Generator")
    print("By Alex Flores, @alexflores83 on X")
    print()

    print("Our website needs to trick people into looking at ads!")
    while True:
        print("Enter the number of clickbait headlines to generate:")
        response = input("> ")
        if not response.isdecimal():
            print("Please enter a number.")
        else:
            number_of_headlines = int(response)
            break # Exit the loop once a valid number is entered.

    for _ in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)

        if clickbait_type == 1:
            headline = generate_are_millenials_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_dont_want_you_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reasons_why_headline()
        elif clickbait_type == 8:
            headline = generate_jobs_automated_headline()

        print(headline)
    print()

    website = random.choice(["wobsite", "blag", "Facebuuk", "Googles",
                            "Facesbook", "Tweedie", "Pastagram"])
    when = random.choice(WHEN).lower()
    print(f"Post these to our {website} {when} or your're fired!")


# Each of these functions returns different type of headlines:
def generate_are_millenials_killing_headline():
    noun = random.choice(NOUNS)
    return f"Are Millenials Killing the {noun} Industry?"


def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    return f"Without this {noun}, {plural_noun} could kill you {when}"


def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See how this {state} {noun1} Invented a Cheaper {noun2}"


def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSISIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"


def generate_dont_want_you_know_headline():
    plural_noun1 = random.choice(NOUNS) + "s"
    plural_noun2 = random.choice(NOUNS) + "s"
    return f"What {plural_noun1} Don't Want You To Know About {plural_noun2}"


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f"{number} Gift Ideas to Give Your {noun} From {state}"


def generate_reasons_why_headline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS) + "s"
    # number2 should be no larger than number1:
    number2 = random.randint(1, number1)
    return f"{number1} Reason Why {plural_noun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"


def generate_jobs_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSISIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == "Their":
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1}. {pronoun2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1}. {pronoun2} Was Wrong."


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()