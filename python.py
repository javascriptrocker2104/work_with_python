"""Написать программу, которая удаляет из списка
все элементы, стоящие на четных позициях. """

def delete(num):
    num=num[::2]
    return num
num=[0,1,2,3,5,6,2,3,9]
delete(num)

"""Написать программу, которая считывает список слов
и находит слова, содержащие более трех гласных букв."""

def letters(words):
    vowels=['a','e','i','o','u','y']
    result=[];
    for i in words:
        cnt=0
        for j in i:
            if j in vowels:
                cnt+=1
        if cnt>3:
            result.append(i)
    return result
words=['environment','python','java','developers']
letters(words)

"""Написать программу, которая находит второй по 
величине элемент в списке. """

num=[0,100,456,11,2000009,3,5,6,2,3,9]
num.sort()
print(num)
print(num[1])

"""Написать программу, которая удаляет из списка все дубликаты"""

lst = ['java','java', 'java', 'sql','c++','c++'] 
temp = [] 
for i in lst: 
    if i not in temp: 
        temp.append(i) 
lst = temp 
print(f'Updated List after removing duplicates = {temp}')

"""Написать программу, которая считывает данные из CSV-файла и 
создает словарь, где ключами являются значения в столбце «Name», а значениями
— соответствующие им словари с информацией о поле, возрасте и зарплате. """

import csv
def get_dict(file):
    rows = {}
    with open(file) as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            line = line.split(';')
            rows.update({line[0]: {'GENDER': line[1], 'AGE': line[2], 'SALARY': line[3]}})

    return(rows)

get_dict(r"C:\Users\Анна\Documents\file.csv")

"""Написать программу, которая запрашивает у пользователя строку и выводит на экран 
все ее подстроки длиной не менее трех символов. """

def work_with_str():
    in_str = input('Write some line: ')
    array_of_str = in_str.split()
    new_array = []
    for i in array_of_str:
        if len(i) >= 3:
            new_array.append(i)
    return ' '.join(new_array)

print(work_with_str())