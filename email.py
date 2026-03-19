email = str(input("Введите ваш емайл: "))
if email.count("@") != 1:
    print("Адрес должен содержать одну \"@\"")
    exit()
if not "." in email:
    print("Адрес должен содержать точку")
    exit()
if not email.endswith("ru"):
    print("Адрес должен содержать \"ru\"")
    exit()
user, domain = email.split("@")
if len(user) == 0:
    print("Некорректный адрес почты")
    exit()
domain2, other = domain.split(".")
if len(domain2) == 0:
    print("Некорректный адрес домена")
    exit()
else:
    print("Адрес принят")

