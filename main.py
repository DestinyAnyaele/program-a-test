# A mini project 😁
# A little quiz
import time
print('welcome to Anyaele Destiny Chinaemerem quiz')
print('Please wait ...')
time.sleep(1.5)
Name = input('What is your Name : ')
print('Whoa! great name')
print('Please wait... while storing your data')
time.sleep(1.5)
print('Start with upper case while answering questions')
time.sleep(3)
response = str(input('Would you like to take quiz : '))
for loop in range(2) :
  if response == 'Yes' :
     print('Loading questions...')
     break
  elif response == 'No' :
    print('Bye-Bye')
    time.sleep(1.5)
    quit()
  else :
    print('You gave a wrong input')
    print('Please follow instructions')
    print('Trying again...')
    time.sleep(1)
    print('welcome to Anyaele Destiny Chinaemerem quiz')
    print('please wait ...')
    time.sleep(1.5)
    print('Start with upper case while answering questions')
    time.sleep(4)
    response = input('Would you like to take quiz : ')
if response != 'Yes' :
  print("You really don't follow instructions")
  time.sleep(1)
  print('Bye-Bye')
  time.sleep(1)
  quit()
elif response == 'No' :
  print('Bye-Bye')
  time.sleep(2)
  quit()
else :
  pass
Answer_1 = str(input('Question 1 : What is "python" programing language named after : '))
if Answer_1 == 'Python monty flying circus' :
  print('you are correct , ',end = '')
  print('You have gained 5 points')
  x = 5
else :
  print('You are wrong , ',end = '')
  print('you have gained 0 points')
  print('The answer is Python monty flying circus')
  x = 0
Answer_2 = str(input('Question 2 : What inbuilt python module can be used to change strings to uppercase or lowecase : '))
if Answer_2 == 'String' or Answer_2 ==  'String module' :
  print('You are correct , ',end = '')
  print('You have gained 5 points')
  y = 5
else :
  print('You are wrong , ',end = '')
  print('You have gained 0 point')
  print('String module can be used to change strings to lowercase or uppercase')
  y = 0
Answer_3 = str(input('Question 3 : what is use to call a function in python : '))
if Answer_3 == '()' :
  print('You are correct , ',end = '')
  print('You have gained 5 points')
  z = 5
else :
  print('You are wrong , ',end = '')
  print('You have gained 0 point')
  z = 0
Answer_4 = str(input('what is used to tell python you a variable referred in a local scope or in a function is a global variable not local : '))
if Answer_4 == 'global' :
  print('You are correct , ',end = '')
  print('you have gained 5 points')
  a = 5
else :
  print('you are wrong , ',end = '')
  print('You have gained 0 point')
  print('The answer is "global"')
  a = 0
Answer_5 = str(input('What is my first name : '))
if Answer_5 == 'Anyaele' or Answer_5 == 'Destiny' or Answer_5 == 'Anyaele Destiny Chinaemerem' :
  print('You are correct , ' , end = '')
  print('You have gained 0 points')
  b = 5
else :
  print('You are wrong , ',end = '')
  print('You have gained 0 points')
  print('The answer is "Destiny"')
  b = 0
print('End of test')
score = x + y + z + a + b
print('please wait... calculating your score')
time.sleep(2)
print(str(Name) + str(' You got a total of ') + str(score) +str(' points out of 50'))
print('please wait... calculating your percentage')
time.sleep(2)
percentage = (score / 50) * 100
print(Name,' You have a percentage of ',percentage,'%')
