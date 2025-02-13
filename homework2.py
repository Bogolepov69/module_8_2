def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_numbers, incorrect_data = personal_sum(numbers)

        if not sum_numbers:
            raise ZeroDivisionError

        return sum_numbers / (len(numbers) - incorrect_data)

    except TypeError:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')