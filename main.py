import random
# Генерация списка из 25 случайных целых чисел в диапазоне от -50 до 50
a = [random.randint(-50, 50) for i in range(25)]
# Вывод списка
print(a)
# Нахождение и вывод минимального значения в списке
print("Минимальное значение", min(a))
# Нахождение и вывод максимального значения в списке
print("Максимальное значение", max(a))
# Инициализация счетчиков для положительных, отрицательных и нулевых элементов
count_positive = 0
count_negative = 0
count_zero = 0
# Инициализация переменных для хранения процентов
procent_positive = 0
procent_negative = 0
procent_zero = 0
# Перебор всех элементов списка
for i in a:
    if i > 0:
        # Если элемент положительный, увеличиваем соответствующий счетчик
        count_positive += 1
        # Вычисляем процент положительных элементов
        procent_positive = count_positive / 25 * 100
    elif i < 0:
        # Если элемент отрицательный, увеличиваем соответствующий счетчик
        count_negative += 1
        # Вычисляем процент отрицательных элементов
        procent_negative = count_negative / 25 * 100
    else:
        # Если элемент равен нулю, увеличиваем соответствующий счетчик
        count_zero += 1
        # Вычисляем процент нулевых элементов
        procent_zero = count_zero / 25 * 100
# Вывод количества и процентов положительных элементов
print("Количество положительных элементов: ", count_positive, "Их процент составляет: ", procent_positive)
# Вывод количества и процентов отрицательных элементов
print("Количество отрицательных элементов: ", count_negative, "Их процент составляет: ", procent_negative)
# Вывод количества и процентов нулевых элементов
print("Количество нулевых элементов: ", count_zero, "Их процент составляет: ", procent_zero)