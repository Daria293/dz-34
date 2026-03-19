shopping = [1250, 2540, 3300, 10000, 1550, 2850, 3350]
total = float(sum(shopping))
minimum = float(min(shopping))
maximum = float(max(shopping))
middle = total/2
info = minimum, maximum, middle
print(tuple(info))