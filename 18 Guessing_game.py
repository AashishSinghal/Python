
secret_word = "Vatsal"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Hint - My Cousin Younger then aadhya..")

while guess != secret_word and not(out_of_guesses):
    print("Total 3 Guesses, Used :" +str(guess_count))
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")


