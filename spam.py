messages  = [
    "Привет!",
    "Купи дешевые курсы!!!",
    "Как дела?",
    "СПАМ реклама!!!",
    "Пойдем играть в футбол?"
]
for message in messages:
    if "СПАМ" in message:
        print("Найден СПАМ")
        break
    if len(message) > 20:
        continue
    print(message)
else:
    print("Проверка завершена, СПАМ не найден")


       
        