class ErrorIdLike(Exception):
    def __init__(self, txt):
        self.txt = txt


def joy_division():
    try:
        divisible = int(input('Введите число, которое хотите разделить: '))
        divisor = int(input('Введите число на которое делите: '))
        if divisor == 0:
            raise ErrorIdLike("О, нет! Вы поделили на ноль...")
        else:
            result = divisible / divisor
            return result
    except ValueError:
        return "Введенное вами значение не является числом."
    except ErrorIdLike as error:
        return error


print(joy_division())
