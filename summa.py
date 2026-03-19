user_list = input("Введите числа через запятую: ").split(",")
first, *rest, last = user_list
sum1 = int(first) + int(last)
sum2 = sum(map(int, rest))
print(sum1, sum2)
