import random

while True:
    user_input = input("Type \'yes\' for dice rolling and type \'no\' for quit (Y/N): ").lower()
    if user_input == 'y':
        print(random.randint(1, 6))
    else:
        print("Thanks for playing")
        break