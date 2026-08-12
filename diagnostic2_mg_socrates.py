#Pizza Parlor

plain_pizza = 10.00
topping = 1.50
topping_choice = ["pepporoni", "mushrooms", "extra cheese"]
discount = "PYTHON20"

def calculate_total(topping_count):
    return plain_pizza + (topping * topping_count)

def main():

    while True:
        print (input("What topping would you like to add? from the menu (pepporoni, mushroom, extra cheese): "))

        if input not in topping_choice:
            return "Not in Menu"
        else:
            break

main()

                  