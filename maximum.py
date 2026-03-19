first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
third_number = input("Введите третье число: ")
if float(first_number) >= float(second_number) and float(first_number) >= float(third_number):
    print("Максимальное число: ", float(first_number))
elif float(second_number) >= float(first_number) and float(second_number) >= float(third_number):
    print("Максимальное число: ", float(second_number))
else:
    print("Максимальное число: ", float(third_number))