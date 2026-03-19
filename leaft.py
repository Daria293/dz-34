floor_number = int(input("Введите номер этажа: "))
if floor_number == -1:
    print("Подвал: здесь находится склад")
elif floor_number == 1:
    print("Холл и ресепшен")
elif floor_number == 10:
    print("Технический этаж, вход запрещен")
elif floor_number % 2 == 0 and floor_number <= 10 and floor_number != 0:
    print("Жилой этаж")
elif floor_number % 2 == 1 and floor_number <= 10:
    print("Офисный этаж")
else:
    print("Некорректный номер этажа")