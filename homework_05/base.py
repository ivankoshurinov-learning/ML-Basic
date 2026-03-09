"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    # Задаем нулевые значения по умолчанию
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        """
        Вызывается при создании экземпляра класса транспортного средства.
        weight: вес транспортного средства
        fuel: количество топлива в баке
        fuel_consumption: расход топлива
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

        # При создании экземпляра транспортного средства оно не заведено
        self.started = False

    def start(self):
        """
        Процедура запуска транспортного средства.

        Если транспорт не запущен:
        - проверяем, есть ли топливо
        - если топливо есть — меняем состояние started на True
        - если топлива нет — выкидываем исключение LowFuelError
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Мало топлива, не можем запустить транспортное средство")

    def move(self, distance):
        """
        Перемещение транспортного средства на distance - расстояние, которое нужно проехать
        """

        # Считаем, сколько топлива потребуется для поездки
        required_fuel = distance * self.fuel_consumption

        # Проверяем, хватает ли топлива в баке
        if required_fuel <= self.fuel:
            # Если топлива в баке достаточно — уменьшаем его количество на то, что потратили
            self.fuel -= required_fuel
        else:
            # Если топлива недостаточно — выбрасываем исключение
            raise NotEnoughFuel("Недостаточно топлива для совершение поездки")