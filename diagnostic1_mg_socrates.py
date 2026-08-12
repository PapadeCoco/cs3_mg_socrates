#Intergalactic Weight Calculator

def calculate_space_weight(earth_weight, destination):
    if destination == "Mars":
        return earth_weight*0.38
    elif destination == "Jupiter":
        return earth_weight*2.34
    elif destination == "Moon":
        return earth_weight*0.16
    else:
        print("Input a valid planet/moon")

def main(earth_weight, destination):

    earth_weight = int(input("Enter your weight on Earth in kg: "))
    destination = input("Enter the destination (Mars, Jupiter, Moon): ")
    weight_planet = calculate_space_weight(earth_weight, destination)
    print(f"Your weight on {destination} would be: {weight_planet} kg")

main(earth_weight=0, destination="")