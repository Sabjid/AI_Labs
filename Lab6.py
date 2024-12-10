                # TASK 1
def Sum():
    num = int(input("Enter Number: ")) 
    sum = 0  
    for i in num: 
        sum = sum + (i)  
    print("The sum of numbers is",sum)  

Sum()




                # TASK 2
def count_Sentance():
 Sen=input("Enter Sentence :")
 print("The number of Sentance is :",len(Sen))
count_Sentance() 

def is_even(number):
  return number % 2 == 0
  number = int(input("Enter a number: "))
  if is_even(number):
   print(number, "is even.")
  else:
   print(number, "is odd.")
is_even(number)
