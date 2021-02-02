import requests
from bs4 import BeautifulSoup
from random import choice


def update_dict():
    """When called, updates the dictionary for the last version available online."""
    soup = BeautifulSoup(requests.get('http://norvig.com/ngrams/sowpods.txt').text, 'html.parser')
    with open('words.txt', 'w+') as file:
        file.write(soup.text)


def game_loop():
    "Starts the game."

    def print_word(a_list, a_guess):
        for i in a_list:
            if i[0] == a_guess:
                i[1] = 1
            if i[1] == 1:
                print(i[0], end='')
            else:
                print('_', end='')

    with open('words.txt', 'r') as f:
        picked_word = choice(f.readlines()).strip('\n')

    original_word = picked_word

    picked_word = [[letter, 0] for letter in picked_word]
    lives = 6
    picked_letters = list()

    while lives != 0:

        while True:
            guess = input('\nPick a letter: ').upper()
            if len(guess) != 1:
                print('Invalid choice.')
                continue
            else:
                break

        if guess not in picked_letters:
            picked_letters.append(guess)
            if guess not in original_word:
                lives -= 1
                print(f'\nIncorrect ! {lives} lives remaining !\n')
                print_word(picked_word, guess)
            else:
                print_word(picked_word, guess)
        else:
            print('Already picked that letter. No life lost tho.')
            print(f'Letters already picked : {picked_letters}')

        if all(list(map(lambda list_in_list: list_in_list[1] == True, picked_word))):
            print('Congrats you guessed the word ! :)')
            break
    else:
        print(f'\nYou lost. The word was : {original_word}')


print("""Hello player !
This is a hangman game.""")

while True:
    print('\nStart new game ?')
    user_response = input('1 - yes/ 0 - no : ')
    if user_response == '1':
        print('\nLet\'s play then. I\'m thinking about a word.\n')
        game_loop()
    elif user_response == '0':
        break
