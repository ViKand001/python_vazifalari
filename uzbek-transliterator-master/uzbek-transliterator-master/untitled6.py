# -*- coding: utf-8 -*-
"""
Created on Tue May 23 20:24:54 2023

@author: Kamalov M
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN =""
bot = telebot.TeleBot(TOKEN, parse_mode=None)
matn = input("Matn kiriting:")
print(to_cyrillic(matn))

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))    
    