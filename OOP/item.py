class Item:

    pay_rate = 0.8 # 20% discount

    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, f"price cannot be less than 0"
        assert quantity >= 0, f"quantity cannot be less than 0"

        # encapsulation
        self.__name = name
        self.__price = price
        self.quantity = quantity

    # getters
    @property
    def name(self):
        return self.__name

    # setters
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        self.__name = value

    # getters
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price += (self.__price * increment_value)

    def calculate_discount(self):
        return self.price * self.quantity

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.name} {self.quantity} times. 
        Regards, Test User
        """

    def __send(self):
        print("sending email")

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()

    def __repr__(self):
        return f"Item({self.name!r}, {self.price}, {self.quantity})"


# if __name__ == "__main__":
#     item1 = Item("pen", 1000, 20)
#     item1.pay_rate = 0.75
#     print(item1.calculate_discount())
#     print(item1)
#     item1.apply_discount()
#     print(item1)
#     item1.apply_increment(0.2)
#     print(item1)