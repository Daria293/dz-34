
print("напиток, суп, десерт: ")
category = input(":")
match category:
    case "напиток":
        print("чай, кофе, сок : ")
        a = input(":")
        match a:
            case "чай":
                print("150 руб")
            case "кофе":
                print("200 руб")
            case "сок":
                print("100 руб")
            case _:
                print("None")
    case "суп":
        print("борщ, щи, суп-пюре : ")
        b = input(":")
        match b:
            case "суп":
                print("550 руб")
            case "борщ":
                print("650 руб")
            case "щи":
                print("400 руб")
            case "суп-пюре":
                print("625 руб")
            case _:
                print("None")
    case "десерт":
        print("торт, мороженое, фрукты : ")
        c = input(":")
        match c:
            case "торт":
                print("300 руб")
            case "мороженое":
                print("100 руб")
            case "фрукты":
                print("500 руб")
            case _:
                print("None")
    case _:
        print("None")