print("Title of program: spell-check ver 2")
print()
print("This is a program for people to check their typing skills for accuracy")

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

  
import random

while tracker !=1:
  
  input("Start")
  start_time = time.time()
  
  print("Q"+str(counter)+") "+ "type this: sdfghjhgfdwtyuj")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "sdfghjhgfdwtyuj":
    output = "Yes, that's right!"
    tracker =1
    score +=1
    
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    
  else :
    output = "Wrong. Check again."
    score -=1
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  input("Start")
  start_time = time.time()
  
  print("Q"+str(counter)+") "+ "type this: e2f6ge7h4c8yn359")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "e2f6ge7h4c8yn359":
    output = "Yes, that's right!"
    tracker =1
    score +=1
    
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    
  else :
    output = "Wrong. Check again."
    score -=1

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  input("Start")
  start_time = time.time()
  
  print("Q"+str(counter)+") "+ "type this: qyf8yge8r383r0-`~")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "qyf8yge8r383r0-`~":
    output = "Yes, that's right!"
    tracker =1
    score +=1
    
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    
  else :
    output = "Wrong. Check again."
    score -=1
  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("Well Done!")
print("End of quiz! Hope you had fun!")
