import random

secret_number = random.randint(0,500)

print(secret_number)

guess = None

    

while guess != secret_number:
    guess = int(input("guess the number i'm thinking about it is between 0 and 500"))

    match secret_number:
        case n if guess > secret_number:
            print("guess lower")

        case n if guess < secret_number:
            print("guess highr")

        case _:
            print("congrats")
            break
