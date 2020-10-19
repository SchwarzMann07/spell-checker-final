print("Title of program: spell-checker bot")
print()
while True:
  description = input("Type the following: dfgsaguffeu")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "dfgswefwefwefwewfefaguffeu":
      feelings_list.append("nice")
      encouragement_list.append("this is correct! nice typing!")
      counter += 1

  if counter == 0:
    
      output = "Sorry this is wrong, try again?"

  elif counter == 1:
    
      output = "It seems that you typing is " + feelings_list[0] + ".  remember that "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that your typing is " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
