# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:39:34 2023

@author: Kamalov M
"""

import random
from uzwords import uzwords

def get_words():
    word = random.choice(uzwords)
    while "-" in word or " " in word:
        word = random.choice(word)
    return word.upper() 

def display(user_letters,word):
    display_letter =""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_words()
    #So'zdagi harflar
    word_letter = set(word)        