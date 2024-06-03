# Topic: The while Loop (Condition-Controlled)
count = 1
while count<= 5:
    print(f"Counting...{count}")
count+= 1 #Increment count

# Topic: The for Loop (Condition-Controlled)
continents = str(input("enter the name of the continent:"))
continents = ["North_America", "South_America", "Asia", "Australia", "Europe", "Africa", "Antartica"]
for continent in continents:
    print(f"I care about{continents}!")


# Topic: The for Loop (Condition-Controlled)
continents = str(input("enter the name of the continent:"))
continents = ["North_America", "South_America", "Asia", "Australia", "Europe", "Africa", "Antartica"]
imfromconts = ["Asia"]
for continent in continents:
    print(f"Im from{imfromconts}")

# Topic: Calculating a Running Total
total = 0 # assigned the total 0
for num in range(1, 6): # Loop through numbers 1 to 5
    total += num
    print(f"Currnet total: {total}") 

# Topic: Sentinels ( Loop Termination with a Specific Value)
number = 0
while number != -1: # loop until user enter -1 #while loop so it continues until -1
    number = int(input("Enter a number(or -1 to quit): "))
 # input statements that leads to value for variable number
    if number-1:
        print(f"you entered:{number}")
