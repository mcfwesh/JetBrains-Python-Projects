import random
words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")


def game():
    choice = random.choice(words)
    initial = '-' * len(choice)
    guessed_letters = []
    trial = 8
    game_status = input('Type "play" to play the game, "exit" to quit: ')
    while (trial > 0 and game_status != 'exit'):
        print(f"\n{initial}")
        reply = input('Input a letter: ')
        if len(reply) != 1:
            print("You should input a single letter")
        elif not reply.islower():
            print("Please enter a lowercase English letter")
        elif reply in initial or reply in guessed_letters:
            print("You've already guessed this letter")
        elif reply not in choice:
            print("That letter doesn't appear in the word")
            trial -= 1

        for index, char in enumerate(choice):
            if reply == char:
                initial = initial[:index] + char + initial[index + 1:]
        if initial == choice:
            break
        guessed_letters.append(reply)
    if trial > 0 and initial == choice:
        print("""You guessed the word!
You survived!
            """)
        game_status = input('Type "play" to play the game, "exit" to quit: ')
    elif trial == 0 and initial != choice:
        print("You lost!")
        game_status = input('Type "play" to play the game, "exit" to quit: ')


game()
