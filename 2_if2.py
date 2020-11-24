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


def answer(word1, word2):
    if type(word1) is not str or type(word2) is not str:
        return 0
    
    elif word2 == 'learn' and word1 != 'learn':
        return 3
    elif len(word1) > len(word2):
        return 2
    elif word1 == word2:
        return 1
    else:
        return "попробуй по-другому"
    




def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(answer('1' , 1))
    print(answer('1' , '1'))
    print(answer('11' , '1'))
    print(answer('1' , 'learn'))
    print(answer('nojlfvffhh,',"learn"))
    print(answer('learn,',"learn"))
    print(answer('learn' , 'learning'))
    print(answer('python' , 'python'))

if __name__ == "__main__":
    main()