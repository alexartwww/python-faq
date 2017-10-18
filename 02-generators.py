def my_range(n, step = 1):
    i = 0
    while True:
        if i < n:
            yield i
            i += step
        else:
            break


def read_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file_descriptor:
        for line in file_descriptor:
            yield line
    file_descriptor.close()

if __name__ == '__main__':

    for i in my_range(10,2):
        print(i)

    for data in read_file('text.txt'):
        print(data)
