

with open('text.txt', 'r', encoding='utf-8') as file_descriptor:
    for line in file_descriptor:
        print(line)


class Hello:
    def __enter__(self):
        print('вход в блок')

    def __exit__(self, exp_type, exp_value, traceback):
        print('выход из блока')

    def __del__(self):
        print('деструктор')


with Hello():
     print('мой код')

'''
вход в блок
мой код
выход из блока
деструктор
'''

import contextlib
@contextlib.contextmanager
def context():
    print('вход в блок')
    try:
        yield {}
    except RuntimeError as err:
        print('error: ', err)
    finally:
        print('выход из блока')
'''
вход в блок
блок
выход из блока
'''

# nested

first, second = context(), context()
with first as first:
    with second as second:
        print('внутри блока')

