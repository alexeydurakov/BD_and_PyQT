import logging
logger = logging.getLogger('server')


# Дескриптор для описания порта:
class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            exit(1)
        # Если порт прошел проверку, добавляем его в список атрибутов экземпляра
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Host():
    def __set__(self, instance, value):
        if not isinstance(value,int):
            logger.critical(
                f'Тип данные не верен {value} введены тип данных {type(value)}')
            exit(1)
        else:
            if value <= 0:
                logger.critical(
                    f'Ваш порт не может быть 0 или меньщь 0')
                exit(1)

        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name