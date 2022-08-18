#Find what grade you need for a final

current = float(input("What is your current grade? (Ex. 92.4)"))
want = float(input("What grade do yuo want? (Ex. 90)"))
worth = float(input("What percent is your final worth? (Ex. 10)"))

#convert worth percentage
worth = worth/100

#calculate final required
required = round((want-current * (1-worth)) / worth, 1)

print(" You need a " + str(required) + " to get a " + str(want) + "% in this class")
