"""
HANGMAN
"""

guess = input('Pon una palabra para tu adversario: ')
hangman = 0

while hangman < 6:
    print(f'La palabra consta de {len(guess)} letras.')