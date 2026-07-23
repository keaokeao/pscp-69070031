"""หารเลข"""
number = int(input())

number -= (number % 10)

while number >= 0 :
    print(number, end = " ")
    number -= 10
