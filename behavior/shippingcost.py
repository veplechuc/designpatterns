class ShippingCost(object):
    def __init__(self, strategy):
        super().__init__()
        self._strategy = strategy

    def shipping_cost(self, order):
        return self._strategy.calculate_cost(order)
