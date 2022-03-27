import time
print('welcome to Anyaele Destiny Chinaemerem quiz')
print('please wait ...')
time.sleep(1.5)
Name = input('what is your Name : ')
print('Whoa! great name')
print('please wait... while storing your data')
time.sleep(3)
print('Start with upper case while answering questions')
time.sleep(4)
response = input('would you like to take quiz : ')
if response == 'Yes' :
  print('ok, you are welcome to my quiz')
  time.sleep(2)
  Question_1 = input('question_1 : Who is the President of Nigeria : ')
  if Question_1 ==  'Mohammed Buhari' :
    print('please wait')
    time.sleep(2)
    print('Correct !  ',end  = '')
    print('You have gained 5 points')
  else :
    time.sleep(1.6)
  
    print('incorrect !  ',end = '')
    print('You have gained 0 points')
    print('The answer is : ',end = '')
    time.sleep(2.5)
    print('Mohammed Buhari')
  Question_2 = input('Question 2 : What is the programming language "PYTHON" named after')
  if Question_2 ==  'Monty python flying circus' :
     time.sleep(2)
     print('Correct  ',end = '')
     print('You have gained 5 points')
  else :
    print('you have gained 0 points')
  Question_3 = input('String')
  List = list(Question_3)
  'boy' or 'girl' in List
elif response == 'No' :
  print('Bye-Bye')
  time.sleep(2)
  quit()
else :
  print('you entered an incorrect response')
  time.sleep(2)
  print('welcome to Anyaele Destiny Chinaemerem quiz')
  print('please wait ...')
  time.sleep(3)
  print('Start with upper case while answering questions')
  response_2 = input('would you lke to try again : ')
  if response_2 == 'Yes' :
    print('ok, you are welcome to my quiz')
  else :
    print('Bye-Bye')
  