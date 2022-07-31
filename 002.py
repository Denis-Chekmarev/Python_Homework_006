# Найти сумму чисел списка стоящих на нечетной позиции


def get_sum(input_list: list) -> int:
    return sum([input_list[i] for i in range(len(input_list)) if i % 2 != 0])


input_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(get_sum(input_list))