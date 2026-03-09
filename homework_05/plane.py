"""
Создайте класс `Plane`, наследник `Vehicle`
"""

"""
Описание самолета.
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    # Текущий груз равен нулю
    cargo = 0

    # Максимальная грузоподъемность
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        """
        Инициализация самолета.

        :param weight: вес самолета
        :param fuel: количество топлива
        :param fuel_consumption: расход топлива
        :param max_cargo: максимальная грузоподъемность
        """

        super().__init__(weight, fuel, fuel_consumption)

        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
        """
        Загружаем груз в самолет, cargo - количество добавляемого груза
        """

        # Проверяем на перегруз
        if self.cargo + cargo > self.max_cargo:
            raise CargoOverload

        # Если перегруза нет — увеличиваем текущий груз на дополнительно загруженный
        self.cargo += cargo

    def remove_all_cargo(self):
        """
        Удаляем весь груз из самолета
        """

        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo