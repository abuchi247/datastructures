from item import Item

item1 = Item("pen", 1000, 20)
item1.pay_rate = 0.75
print(item1.calculate_discount())
print(item1)
item1.apply_discount()
print(item1)
item1.apply_increment(0.2)
print(item1)

item1.send_email()