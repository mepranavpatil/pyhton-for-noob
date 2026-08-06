secret_num = 9
i=0
while i < 3:
    guess = int(input("Guess the secret number between 1 and 10: "))
    if guess == secret_num:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Sorry, that's not the secret number. Try again.")
    i += 1
    if i == 3:
        print("You've used all your attempts. The secret number was:", secret_num)