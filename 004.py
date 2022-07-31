# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def get_second_include(text: str, search_text: str) -> int:
    count = 0
    for index, elem in enumerate(text):
        if search_text == elem:
            count += 1
            if count == 2:
                return index
    return -1


input_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(get_second_include(input_list, 'йцу'))