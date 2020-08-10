"""CSC108 Assignment 2 functions"""

from typing import List

# Used to determine whether to encrypt or decrypt
ENCRYPT = 'e'
DECRYPT = 'd'
ALPHABET_LEN = 26


def clean_message(message: str) -> str:
    """Return a string with only uppercase letters from message with non-
    alphabetic characters removed.
    
    >>> clean_message('Hello world!')
    'HELLOWORLD'
    >>> clean_message("Python? It's my favourite language.")
    'PYTHONITSMYFAVOURITELANGUAGE'
    >>> clean_message('88test')
    'TEST'
    """
    new_str = ''
    for i in message:
        if i.isalpha():
            new_str += i.upper()
    return new_str

def encrypt_letter(letter: str, keystream: int) -> str:  
    """Return a string containing a new character after alphabetical index 
    of letter has been added to the keystring and had modulo 26 applied.
    
    >>> encrypt_letter('H', 7)
    O
    >>> encrypt_letter('D', 21)
    Y
    """
    alpha_index = ord(letter) - ord('A') 
    encrypted_num = alpha_index + keystream
    return chr((encrypted_num % 26) + ord('A'))
    

def decrypt_letter(letter: str, keystream: int) -> str: 
    """Return a string containing the original character after the keystream 
    has been subtracted from the letters alphabetical index and modulo 26 is 
    applied.
    
    >>> decrypt_letter('O', 7)
    H
    >>> decrypt_letter('Y', 21)
    D
    """
    alpha_index = ord(letter) - ord('A') 
    encrypted_num = alpha_index - keystream
    return chr((encrypted_num % 26) + ord('A'))
        
def is_valid_deck(deck: List[int]) -> bool:  
    """Return True if and onlt if deck contains every integer value 
    from 1 to the length of deck.
    
    >>> is_valid_deck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    True 
    >>> is_valid_deck([1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 12, 12])
    False 
    >>> is_valid_deck([1,2,3,4,5,6,7,8])
    True  
    >>> is_valid_deck([1, 1])
    False 
    """
    deck_range = []
    for i in range(1, (len(deck) + 1)):
        deck_range.append(i)
    is_valid = True  
    for i in deck:
        if deck.count(i) != 1:
            is_valid = False 
        elif i not in deck_range:
            is_valid = False 
    return is_valid

def swap_cards(deck: List[int], index: int) -> None:
    """Return None. Rearange deck such that the card at index 
    and the card following have swapped places.
    
    >>> swap_cards([1, 2, 3, 4, 5, 6], 2)
    >>> deck
    [1, 2, 4, 3, 5, 6]
    >>> swap_cards([1, 2,3, 4, 5, 6, 7, 8, 9], 8)
    >>> deck
    [9, 2, 3, 4, 5, 6, 7, 8, 1]
    """
    x = deck[index]
    z = deck[0]
    
    if index < (len(deck) - 1):
        y = deck[index + 1]
        deck.pop(index)
        deck.pop(index)
        deck.insert(index, y)
        deck.insert((index + 1), x)
        
    elif index == (len(deck) - 1):
        deck.pop(0)
        deck.pop(index - 1)
        deck.insert(0, x)
        deck.insert(index, z)
        
def get_small_joker_value(deck: List[int]) -> int:
    """Return the value of the small joker, represented by the 
    second largest value in deck.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> get_small_joker_value(deck)
    27
    >>> get_small_joker_value([1, 2, 3, 4, 5, 6, 7])
    6
    """
    return (len(deck) - 1)
    
def get_big_joker_value(deck: List[int]) -> int:
    """Return the value of the big joker, represented
    by the largest value in deck.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> get_big_joker_value(deck)
    28
    >>> get_big_joker_value([1, 2, 3, 4, 5, 6, 7])
    7
    """
    return len(deck)
    
def move_small_joker(deck: List[int]) -> None:
    """Return None. Move the small joker, defined by the second highest 
    value in the deck, one index to the right, by swapping it with the 
    value following it. If it is at the last index, swap it with the value 
    at the first index.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> move_small_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 27]
    >>> deck = [1, 2, 3, 4, 5, 6, 7]
    >>> move_small_joker(deck)
    >>> deck
    [1, 2, 3, 4, 5, 7, 6]
    
    """
    swap_cards(deck, deck.index(get_small_joker_value(deck)))
    
def move_big_joker(deck: List[int]) -> None:
    """Return None. Swap the big joker twice, such that is moved 
    two cards down the deck.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> move_big_joker(deck)
    >>> deck
    [2, 10, 3, 4, 5, 6, 7, 8, 9, 1]
    >>> deck = [1, 2, 3, 4, 5, 6, 7]
    >>> move_big_joker(deck)
    >>> deck
    [2, 7, 3, 4, 5, 6, 1]
    """
    swap_cards(deck, deck.index(get_big_joker_value(deck)))
    swap_cards(deck, deck.index(get_big_joker_value(deck)))
    
def triple_cut(deck: List[int]) -> None: 
    """Return None. Mutate the deck such that all of the cards to the left of 
    the big joker and all of the cards to the right of the small joker swap 
    places.
    
    Precondition: is_valid_deck == True 
    
    >>> triple_cut([1, 2, 3, 7, 4, 6, 5])
    >>> deck 
    [5, 7, 4, 6, 1, 2, 3]
    >>> triple_cut([5, 7, 4, 6, 1, 2, 3])
    >>> deck
    [1, 2, 3, 7, 4, 6, 5]
    """
    if (deck.index(get_big_joker_value(deck)) < 
            deck.index(get_small_joker_value(deck))):
        deck[:] = deck[(deck.index(get_small_joker_value(deck)) + 1):] + \
            deck[(deck.index(get_big_joker_value(deck))):\
                 (deck.index(get_small_joker_value(deck)) + 1)] + \
            deck[:deck.index(get_big_joker_value(deck))]
        
    elif (deck.index(get_big_joker_value(deck)) > 
          deck.index(get_small_joker_value(deck))):
        deck[:] = deck[(deck.index(get_big_joker_value(deck)) + 1):] + \
            deck[(deck.index(get_small_joker_value(deck))):\
                 (deck.index(get_big_joker_value(deck)) + 1)] + \
            deck[:deck.index(get_small_joker_value(deck))]
        

def insert_top_to_bottom(deck: List[int]) -> None:
    """Return None. Mutate deck such that the number of cards equal to the
    value of the last card in the deck are moved from the top of the deck to 
    the bottom, directly on top of the bottom card.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [5, 8, 11, 14, 17, 20, 23, 26, 28, 9, 12, 15, 18, 21, 24, 
    2, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16, 19, 
    22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> deck = [2, 3, 5, 4, 6, 1]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [3, 5, 4, 6, 2, 1]
    """ 
    bottom_card = deck[-1]
    
    if bottom_card != get_big_joker_value(deck):
        deck[:] = deck[bottom_card:-1] + deck[:bottom_card]
        deck.append(bottom_card)
    elif bottom_card == get_big_joker_value(deck):
        bottom_card = get_small_joker_value(deck)
        deck[:] = deck[bottom_card:-1] + deck[:bottom_card]
        deck.append(get_big_joker_value(deck) + 1)
    
        
def get_card_at_top_index(deck: List[int]) -> int: #make better 
    """Return the value of the card at the index of the value of the top card.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13,
    16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> get_card_at_top_index(deck)
    11
    >>> deck = [1, 2, 3, 7, 4, 6, 5]
    >>> get_card_at_top_index(deck)
    2
    """
    if deck[0] != get_big_joker_value(deck):
        top_card = deck[0]
        keystream = deck[top_card]
        return keystream
    
    elif deck[0] == get_big_joker_value(deck):
        top_card = deck[get_small_joker_value(deck)]
        keystream = deck[top_card]
        return keystream 
    else:
        return None

def get_next_keystream_value(deck: List[int]) -> int:
    """Repeat the previous five functions to re-mutate the deck in order 
    to generate a new keystream value. If the keystream value is either of the 
    jokers, repeat the function to generate the next keystream value.
    
    Precondition: is_valid_deck == True 
    
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(deck)
    11
    >>> get_next_keystream_value(deck)
    9 
    """
    valid = False
    while valid is not True:
        move_small_joker(deck)
        move_big_joker(deck)
        triple_cut(deck)
        insert_top_to_bottom(deck)
        
        if get_card_at_top_index(deck) == get_big_joker_value(deck):
            valid = False 
        elif get_card_at_top_index(deck) == get_small_joker_value(deck):
            valid = False 
        else:
            valid = True  
            
    return get_card_at_top_index(deck)

def process_messages(deck: List[int], messages: List[str], action: str) -> \
List[str]: 
    """Return a list of encrypted messages if action is ENCRYPT using the 
    keystream values generated using deck. If the action is DECRYPT, using the 
    same initial deck, return a list of decrypted messages.
    
    Precondition: is_valid_deck == True 
    
    >>> process_messages([1, 2, 3, 4, 5, 6, 7], ['GOODWILL'], ENCRYPT)
    ['ITTGXKNN']
    >>> process_messages([1, 2, 3, 4, 5, 6, 7], messages, DECRYPT)
    ['GOODWILL']
    """
    keystream = []
    for message in messages:
        messages[messages.index(message)] = clean_message(message)
        for letter in message:
            keystream.append(get_next_keystream_value(deck))        
            
    if action == ENCRYPT:    
        for message in messages:
            encrypted_message = ''
            for letter in message:
                i = 0
                encrypted_message += encrypt_letter(letter, \
                keystream[i])
                i += 1
            messages[messages.index(message)] = encrypted_message    
        return messages 
    
    elif action == DECRYPT:
        for message in messages:
            decrypted_message = ''
            for letter in message:
                i = 0
                decrypted_message += decrypt_letter(letter, \
                keystream[i])
                i += 1
            messages[messages.index(message)] = decrypted_message 
        return messages      
    else:
        return None 
    
# This if statement should always be the last thing in the file, below all of
# your functions:
if __name__ == '__main__':
    """Did you know that you can get Python to automatically run and check
    your docstring examples? These examples are called "doctests".

    To make this happen, just run this file! The two lines below do all
    the work.

    For each doctest, Python does the function call and then compares the
    output to your expected result.
    
    NOTE: your docstrings MUST be properly formatted for this to work!
    In particular, you need a space after each >>>. Otherwise Python won't
    be able to detect the example.
    """
    #import doctest
    #doctest.testmod()
