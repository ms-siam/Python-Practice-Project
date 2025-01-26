import pyinputplus as pyip

#Selection Part
print('Welcome , what are your preferences for the Sandwich?')
print('Which type of bread you would like to take?')
breadType = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
print('Which type of Protein you would like to take?')
proteinType = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
needCheese = pyip.inputYesNo(prompt= 'Would you like to add cheese?')
cheeseType = None
if needCheese == 'yes':
    cheeseType = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
needAddOn= pyip.inputYesNo('Would you like to add any add-ons?')
addOnType = []
if needAddOn == 'yes':
    addOnType.append(pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'], numbered=True))
    while True:
        moreAddOn = pyip.inputYesNo('Would you like to add more add-ons?' )
        if moreAddOn == 'yes':
            addOnType.append(pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'], numbered=True))
            continue
        else:
            break
numOfSand = pyip.inputInt('How many Sandwiches you want?', min=1)

#costing Part
SandwichPrice = 0
Pricing = {"Wheat":10, "Sourdough": 6,"Chicken": 5,"Turkey": 7,"Ham": 4,"Tofu": 3,"Cheddar": 1,"Swiss": 2,"Mozzarella": 3,"Mayo": 1,"Mustard": 1,"Lettuce": 1,  "Tomato": 1}
if breadType in Pricing:
    SandwichPrice = SandwichPrice + Pricing[breadType]
if cheeseType in Pricing:
    SandwichPrice = SandwichPrice + Pricing[cheeseType]
for addOns in addOnType:
    if addOns in Pricing:
        SandwichPrice = SandwichPrice + Pricing[addOns]
TotalPrice = numOfSand * SandwichPrice
print(f'The total cost will be {TotalPrice}$')
    

