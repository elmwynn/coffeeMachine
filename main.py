# a very, very simple first python program to get familiar with syntax
# allows user to purchase coffee with attributes milk, water, coffee, cost
# in exchange for coins


# import dataset
from coffeedata import machine, coffeeType

# set machine variables
machineWater = machine["water"]
machineMilk = machine["milk"]
machineCoffee = machine["coffee"]
machineMoney = machine["money"]
water = 0
milk = 0
coffeeGrounds = 0
coffeeCost = 0
sumChange = 0
# variable to control loop:
continueOn = True

while continueOn:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")
    if userInput == "report":
        print(f"Water: {machineWater} ml")
        print(f"Milk: {machineMilk} ml")
        print(f"Coffee: {machineCoffee} g")
        print(f"Money: ${machineMoney:.2f}")
        continue
    elif userInput == "off":
        # break from loop
        continueOn = False
        break
    elif userInput != "cappuccino" and userInput != "latte" and userInput != "espresso":
        # if user inputs coffee-type or other not in dataset, inform and continue
        print(f"Sorry, we don't have {userInput}! Please pick something else.")
        continue
    else:
        water = coffeeType[userInput]["water"]
        milk = coffeeType[userInput]["milk"]
        coffeeGrounds = coffeeType[userInput]["coffee"]
        coffeeCost = coffeeType[userInput]["cost"]

    # if machine does not have enough materials, restart loop
    if water > machineWater:
        print("Sorry there is not enough water.")
        continue
    if milk > machineMilk:
        print("Sorry there is not enough milk.")
        continue
    if coffeeGrounds > machineCoffee:
        print("Sorry there is not enough coffee.")
        continue

    print(f"The {userInput} will be {coffeeCost: .2f}")
    print("Please insert coins.")
    # get number of quarter, dimes, etc. and multiply by value to get amount
    sumChange = int(input("Number of quarters: ")) * 0.25
    sumChange += int(input("Number of dimes: ")) * 0.10
    sumChange += int(input("Number of nickels: ")) * 0.05
    sumChange += int(input("Number of pennies: ")) * 0.01
    if sumChange < coffeeCost:
        print(f"Sorry. ${sumChange: .2f} is not enough money. Money refunded.")
        continue
    if sumChange > coffeeCost:
        print(f"Thank you for your purchase. Here is your change: ${sumChange - coffeeCost:.2f}")
    print(f"Here is your {userInput}!")
    machineMoney += coffeeCost
    machineWater -= water
    machineMilk -= milk
    machineCoffee -= coffeeGrounds

print("Thanks for using our machine!")
