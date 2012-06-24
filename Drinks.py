###
print ("------------------a---------------------------")

groceries = ['banana','strawberries','apples','bread']
groceries.append('champagne')
print groceries






print ("-------------------b--------------------------")




groceries = ['banana','strawberries','apples','bread']

del groceries [3]

print groceries




print ("------------------------c--------------------------")


#Product and aisles
aisle = ['a', 'b', 'c', 's']


aisle.sort()
product.sort()


a = {}
for index in range(4):
    res={aisle[index]:product[index]}
    a[aisle[index]] = product[index]

print a


print ("----------------QUESTION 2 ----------------------------------")

print ("")



print ("----------------------------a----------------------------------")

products = {'apples':7.3,'Bananas':5.5,'Bread':1.0,'Carrots':10.0,'Champagne':20.90,'Strawberries':32.6}

for i in products:

      print i,products[i]
