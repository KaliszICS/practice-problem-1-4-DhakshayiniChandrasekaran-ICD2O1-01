'''
  Lesson: Input and F strings 
  Author: Dhakshayini
  Date Created: September 19, 2024
  Date Last Modified: September 19, 2024
'''

def q1():
  #Write Assignment code here
  words = input("enter a word: ") 
  print (words)

def q2():
  #Write Assignment code here
  words = input("enter your name: ")
  print ("your name is " + words)

def q3():
  #Write Assignment code here
  Firstname = input ("enter your first name: ")
  Lastname = input ("enter your last name: ")
  
  word = f"your name is {Firstname} {Lastname}"
  print (word)

def q4():
  #Write Assignment code here
  student1 = input("Input a student")
  student2 = input("Input another student")

  word = f"your students are {student1} and {student2}"
  print(word)

#Do not edit code below this comment

q1()
q2()
q3()
q4()
