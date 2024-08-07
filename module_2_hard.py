def generate_password(n):
    result = ""

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum_pair = i + j

            if sum_pair != 0 and n % sum_pair == 0:
                result += f"{i}{j}"
    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print("Подбор пароля:", password)
else:
    print("Число не подходит")
