# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:10:49 2021
@author: Nepryaev
"""
import random
import math
from random import choice
from random import randrange
from typing import List
import random


s_cards_list = [['6♠', 6], ['7♠', 7], ['8♠', 8], ['9♠', 9], ['10♠', 10], ['В♠', 2], ['Д♠', 3], ['К♠', 4], ['Т♠', 11],
                ['6♥', 6], ['7♥', 7], ['8♥', 8], ['9♥', 9], ['10♥', 10], ['В♥', 2], ['Д♥', 3], ['К♥', 4], ['Т♥', 11],
                ['6♦', 6], ['7♦', 7], ['8♦', 8], ['9♦', 9], ['10♦', 10], ['В♦', 2], ['Д♦', 3], ['К♦', 4], ['Т♦', 11],
                ['6♣', 6], ['7♣', 7], ['8♣', 8], ['9♣', 9], ['10♣', 10], ['В♣', 2], ['Д♣', 3], ['К♣', 4], ['Т♣', 11]]


game_start_end = 'y';
player_y_n     = 1;
deck_cards_nums     = list(range(0, 36)) 

bot_points    = 0
player_points = 0

bot_cards_sum    = 0
player_cards_sum = 0

bot_cards_list    = []
player_cards_list = []
player_choice = 'n'
bot_pass     = False
player_pass  = False
first_card   = True 
first_set  = True 
set_off = False
card_num     = 0
cards_digit  = 0
cards_names  = 0


print("Милости прошу к игральному шалашу")
game_start_end = str(input("Сыграем? (y/n): "))

while True:
    
    if  first_set == True:
        first_set = False
    else:   
         game_start_end = str(input("Сыграем еще? (y/n): "))  
    
    if game_start_end  != 'y':
        break

    set_off = False      
    bot_cards_list    = []
    player_cards_list = []
    bot_cards_sum     = 0
    player_cards_sum  = 0
    card_num = 0
    first_card   = True 
    bot_pass     = False
    player_pass  = False
    random.shuffle(deck_cards_nums)    
    while set_off == False:
       
        if   (sum(bot_cards_list) < 17) and  bot_pass != True:
             bot_cards_list.append(s_cards_list[deck_cards_nums[card_num]][1])
             card_num = card_num + 1
        elif (sum(bot_cards_list) >= 17) and (sum(bot_cards_list) <= 21) and  (bool(random.getrandbits(1)) == True) and  bot_pass != True:
             bot_cards_list.append(s_cards_list[deck_cards_nums[card_num]][1])
             card_num = card_num + 1
        else:
           bot_pass = True
           print(" Бот пас ♣") 
        print("Сумма Бота:", sum(bot_cards_list))
    
        if   (player_pass == False):
            if  first_card == True:
                player_cards_list.append(s_cards_list[deck_cards_nums[card_num]])
                card_num = card_num + 1
                first_card = False
            else:  
                 player_choice = str(input("Еще? (y/n): "))
                 if  (player_choice == 'y'):
                     player_cards_list.append(s_cards_list[deck_cards_nums[card_num]])
                     card_num = card_num + 1
                     player_pass = False 
                 else:
                     player_pass = True 
            
        cards_digit  = [el[1] for el in player_cards_list[0:len(player_cards_list)]]  
        cards_names = [el[0] for el in player_cards_list[0:len(player_cards_list)]]   
        print("Твои карты:",str(cards_names),"Сумма:", str(sum(cards_digit)))
    
        if (player_pass == True) and (bot_pass == True):
            bot_cards_sum    = sum(bot_cards_list)
            player_cards_sum = sum(cards_digit)
            if  (player_cards_sum > 21) and  (bot_cards_sum > 21):
                print("♥ Ничья ♥")
                print("Счет Игрок [",str(player_points),"] Бот [",str(bot_points), ']')
            elif player_cards_sum == bot_cards_sum:
                print("♣ Ничья ♣")
                print("Счет Игрок [",str(player_points),"] Бот [",str(bot_points), ']')
            elif (player_cards_sum <= 21) and  (bot_cards_sum > 21):
                player_points = player_points + 1
                print("♣ Фарт - Твоя взяла ")
                print("Счет Игрок [",str(player_points),"] Бот [",str(bot_points), ']')
            elif (player_cards_sum > 21) and  (bot_cards_sum <= 21):
                bot_points = bot_points + 1
                print("♣ Хах, повезет в питоне ")
                print("Счет Игрок [",str(player_points),"] Бот [",str(bot_points), ']')           
            elif (player_cards_sum < bot_cards_sum):
                bot_points = bot_points + 1
                print("♣ Атятятя Хаха, повезет в питоне ")
                print("Счет Игрок [",str(player_points),"] Бот [",str(bot_points), ']')   
            else:
                player_points = player_points + 1
                print("♣ Фарт - Твоя взяла ")
                print("Счет Игрок [",str(player_points),"] Бот [",str(bot_points), ']')    
            set_off = True     

print("♣ Конец игры ♣")
