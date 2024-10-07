def generate_password(n):
    password = ""

    for i in range(1, n // 2 + 1):
        j = n - i
        if i < j:
            pair_sum = i + j
            if n % pair_sum == 0:
                password += str(i) + str(j)

    return password

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_password(n)
    print("Нужный пароль:", result)
else:
    print("Число должно быть в диапазоне от 3 до 20.")
