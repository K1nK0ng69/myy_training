first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для вычисления разницы длин, если длины строк не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Пример вывода результатов
print(list(first_result))  # Генератор разворачивается в список для просмотра результата
print(list(second_result))
