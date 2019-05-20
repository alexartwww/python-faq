"""
Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
Напишите функцию, которая создаёт из этих ключей и значений словарь.
Если ключу не хватило значения, в словаре должно быть значение None.
Значения, которым не хватило ключей, нужно игнорировать.
Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml
"""

a = [1, 2, 3, 4, 5, 8, 56, 67, 78, 89]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(dict(zip(a, b) if len(a) <= len(b) else zip(a, b + [None for _ in range(len(a) - len(b))])))
