"""
from datetime import datetime
time = datetime.now()
print(time)

import json
x = '{ "name":"Alex", "age":20, "city":"Falesti" }'
y = json.loads(x)
print(y[input()])

print(json.dumps({"name":"John", "age":30}))
print(json.dumps(["Hello"]))
print(json.dumps(42))
print(json.dumps(True))
"""

from Classika import Student

print("Выберите меню:")
print("1. Добавить имя студента")
print("2. Изменить оценку")

n = int(input())

if n == 1:
    name = input("Введите имя: ")
    s1 = Student(name)
    print(s1.name)

