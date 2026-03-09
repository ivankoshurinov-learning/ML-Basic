"""
Создайте dataclass `Engine`
"""

"""
Датакласс описание двигателя транспортного средства.
"""

from dataclasses import dataclass

@dataclass
class Engine:
    """
    Класс двигателя и его атрибуты:

    volume — рабочий объём двигателя
    pistons — количество цилиндров
    """

    volume: int
    pistons: int