#composition= "My name is Obiorah Emmanuel. \n I love hiking and taking a walk. \n I also love playing video games. \n I recently began python training and i am loving it"

#usercomposition= input('tell a story about yourself in not less than 10 sentences. \n please, put fullstop at the end of each sentence.\n')

#lines= usercomposition.split(sep='.', maxsplit=10)
#for line in lines:
 #   print(line)

#ame1 = 'Samuel'
#name2 ='Joseph'
#ms = open('C:/Users/hp/Documents/Projects.txt')
#print(ms)

 # 'Hello World. \n We are breaking Records in NIIT Enugu. \n Programming is for everybody.
#ms = open('C:/Users/hp/Documents/Projects.txt','r')
#document = ms.read()
#print(document)
'''
user = input('please, enter your score\n')
try:
    userscore =int(user)

    print('congratulations, your %d'%userscore)
#except:
    userscore= float(user)

except:
    print('your input is invalid\n kindly enter a valid score.')

else:
    print('we have received your score for calculation')


try:
    fh=open('desktop/samuel/niit.doc', 'r') #try to read a non-exixting file
except IOError: # to handle the error instead of terminating program  for not being to read the file
    print("Error! file or directory does not exist") #errpr message


#writing data into a file
fs = open('C:/Users/hp/Documents/Projects.txt', 'w')
note ="Hello guys', how's class today?\n I'm really thrilled with our progress"
doc=fs.write(note)

#hs=doc.search(startwith ='h:')
#print(hs)

fs = open('C:/Users/hp/Documents/Projects.txt', 'r')
doc = fs.read()
for word in doc:
    if word.startswith("h:"):
        print(word)

#list
mylist = [32,2,3,6]
#print(type(list))
print('This is a %s'%type(mylist))

classNames =['Emmanuel']



classNames =['David', 'Emmanuel', 'Bryan', 'John']
#print('Members of the class are %s'%classNames)
scores =[90,85,80,75]
#print(scores)
items =('Rice', 'Maggi','Lemmon','Bannana','Ukwa', 'Water Mellon')
itemlist =list(items)
print(items, type(items))

# trasversing a list
for item in itemlist:
    print('*', item)

count =0
for  name in classNames:
    count+=1
    print(count,name)

finalscore =[]
for score in scores:
    finalscore.append(score+5) #append is used to create a function to add a value to the end of the list. ( to the original scores. +5
print(finalscore)

# List operators
batch1=['Samuel', 'David']
batch2=['Emmanuel', 'John']
batch3=['Bryan','Jeremy']
allStudents= batch1 + batch2 + batch3
print (allStudents)

praise ='gbosa '
praise =praise*3
print(praise)


fisrt3Stds =allStudents[0:2]
fisrt3Std =allStudents[:3]
last3Stds =allStudents[3:]
print(last3Stds)
print(allStudents[-1]) # for the last item
print(allStudents[-2]) # 2nd to the last item
print(batch1[1]) #for the 2nd item

#List Methods
newStudent ='Elijah'
allStudents.append(newStudent)
print(allStudents)
finalscore.append(99)
print(finalscore)

batch2.extend(batch1)
print(batch2)

students =[]
students =allStudents.copy()
print(students)
print(allStudents)
students =[]
allStudents =allStudents.copy() #to transfer the items in allstudents into students
print(students)
print(allStudents)
students.clear() # to remove all the items in students
print(allStudents)
allStudents.remove('Samuel')
print(allStudents)
allStudents.insert(3, 'Sampson')
print(allStudents)

reversedStudents = allStudents.copy()
reversedStudents.reverse()
print(reversedStudents)
allStudents.reverse()

allStudents.pop()
print(allStudents)



# Dictionary
mydict=  {'Names':['Bryan, John, Bright'], 'Scores:':[78, 90, 89]}
print(mydict)

teacher ={'Names':'Samuel Cyril', 'Specialty': 'Python Programming', 'Qualification': 'Masters Degree'}
print(teacher)

positions ={1:'Ada', 2:'Emeka', 'Last':'Amaka'}
print(positions)

#Accessing Value in a dictionary
print(mydict['Names'])
print(mydict['Scores:'])
print(positions[1])

newPosition = positions.copy()
print('This is the copied dictionary',newPosition)
positions.clear()
print(positions)
print(len(positions))
print('This dictionary has %d'%len(newPosition),'items')

print(mydict.get('Names')) # used to retrieve the values in the 'Names' key

print(newPosition.keys()) #to retrive the names of the keys in a dictionary
print(mydict.items())#to retrive the keys and values of the dictionary
print(newPosition.values())

old_students = {'Names':['John', 'Emmanuel', 'Bryan','David','Bright'], 'Scores':[80,90, 92, 95, 99]}
new_students ={'Names':['Samuel', 'Elijah'], 'Scores':[89,90, 10]}
old_students.update(new_students) #to overide the content of students with new_students
print(old_students)
#print(new_students.has_key(1)) #no longer available in python 3 and above
print(1 in new_students) # used in place of dict.has_key() #in operator is used check if data in specified if a dictionary
students_values = new_students.values()
print(10 in students_values)


# Tuples

mytuple =()
mylist =[]
mydict ={}
mylist.append('Samuel') #possible
mydict['Name'] ="Samuel" #possible
print(mydict)
print(mylist)
#mytuple.append('Samuel') #impossible

from itertools import repeat
from tabnanny import check

mytuple ='Samuel'
print(mytuple)

students = ['Samuel', 'John', 'Emmanuel', 'Bright', 'Bryan', 'David'] #list
students = tuple(students) # converts the list to a tuple
print(students)

someStudents = students[0:4] #creating a new tuple from an exixting tuple.
print(someStudents)
del(someStudents)
#print(someStudents) some students has been deleted


# Tuple Operations

team1 =(80,85,90)
team2 =(90,85,70)
team = team2 + team1 #merging the tuples
print(team)
repTeam1 = team1 * 5 #repeating team1 five times
print(repTeam1)

checkFor70 = 70 in team1
print(checkFor70)

print('Hellow', repTeam1)

for number in team1:
    print("Hellow", number)

teamSize = len(team)
print(f"The tuple has {teamSize} items")

#print(any(team1)> 87 #to check if any value is greater than 87
scores = [ 69, 80, 50]
print(any(scores)< 69)
print(all(scores)>69) #false
print(sorted(scores))
enumerate

scoresTuple = tuple(scores)
print(max(scores))
print(min(students))
print(students)

names = ('Amaka', 'Adaobi', 'Adaeze', 'John', 'Emmanuel', 'Adaugo')
print(sorted(names))
print(min(names))
print(max(names))
'''
#Regular Expressions

import re
from tkinter.constants import PAGES
from unittest.mock import patch

text ="Cat Hit Cattle Kitten Our"
praise = "God is good all the time. \n His faithfulness never fail"
partern = r'fail$'
print(text)
partern=r'.t' #  to find any two two character that precedes 't'
print(re.findall(partern,praise),"is the beginning of all ")

praise = "God is good all the time. \n His faithfulness never fail \n God is my ever present help. \n God is amazing. \n God is precious' God is not partial."
partern = r'^fail$'
partern = r'God*'
names = "Samuel John Emmanuel Bright Bryan David Samson, Sampson James"
pat = r'J*o'
#partern = r'.t'
print(re.findall(partern,praise))
print(r'hello world\n God is the ultimate\n Jesus is the saviour of the world')

words = "Good God Friends Godly Goodness Life Gad"
pat = r'G.d+'
pat = r'G.d?'
pat =r'[GFL]od'# it is used to match anyone of the characters inside the bracket
print(re.findall(pat,words))

#[^] is used to match
pat = r'[^F].d'
print(re.findall(pat,words))

words ="sduhrjhi7353difvhuddhdyhu47352dyeudj"
pat = r'[A-Z,a-z]'
letters= (re.findall(pat,words))
print(letters)
print(re.findall(pat,words))
numbers =re.findall(r'[^A-Z,a-z]',words)
print(numbers)

#|(pipe)
words = "Good God Friends Godly Goodness Life Gad Fod"
print(re.findall(r'Goodness|Friends',words))