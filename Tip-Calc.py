# Day 2 - Jun 7 '24
# Tip Calucator

print("Welcome to the tip calculator!")

billTotal = float(input("What was the total bill? "))

tipPercent = int(input("How much tip would you like to give? 10, 12, or 15? "))

numOfPeople = int(input("How many people to split the bill? "))

totalWithTip = billTotal + (billTotal * tipPercent / 100)

finalAmount = round(totalWithTip / numOfPeople, 2)

finalAmount = "{:.2f}".format(finalAmount)

print(f"Each person should pay: ${finalAmount}")