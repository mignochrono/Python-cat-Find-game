import time
catlocation = 0
leng= ["1.espanol","2.english"]
print ("select lenguage/seleccione idioma")
print (*leng, sep="\n")

leng_select = int(input())
if leng_select == 2:
  while catlocation != 4:
      print('starting')
      time.sleep(5)
      #ask the question
      question = "where is the cat?"
      print(question)
      #shows options in a list
      options = ["1.it is on the tree", "2.it is on his house", '3.it is on the backyard','4.exit']
        #i copied this code from (https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/) i still dont know why i need the (*) and what does the (sep) means. i can deduce that the ("\n") is a string for new line? i need to do more research
      print(*options, sep="\n")
        #i get imput from user
      catlocation = input()
        #i change the imput to a integrer number
      catlocation = int(catlocation)
        #i use the (if) statement to check if the number stored on the variable "catlocation" is equal to int(1) if not i print "looking"
      if (catlocation == 1):
            print('the cat is on the tree')
      
        #i bassically do the same over and over again.  is there a more efficient way to do this?
      if (catlocation == 2):
            print('the cat is on the house')

      if (catlocation == 3):
        print('the cat is on the backyard')
        

  print('exiting program')

elif leng_select == 1:
  while catlocation != 4:
      print('iniciando')
      time.sleep(5)
      #ask the question
      question = "donde esta el gato?"
      print(question)
      #shows options in a list
      options = ["1.en el arbol", "2.en su casita", '3.en el patio','4.salir']
        #i copied this code from (https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/) i still dont know why i need the (*) and what does the (sep) means. i can deduce that the ("\n") is a string for new line? i need to do more research
      print(*options, sep="\n")
        #i get imput from user
      catlocation = input()
        #i change the imput to a integrer number
      catlocation = int(catlocation)
        #i use the (if) statement to check if the number stored on the variable "catlocation" is equal to int(1) if not i print "looking"
      if (catlocation == 1):
            print('el gato esta en el arbol')
      
        #i bassically do the same over and over again.  is there a more efficient way to do this?
      if (catlocation == 2):
            print('el gato esta en la casa')

      if (catlocation == 3):
        print('el gato esta en el patio')
        

  print('cerrando programa')

#extra code not used
#elif (catlocation == 2):
#print("the cat is on the house")
#elif (catlocation == 3):
#print("the cat is on the backyard")

#https://www.youtube.com/watch?v=shO5VbD2rNI