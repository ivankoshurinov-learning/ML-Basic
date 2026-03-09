"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class UserException(Exception):
    """
    Базовый класс для всех пользовательских исключений, как рекомедовано на лекции.
    """
    pass


class LowFuelError(UserException):
    """
    Исключение по предупреждению малого остатка топлива в баке для запуска
    """
    pass


class NotEnoughFuel(UserException):
    """
    Исключение по ошибке недостаточного количества топлива для поездки
    """
    pass


class CargoOverload(UserException):
    """
    Исключение по ошибке превышения предельной массы груза
    """
    pass
