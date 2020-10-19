print("Title of program: spell-check ver 2")
print()
print("This is a program for people to check their typing skills for accuracy")

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "type this: sdfghjhgfdwtyuj")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "sdfghjhgfdwtyuj":
    output = "Yes, that's right!"
    tracker =1
    score +=1
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
  
  print("Q"+str(counter)+") "+ "type this: e2f6ge7h4c8yn359")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "e2f6ge7h4c8yn359":
    output = "Yes, that's right!"
    tracker =1
    score +=1
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
  
  print("Q"+str(counter)+") "+ "type this: qyf8yge8r383r0-`~")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "qyf8yge8r383r0-`~":
    output = "Yes, that's right!"
    tracker =1
    score +=1
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
