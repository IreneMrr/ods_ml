import json
import re


def task1():
    """
    Написать код, который вычисляет сумму всех чисел, удовлетворяющих следующие условия:
    положительные целые числа от 1 до 1_000_000_002 (один миллиард два) включительно
    которые нацело (без остатка) делятся на 3 (пример: 3, 6, 9, ...)
    и которые не заканчиваются на 4 и 7 (пример заканчивающихся на 4 и 7: 24, 27, 54, 57 ...)
    """
    a = 0
    for i in range(3, 1000000003, 3):
        if i % 10 != 4 and i % 10 != 7:
            a = a + i
    print(a)


def task2():
    """
    На вход поступает текстовый файл из 3-х тысяч строк
    Нужно подготовить текстовый файл из 1 строки.
    Строка содержит набор из 3-х тысяч чисел, разделенных запятой.
    После последнего числа запятая не ставится.
    каждое число - результат операции:
    "результирующее целое число" = "целое число #1" применить "арифметическая операция" "целое число #2"
    """
    new = []
    with open('input_file.txt', 'r') as f:
        for line in f:
            line = line.split()
            if line[0] == '+':
                new.append(str(int(line[1]) + int(line[2])))
            elif line[0] == '-':
                new.append(str(int(line[1]) - int(line[2])))
            elif line[0] == '*':
                new.append(str(int(line[1]) * int(line[2])))
            elif line[0] == '//':
                new.append(str(int(line[1]) // int(line[2])))
            elif line[0] == '%':
                new.append(str(int(line[1]) % int(line[2])))
            elif line[0] == '**':
                new.append(str(int(line[1]) ** int(line[2])))
    new = ",".join(new)
    print(new)


def task3():
    """
    На вход поступает два текстовый файл из 3-х тысяч строк каждый.
    Первый файл содержит строки текста.
    Второй файл содержит строки из двух целых неотрицательных чисел.
    Первое число в строке всегда меньше или равно второму.
    Числа всегда меньше длины соответствующей строки первого файла.
    Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла,
    а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.
    Подготовить выходной файл, который состоит из подстрок 1-го входного файла.
    Подстроки разделены пробелами.
    Какие брать подстроки - написано во втором файле.
    :return:
    """
    third = []
    with open('import_file_2_1.txt', 'r') as first, open('import_file_2_2.txt', 'r') as second:
        for line_1, line_2 in zip(first, second):
            line_2 = line_2.split()
            third.append(line_1[int(line_2[0]):int(line_2[1]) + 1])
    third = (" ".join(third))
    print(third)


def task4():
    """
    На вход поступает строка.
    В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов.
    Нужно расшифровать химические символы в название химических элементов.
    :return:
    """
    with open('import_file_3.txt', 'r') as start_file:
        element_name = start_file.read()
    element_name = re.sub(r'([A-Z])', r' \1', element_name).split()

    with open('periodic_table.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)

    element_rus = []
    for i in element_name:
        element_rus.append(data[i])

    element_rus = ''.join(element_rus)
    print(element_rus)

