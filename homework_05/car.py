"""
Создайте класс `Car`, наследник `Vehicle`
"""

"""
Модуль с описанием автомобиля.
"""

from homework_05.base import Vehicle
from homework_05.engine import Engine


class Car(Vehicle):
    # Атрибут двигателя (по умолчанию двигатель отсутствует)
    engine = None

    def set_engine(self, engine: Engine):
        """
        Устанавливает двигатель для автомобиля.
        """

        self.engine = engine