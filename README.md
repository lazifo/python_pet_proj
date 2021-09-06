## Описание

Алгоритм реализует консольную игру в "21",  с некоторыми отклонениями от правил игры.

## Функционал
В консоле игроку предлагается сыграть против бота, можно выбрать взять карту или отказаться. 
Можно видеть кол-во очков игрока и бота, а также те карты что пришли игроку. 
Реализован подсчет очков за выигранные партии

## Реализация
Для перемешивания колоды, сначала создается список списков и 36 карт колоды вида [масть кол-во очков]. 
Затем создается список с числами\номерами карты от 1 до 36, далее этот список перемешивается, и по инкременту счетчика последовательно выбирается значение индекса которое будет соответствовать карте из список списков.
           
$ player_cards_list.append(s_cards_list[deck_cards_nums[card_num]])
$ card_num = card_num + 1 

Далее происходит сортировка списка карты игрока\бота где извлекатся значения для подсчета очков и показа в консоле

$ cards_digit = [el[1] for el in player_cards_list[0:len(player_cards_list)]]  
$ cards_names = [el[0] for el in player_cards_list[0:len(player_cards_list)]] 