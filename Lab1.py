                  # Task 1
                  # Program 1:  integers
a = 5
b = 10
print( a + b)

# Program 2: Check if a number is even or odd
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
               #  program 1 : Float 
               # Fahrenheit to Celsius
fahrenheit = 27.4
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")


             # Program 2: Celsius to Fahrenheit
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

              # Program 1:  Strings
greeting = "Hello"
name = "World"
print(greeting + " " + name)

               # Program 2:  String 
word = "Hello"
print((  word  + "" )* 3)

                   # Program 1:  List
fruits = ["apple", "orange", "cherry"]
print("First fruit:", fruits[0])

                    # Program 2: List
numbers = [1, 2, 3]
numbers.remove(1)

print("Modified list:", numbers)

                    # Program 1:  Tuple 
coordinates = (10, 20)
print("X-coordinate:", coordinates[0])

                      # Program 2: Tuple 
axis = (5, 10)
x , y = axis
print("x:", x, "y:", y)

                    # Program 1:  Dictionary 
person = {"name": "Ali", "age": 25}
print("Name:", person["name"])

                       # Program 2:  Dictionary 
person["city"] = "New York"
person["age"] = 26
print("Updated person info:", person)


                    # Program 1:  Set 
colors = {"red", "green", "blue"}
colors.add("yellow")
print("Colors set:", colors)

                     # Program 2: Set
if "green" in colors:
    print("Green is in the set")


           # Program 1: Boolean  with AND and OR
a = True
b = False
print("a AND b:", a and b)
print("a OR b:", a or b)

               # Program 2: Boolean
num = -10
is_positive = num > 0
print("Is number positive?", is_positive)

                       # Task 2
          # 10 Programs :  Shapes using Strings
print("Square:\n" + "****\n" * 4)
print("Triangle:\n  *  \n *** \n*****")
print("Rectangle:\n" + "*****\n" * 3)
print("Diamond:\n  *  \n *** \n*****\n *** \n  *  ")
print("Arrow:\n  *  \n *** \n*****\n  |  \n  |  ")
print("Heart:\n ** ** \n*******\n ***** \n  ***  \n   *   ")
print("Right-angled triangle:\n*\n**\n***\n****")
print("Divide:\n  *  \n*****\n  *   ")
print("Star:\n  *  \n * * \n*****\n * * \n  *  ")
print("House:\n   *   \n  ***  \n ***** \n*******\n |   |")

