"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    hello = ""
    while hello.lower().capitalize() != 'Хорошо':
        hello = input('Как дела?  ') 
              
    print('Ну и славненько')

if __name__ == "__main__":
    hello_user()
