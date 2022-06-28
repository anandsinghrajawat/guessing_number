import random
def guess(x):
    random_number = random.randint(1,x)
    guess =0
    while guess != random_number:  
        guess = int(input(f'guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print("guess again it's low")
        elif guess > random_number:
            print("guess again it's too high")
    print (f"congrats you guess correct number{random_number}")
guess(10)        