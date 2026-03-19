food = float(input("Введите траты на еду: "))
transport = float(input("Введите траты на транспорт: "))
discovery = float(input("Введите траты на развлечения: "))
total = food + transport + discovery
middle = total / 2
print(f"Ваши общие траты: {total:.2f}\n"
      f"В среднем вы тратите: {middle:.2f}")


price = float(input("Введите цену товара: "))
discount = float(input("Введите процент скидки: "))
price_with_discount = price - price/100*discount
print(f"Цена товара со скидкой {price_with_discount:.2f}")