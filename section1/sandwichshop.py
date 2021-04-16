# Todo : push changes to remote repo


def markup(cost, mark=1.10):
    return cost * mark


def discount(cost, coupon=0.10):
    return cost - (cost * coupon)


print(markup(100))
print(discount(100))
