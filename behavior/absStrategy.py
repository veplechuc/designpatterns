from abc import ABCMeta, abstractmethod


class AbsStrategy(metaclass=ABCMeta):
    @abstractmethod
    def calculate_cost(self, order):
        "calculate order cost based on strategy"
