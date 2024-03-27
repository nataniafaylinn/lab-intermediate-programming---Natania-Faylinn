import random

word_dictionary = ["capybara", "horse", "elephant", "tiger", "otter", "giraffe", "quokka", "panda"]
global score
score = {'win': 0, 'lose': 0}

def main_lagi():
    global score
    while True:
        input_user = input(str("Do you want to play again? (yes or no) ")).lower()
        if input_user == "yes":
            main()
        elif input_user == "no":
            print("Thank you for playing!")
            break
        else:
            print("You should input rather (yes) or (no) only")

def main():
    secret = random.choice(word_dictionary)
    word_dictionary.remove(secret)
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
                print("Congratulations! You have guessed the correct word", secret, "!")
                score['win'] += 1
                main_lagi()
                break
        elif not letter.isalpha():
            print("Please input a letter")
        else:
            print("Oops! You have not guessed the correct letter")
            wrong_guesses += 1
            print(f"Wrong guesses left: {6 - wrong_guesses}")
        
        if wrong_guesses == 6:
            print("Sorry, you've run out of guesses. The word was:", secret)
            score['lose'] += 1
            break

main()
print(f"Final score -> Wins: {score['win']}, Losses: {score['lose']}")
