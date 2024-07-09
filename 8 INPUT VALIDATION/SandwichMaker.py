import pyinputplus as pyip

# Prices for sandwich options
prices = {'bread' : {'wheat' : 1, 'white' : 2, 'sourdough' : 3},
          'protein' : {'chicken' : 5, 'turkey' : 7, 'ham' : 10, 'tofu' : 2},
          'cheese' : {'cheddar' : 5, 'Swiss' : 6, 'mozzarella' : 7},
          'extras' : {'mayo' : 1, 'mustard' : 2, 'lettuce' : 3, 'tomato' : 4},
          }

# Get user's sandwich preferences
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Choose a bread type: \n")
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choose a bread type: \n")
cheeseOrNot = pyip.inputYesNo("Do you want cheese?")
if cheeseOrNot == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
extrasOrNot = pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato?")
if extrasOrNot == 'yes':
    extrasList = []
    for extra in prices['extras'].keys():
        if pyip.inputYesNo(f'Do you want {extra}?') == 'yes':
            extrasList.append(extra)        
numofSandwiches = pyip.inputInt("How many sandwiches do you want?", min=1)

# Print the prices
print(f'{bread}'.ljust(10), f'{prices["bread"][bread]}')
print(f'{protein}'.ljust(10), f'{prices["protein"][protein]}')
price = prices["bread"][bread] + prices["protein"][protein]
if cheeseOrNot == 'yes':
    print(f'{cheese}'.ljust(10), f'{prices["cheese"][cheese]}')
    price += prices["cheese"][cheese]
if extrasOrNot == 'yes':
    for extra in extrasList:
        print(f'{extra}'.ljust(10), f'{prices["extras"][extra]}')
        price += prices["extras"][extra]
print('Price'.ljust(10), f'{price}')
print('Num'.ljust(10), f'{numofSandwiches}')
print('Total'.ljust(10), f'{numofSandwiches * price}')