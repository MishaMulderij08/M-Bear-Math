#Creating 4 variables to store each dice roll
d1 = 1
d2 = 1
d3 = 1
d4 = 1

#Sum of all the dice results and combinations
dScoreSigma = 0

#Number of sides on the dice (this is NOT customizable with this version of code)
sides = 6

#Total number of throws being x sided dice ^ 4
throws = sides*sides*sides*sides

#Recording how many times each possible roll appeared
roll3 = 0
roll4 = 0
roll5 = 0
roll6 = 0
roll7 = 0
roll8 = 0
roll9 = 0
roll10 = 0
roll11 = 0
roll12 = 0
roll13 = 0
roll14 = 0
roll15 = 0
roll16 = 0
roll17 = 0
roll18 = 0

for i in range(throws):
  #Create a list of all dice rolls
  dList = [d4, d3, d2, d1]
  #Identify the smallest Value
  dSmallest = min(dList)
  #Calculate the score for that List of rolls
  dScore = d1+d2+d3+d4-dSmallest
  #Add it to the total
  dScoreSigma = dScoreSigma + dScore
  
  #Take note of the value rolled and add it to a frequency table
  if dScore == 3:
    roll3 = roll3+1
  if dScore == 4:
    roll4 = roll4+1
  if dScore == 5:
    roll5 = roll5+1
  if dScore == 6:
    roll6 = roll6+1
  if dScore == 7:
    roll7 = roll7+1
  if dScore == 8:
    roll8 = roll8+1
  if dScore == 9:
    roll9 = roll9+1
  if dScore == 10:
    roll10 = roll10+1
  if dScore == 11:
    roll11 = roll11+1
  if dScore == 12:
    roll12 = roll12+1
  if dScore == 13:
    roll13 = roll13+1
  if dScore == 14:
    roll14 = roll14+1
  if dScore == 15:
    roll15 = roll15+1
  if dScore == 16:
    roll16 = roll16+1
  if dScore == 17:
    roll17 = roll17+1
  if dScore == 18:
    roll18 = roll18+1
  
  #This code will display each combination to see what the code does (recommended to keep turned off as it can get laggy printing all combinations)
"""  print(str(i+1) + " : " + str(dList) + " : " + str(dScore))
  #print("")"""
  #Filter through to the next roll similar to a regular counting system / binary (described in Github)
  if d3==sides:
    if d2==sides:
      if d1==sides:
        d1=1
        d2=1
        d3=1
        d4=d4+1
      else:
        d1=d1+1
    else:
      if d1==sides:
        d1=1
        d2=d2+1
      else:
        d1=d1+1
  else:
    if d2==sides:
      if d1==sides:
        d1=1
        d2=1
        d3=d3+1
      else:
        d1=d1+1
    else:
      if d1==sides:
        d1=1
        d2=d2+1
      else:
        d1=d1+1

#Once gone through all values, find the mean score and display all the data
dAverageScore = dScoreSigma/throws
print("Mean")
print(dAverageScore)
print("Distribution")
#Value of dice roll: Frequency
print("3: " + str(roll3))
print("4: " + str(roll4))
print("5: " + str(roll5))
print("6: " + str(roll6))
print("7: " + str(roll7))
print("8: " + str(roll8))
print("9: " + str(roll9))
print("10: " + str(roll10))
print("11: " + str(roll11))
print("12: " + str(roll12))
print("13: " + str(roll13))
print("14: " + str(roll14))
print("15: " + str(roll15))
print("16: " + str(roll16))
print("17: " + str(roll17))
print("18: " + str(roll18))
