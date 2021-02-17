"""

print ('starting')
#ask the question
question="where is the cat?"
print(question)
#shows options in a list
options=["1.it is on the tree","2.it is on his house",'3.it is on the backyard']
#i copied this code from (https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/) i still dont know why i need the (*) and what does the (sep) means. i can deduce that the ("\n") is a string for new line? i need to do more research
print(*options, sep = "\n")
#i get imput from user
catlocation = input()
#i change the imput to a integrer number
catlocation = int(catlocation)
#i use the (if) statement to check if the number stored on the variable "catlocation" is equal to int(1) if not i print "looking"
if (catlocation == 1):
 print('the cat is on the tree')
else:
  print('looking')

#i bassically do the same over and over again.  is there a more efficient way to do this? 
if (catlocation == 2):
 print('the cat is on the house')
else:
  print('looking')


if (catlocation == 3):
 print('the cat is on the backyard')
else:
  print('looking')

#extra code not used
  #elif (catlocation == 2):
  #print("the cat is on the house")
  #elif (catlocation == 3):
  #print("the cat is on the backyard")
   


#https://www.youtube.com/watch?v=shO5VbD2rNI
"""

print('starting')
#ask the question
question = "where is the cat?"
print(question)
#shows options in a list
options = [
    "1.it is on the tree", "2.it is on his house", '3.it is on the backyard',
    '4.exit'
]
#i copied this code from (https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/) i still dont know why i need the (*) and what does the (sep) means. i can deduce that the ("\n") is a string for new line? i need to do more research
print(*options, sep="\n")
#i get imput from user
catlocation = input()
#i change the imput to a integrer number
catlocation = int(catlocation)
#i use the (if) statement to check if the number stored on the variable "catlocation" is equal to int(1) if not i print "looking"
while catlocation < 4:
	if (catlocation == 1):
		print('the cat is on the tree')
		break

#i bassically do the same over and over again.  is there a more efficient way to do this?
	if (catlocation == 2):
		print('the cat is on the house')
		break

	if (catlocation == 3):
		print('the cat is on the backyard')
		break

#extra code not used
#elif (catlocation == 2):
#print("the cat is on the house")
#elif (catlocation == 3):
#print("the cat is on the backyard")

#https://www.youtube.com/watch?v=shO5VbD2rNI
