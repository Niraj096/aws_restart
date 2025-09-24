# Exercise 1: Creating a mixed-type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Traverse the list with a for loop and print item with its data type
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)));

   


for item in myMixedTypeList:
    print(item, "is of the data type", type(item))
