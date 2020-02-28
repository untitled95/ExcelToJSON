import pandas,json


print("please drag your file here") 
input1 = input()

data = pandas.read_excel(input1, skiprows = 54, keep_default_na = False, usecols = ['Description', 'Additional Instructions'])

tempCategories = data.iloc[:,0]
tempDescriptions = data.iloc[:,1]

categories = []
descriptions = []
finalResult = []

for i in tempCategories:
    categories.append(i)
    if i == '':
        break

for i in tempDescriptions:
    descriptions.append(i)
    if i == '':
        break

for i in range(len(categories)-1):
    finalResult.append({
        "category": categories[i],
                "bids": [{
                    "item": 1,
                    "description": descriptions[i],
                    "qty": 1,
                    "unit": "EA",
                    "price": "",
                    "cost": "",
                    "comments": []
                }],
    })


y = json.dumps(finalResult)

print (y)  
