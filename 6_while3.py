name = ['Дима' , 'Костя' , 'Валера' , 'Антон']
name1 = ['Дима' , 'Костя' , 'Валера' , 'Антон']
def ask_user(name):
    
    Valera = ''
    while Valera != "Валера":
        
        Valera = name.pop()
        
    print(Valera , "настало твое время")


def find_pesone(name1):
    how_mach = len(name1)
    point = 0
    print('Кого ищем?')
    while point < how_mach:
        
        print(f'{name1[point]}?')
        point += 1

if __name__ == "__main__":
    ask_user(name)
    find_pesone(name1)
