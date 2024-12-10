          #TASK 1
def draw_square(side_length):
 
    for _ in range(side_length):
        print('*' * side_length)
length = int(input("Enter the side length of the square: "))
draw_square(length)

           #TASK 2

def sum_of_even_numbers(numbers):
   
    return sum(num for num in numbers if num % 2 == 0)


numbers_list = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(numbers_list)
print(f"The sum of even numbers in the list is: {result}")

              #TASK 3

def countdown_to_zero(number):
   
    for i in range(number, -1, -1):
        print(i)


start_number = int(input("Enter a number to count down from: "))
countdown_to_zero(start_number)