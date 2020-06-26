from ..absStrategy import AbsStrategy

class FedexStrategy(AbsStrategy):

    def calculate_cost(self, order):
        return 3.0