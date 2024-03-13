def main():
    secret = "puppy"
    guess = "_ " * len(secret)
    correct = []
    wrong_guesses = 0 
    guessed_letters = []

    while True:
        print("Guess this", guess)
        letter = input("Guess a letter: ").lower()

        if letter in guessed_letters:
            print("You have already guessed that letter. Try a different letter.")
            continue
        else:
            guessed_letters.append(letter)

        if letter in secret:
            correct.append(letter)
            newguess = ""
            for i in range(0, len(secret)*2, 2): 
                if secret[i//2] == letter:
                    newguess += letter + " "
                else:
                    newguess += guess[i:i+2]  
            guess = newguess
            print("You have guessed the correct letter")
            if "_" not in guess:
                print("Congratulations! You have guessed the correct word!")
                break
        elif not letter.isalpha():
            print("Please input a letter")
        else:
            print("Oops! You have not guessed the correct letter")
            wrong_guesses += 1
            print(f"Wrong guesses left: {6 - wrong_guesses}")
        
        if wrong_guesses == 6:
            print("Sorry, you've run out of guesses. The word was:", secret)
            break

main()