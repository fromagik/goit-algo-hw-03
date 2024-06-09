import random #Імпортуємо модуль

def get_numbers_ticket(min, max, quantity): #Створення функції
    lottery_numbers = [] #створення списку
    if min < 1 or max > 1000 or quantity > max: #Перевірка обовязковизкових умов 
        return f'Invalid parametres'

    while quantity != 0: # Цикл поки довжина списку не буде рівна заданому параметру кількості
        random_num = random.randint(min, max) # Генерація випадкових чисел
        if random_num not in lottery_numbers: # Переверка чисел на унікальність
            lottery_numbers.append(random_num) 
            quantity -= 1
    
    return sorted(lottery_numbers) # Повертаємо відсортований список лотарейних чисел



