from base.order import Order
from behavior.shippingcost import ShippingCost
from behavior.types import fedex, postal

order = Order()

strategy = fedex.FedexStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)

print(f"cost for Fedex strategy {cost}")
assert cost == 3.0


strategy = postal.PostalServiceStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
print(f"cost for Postal strategy {cost}")
assert cost == 8

print("all ok")
