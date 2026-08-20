#This is a simple number guessing game. The program generates a secret number and allows the user to guess it within a limited number of attempts. If the user guesses correctly, they win; otherwise, they lose after exhausting their attempts.
secret_number = 711
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('You lost!')