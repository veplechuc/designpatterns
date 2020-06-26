from ..absStrategy import AbsStrategy


class UPSStrategy(AbsStrategy):
    def calculate_cost(self, order):
        return 5.0
