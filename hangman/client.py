from hangman.game import Game
from hangman.game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f'Слово состоит из {letters_count} букв')
print('Попробуй отгадать слово буква за буквой')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Выбери букву. \n')
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))
    print(f'Осталось попыток {game.remaining_tries}')
    print(f'Выбранные буквы {chars_list_to_str(game.tried_letters)}')


if game.game_status == GameStatus.LOST:
    print('Ты повешан...')
    print(f'Загаданное слово было - {game.word}')
else:
    print("Поздравляю, Вы победили!")
