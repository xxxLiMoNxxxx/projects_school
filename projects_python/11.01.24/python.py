while(True):
    banned_words = ["лайно", "кретин", "дегенерат", "мудак", "жид", "залупа", "тупий", "гидота", "гнида", "срань"]
    nickname = input("Реєстрація \n Введіть свій нікнейм: ")
    password = input("Реєстрація \n Введіть свій пароль: ")
    while(True):
        while(True):
            comment = input("ЧІНАЗЕС \n Введіть повідомлення для чата: ")
            for word in banned_words:
                if word.lower() in comment.lower():
                    comment = comment.replace(word, "*цензура*")
            else:
                print(f"{nickname}: {comment}")
                break