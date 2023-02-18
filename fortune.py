from cards11 import CardGame01 as game


def lets_play():
    print(f"Привіт! Хочеш дізнатись відповідь на своє запитання?")
    answer=input("Введіть, 'Так', або 'Ні'")

    while True:
        if answer == "Так":
            return game.fortune()
        elif answer == "Ні":
            break
        else:
            answer = input("Введіть або 'Так', або 'Ні'")


lets_play()
