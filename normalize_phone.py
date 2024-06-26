def normalize_num(phone_number): #Створення функції
    clean_number = '+38' # Створення очищеного номеру, починаючи з префіксу
    phone_number = phone_number.strip() # Метод для видалення табуляції 
    if phone_number.startswith("+38"): # видалення "префіксу" в номерах
        phone_number = phone_number.replace("+38", "")
    elif phone_number.startswith("38"):
        phone_number = phone_number.replace("38", "")

    for num in phone_number: # Перебір символів в номері
        if num.isdigit(): # Метод для посторонніх символів якщо це не цифра
                clean_number += num # Додаємо цифру до номеру 
    return clean_number # Повернення чистого номеру

assert(normalize_num('    0502312343')) == "+380502312343"
assert(normalize_num("38(050)123412      ")) == '+38050123412'
assert(normalize_num("    +380758021503    ")) == '+380758021503'