from datetime import datetime #Імпориуємо моду 

def get_days_from_today(date): #Створюємо функцію
    while True:
        try: #Обробка винятків 
            user_date = datetime.strptime(date, '%Y-%m-%d') #Переводимо отриману дату в фотмат дати 
            currant_date = datetime.today() # Отримуємо теперішьню дату
            difference_date = currant_date - user_date # Розраховуємо різницю
            print(f"Різниця між вказаною датою {user_date.date()} та сьогодні {currant_date.date()} складає {difference_date.days} днів" )
            break # Завершення циклу
        except ValueError: # Обробка винятку
            print("Невірно введена дата. Спробуйте ще раз, та пам'ятайте про формат РРРР-ММ-ДД")
            date = input('Введіть дату в форматі РРРР-ММ-ДД: ')
        
date = input('Введіть дату в форматі РРРР-ММ-ДД: ') 
get_days_from_today(date) # Виклик функції 