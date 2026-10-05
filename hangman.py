import random

words = ["python", "coding", "laptop", "internet", "program"]
word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

while wrong < max_wrong:
    display = " ".join(c if c in guessed else "_" for c in word)
    print("\nWord:", display)
    print("Wrong guesses left:", max_wrong - wrong)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter.")
    elif guess in guessed:
        print("Already guessed!")
    else:
        guessed.append(guess)
        if guess not in word:
            wrong += 1
            print("Wrong!")
else:
    print("\n💀 Game over! The word was:", word)