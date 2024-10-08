"""
if 5 > 2:
    print("five is greater than two!")



This is a comment
written in
more than just one line

print("Hello, World!")
x = 4
age = 20
y = "women under the age 20"
z = "women above age 20"
print ('age > 20')


#Python List Method
thelist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thelist)
print(len(thelist))
print(type(thelist))
thelist = list(("apple", "banana", "cherry", "apple", "cherry"))
print(thelist)

print(thelist[1])#Access list items
print(thelist[-1]) #-1 refers to the last item in the list

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #return item 3,4 and 5
print(thislist[2:5]) #Note: The search will start at index 2 (included) and end at index 5 (not included).
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
print(thislist[2:6])
print(thislist[4])
print(thelist[4])
print(thislist[:4])
print(thelist[:4])
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included
print(thislist[2:])
print(thislist[-4:-1])
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,

#Check if Item Exist
#check if apple is present in the list:
list = ["apple", "banana", "cherry"]
if "apple" in list:
    print("Yes, 'apple' is in fruits list")

#Change Item Value
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)
thislist[1:3] = "mango", "watermelon"
print(thislist)


fruits = ["apple", "orange", "mango"]
#x, y, z = fruits
#print(x)
print(y)
print(z)

X = Y = Z ="Orange"
print(X)
print(Y)
print(Z)
"""

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x) #If you create a variable with the same name inside a function,
    # this variable will be local, and can only be used inside the function.
    # The global variable with the same name will remain as it was, global and with the original value.

myfunc()
print("Python is " + x)

fruits = ("Mango")
def myfunc():
    fruits= "Coconut"
    print("this is " + fruits)
myfunc()
print("this is " + fruits)