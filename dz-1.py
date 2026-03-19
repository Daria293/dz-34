name = input("Введите ваше имя: ").capitalize()
age = input("Введите ваш возраст: ")
ages = "error"
if int(age[-1]) == 1 and int(age) != 11:
    ages = "год"
elif int(age) == 10 or int(age) == 11 or int(age) == 12 or int(age) == 13 or int(age) == 14:
    ages = "лет"
elif int(age[-1]) == 2 or int(age[-1]) == 3 or int(age[-1]) == 4:
    ages = "года"
else:
    ages = "лет"
print(f"Привет {name}! Тебе {age} {ages}.")