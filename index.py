import sys

# double every second digit
def checkSum(numbers):
    # get length of numbers input
    length = len(numbers)
    # checks from the last digit in numbers input and checks every second number
    for i in range(length-2,0,-2):
        # gets the value of each number and not the index position
             num = numbers[i]
            #  doubles the returned number
             double_num = num * 2
            #  check for if the doubled number is greater and 9
             if double_num > 9:
                 print(double_num)
             
        

checkSum([2,9,3,8,5])
