"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def word(old_word1, old_word2):
    old_word1 = input("первое слов: ")
    old_word2 = input("второе слово: ")
    return old_word1, old_word2

def answer(word1, word2):
    if word2 == 'learn' and len(word1) < len(word2) and len(word1) != len(word2) :
        return 3
    elif len(word1) > len(word2):
        return 2
    elif word1 == word2:
        return 1
    elif type(word1) is str and type(word2) is str:
        return 0


old_word1 = ''
old_word2 = ''
word1, word2 = word(old_word1, old_word2)
print(answer(word1, word2))


word1, word2 = word(old_word1, old_word2)
print(answer(word1, word2))

word1, word2 = word(old_word1, old_word2)
print(answer(word1, word2))

word1, word2 = word(old_word1, old_word2)
print(answer(word1, word2))
