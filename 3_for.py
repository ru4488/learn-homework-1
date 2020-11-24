"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
#     """
#     Эта функция вызывается автоматически при запуске скрипта в консоли
#     В ней надо заменить pass на ваш код
#     """
#     pass
      # ten = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 78 , 13 , 11]
      # for numb in ten:
      #     print(numb + 1)
      #  1315
      # for letter in "слон":'22'
      #     print(letter)
      
      school = [
        {'school_class': '1a', 'score' :[1 , 5 , 2 , 2, 3]},
        {'school_class': '1б', 'score' : [3 , 3, 3 , 3, 3]}, 
        {'school_class': '1в', 'score' : [5 , 4 , 5 , 4 , 4]},   
         ]
      # for middle in school['score']:
      #     print(middle)
      total = 0
      point = 0
      allschool = 0
      for score in range(len(school)):
          
          
          total += sum(school[score]['score'])/len(school[score]['score'])
          allschool += sum(school[score]['score'])
          point += len(school[score]['score'])
          middle_class  = total 
          classroom = {school[score]['school_class']}
          print(f'среднийй бал класса  {classroom} - {middle_class} балла')
          total = 0
      print(f'средний бал в вашей школе {round(allschool/point , 1)}')
      print('так себе')


if __name__ == "__main__":
    main()
