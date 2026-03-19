word = input("Введите слово для проверки: ")
usual_word = list(word[:].lower())
convert_word = list(word[::-1].lower())
if str(usual_word) == str(convert_word):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
