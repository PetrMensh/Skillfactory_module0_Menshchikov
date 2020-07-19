#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # Предполагаемое число
        if number == predict: 
            return(count) # Выход из цикла, если угадали
        
def game_core_v3(number):
    '''Каждый раз в качестве предполагаемого числа берем число из середины списка 
       возможных чисел, который определяется на каждом этапе итеррации сравнением с
       загаданным числом. 
       
       Таким образом на каждом этапе итерации количество 
       предполагаемых значений сокращается в 2 раза. Максимальное значение шагов 
       итераций n = 7 (2**7 = 128 > 100)'''
    
    count = 1
    prediction_list = [x for x in range(1,101)] # Список возможных чисел  
    predict_index = int(len(prediction_list)/2) #Индекс предполагаемого числа
    predict_value = prediction_list[predict_index] # Предполагаемое число
    
    while number != predict_value:
        count+=1
        if number > predict_value: 
            prediction_list = prediction_list[predict_index:]
            predict_index = int(len(prediction_list)/2)
            predict_value = prediction_list[predict_index]
            
        elif number < predict_value: 
            prediction_list = prediction_list[:predict_index]
            predict_index = int(len(prediction_list)/2)
            predict_value = prediction_list[predict_index]          
            
    return(count) # Выход из цикла, если угадали
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    
    score = int(np.mean(count_ls)) #среднее число попыток
    max_predictions = max(count_ls) #максимальное число попыток
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    print(f"Максимальное число попыток - {max_predictions}")
    
    return(score, max_predictions)

(score, max_predictions) = score_game(game_core_v3)


# In[ ]:




