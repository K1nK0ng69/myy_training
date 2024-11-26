def apply_all_func(int_list, *functions):
    # Создаем пустой словарь для результатов
    results = {}
    # Перебираем все переданные функции
    for func in functions:
        # Вызываем функцию с переданным списком и записываем результат в словарь
        results[func.__name__] = func(int_list)
    # Возвращаем словарь с результатами
    return results

# Пример вызова функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
