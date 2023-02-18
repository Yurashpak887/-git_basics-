import random


ranks = ["J", "K", "Q", "A", 5, 6, 7, 8, 9]
suits = ['\u2660',
         '\u2665',
         '\u2666',
         '\u2663']

class CardGame01():
    def __init__(self):
        self.rankss=random.choice(ranks)
        self.suitss=random.choice(suits)

    def __repr__(self):
        return f'{self.rankss}{self.suitss}'

    def fortune():
        yourcard=CardGame01()


        yourquestion=input("Що ти хочеш дізнатись?")

        if yourcard.rankss==("A") or yourcard.rankss ==("Q") and yourcard.suitss=={'\u2660'} or yourcard.rankss =={'\u2663'}:
            print(f"Випала карта {yourcard.__repr__()} Значить Так, це неодмінно збудеться!")
        elif yourcard.rankss==(9) or yourcard.rankss ==("K") and yourcard.suitss=={'\u2666'} or yourcard.rankss =={'\u2665'}:
            print(f"Випала карта {yourcard.__repr__()} Найбільш можливо, все буде добре!")
        elif yourcard.rankss == (5) or yourcard.rankss == (6) and yourcard.suitss == {'\u2666'} or yourcard.rankss == {'\u2663'}:
            print(f"Випала карта {yourcard.__repr__()} Я бачу негаразди на твоєму шляху, проте результат буде хороший!")
        else:
            print("Вибач, але тебе чекає невдача!")

if __name__ == '__main__':
    CardGame01()
