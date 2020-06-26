from ..absStrategy import AbsStrategy


class PostalServiceStrategy(AbsStrategy):
    def calculate_cost(self, order):
        return 8
