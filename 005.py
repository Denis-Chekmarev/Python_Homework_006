# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

origin_list = [2, 4, 3, 5, 4, 9, 10]
new_list = [origin_list[i] * origin_list[-i - 1] for i in range(int(len(origin_list)/2))]
print(new_list)