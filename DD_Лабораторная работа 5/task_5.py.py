# TODO написать функцию генерации случайных паролей
import random
import string

def get_random_password(n=8) -> str:
    if not isinstance(n, int):
        raise TypeError(f"У переменной n должен быть тип int, а не {type(n)}.")
    if not n > 0:
        raise ValueError("Количество символов должно быть больше 0")
    list_digits = string.ascii_uppercase + string.ascii_lowercase + string.digits
    list_password = random.sample(list_digits, n)
    password = "".join(list_password)
    return password

print(get_random_password())
