print('\033[30m\033[47mДомашнее задание по теме "Генераторы"\033[0m')
print('\033[30m\033[47mЦель: более глубоко понять особенности работы с функциями генераторами и оператором '
      'yield в Python.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


def all_variants(text):
    x = len(text)
    for g in range(x):
        yield text[g]

    for j in range(2, x + 1):
        for y in range(x - j + 1):
            z = y + j
            yield text[y:z]


# Пример результата выполнения программы: Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
print()
print(thanks)
