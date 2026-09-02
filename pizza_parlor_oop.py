class PizzaParlor:

    def __init__(self, topping_count, price):
        self.topping_count = topping_count
        self.price = price

    def pizza_info(self):
        print("Topping count: ", self.topping_count)
        print("Total price: ", self.price)

    def total_price(self):
        if self.topping_count > 0:
            print(10.00)

pizza1 = PizzaParlor(3, 14.50)
pizza2 = PizzaParlor(2, 13.00)

pizza1.pizza_info()
print("_______________________")
pizza2.pizza_info()


    



        
