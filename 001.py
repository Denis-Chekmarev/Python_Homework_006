# Определить, присутствует ли в заданном списке строк, некоторое число


def is_there(str_list: str, find_number: int) -> bool:
    if len(list(filter(lambda x: str(find_number) in x, str_list))):
        return True
    return False


str_list = ['word', '12', 'toe', 'asdf', '5051 is number', '75']
find_number = 50


print(is_there(str_list, find_number))