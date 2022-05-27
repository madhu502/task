# def display_student(name="Namrata",age=19):
#     print(f"Your name is {name},and your age is {age}")
# display_student(name="Ram")

#3. Assign a different name to function and call it through the new name
#Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.


# def display_student(name="Liban",age=19):
#     print(f"Your name is {name},and your age is {age}")
# display_student(name="Ram")

#5. What is the difference between 10 / 3 and 10 // 3?
#.-->10/3 shows the division and 10//3 shows the floor value which gives the quotient

#6. What about two asterisks (**)?
#--> ** shows the power of some number.for eg.2**2=4

# 7. What is the difference between local and global variables?
# -->Those variable that are declared outside the function are called global variables.
# -->Those variable that are declarde inside the function are called local variables.

# 8. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

# def fizz_buzz(x):
#     if x%3==0:
#         print("Fizz")
#     elif x%5==0:
#         print("Buzz")
#     elif x%3==0 and x%5==0:
#         print("FizzBuzz")
#     else:
#         print(x)
# x=int(input("Enter a number:"))
# fizz_buzz(x)

# 9. Write a function for checking the speed of drivers.
# If speed is less than 70, it should print “Ok”.
# if the speed is 80, it should print: “Warning”.

# def speed(n):
#     if n<70:
#         print("OK")
#     elif n>80:
#         print("Warning!!!")
# n=int(input("Enter the speed:"))
# speed(n)

# 10. Write a program that prompts the user to input a positive integer.
#  It should then print the multiplication table of that number.

# n=int(input("Enter a positive number to print multiplication table:"))
# for i in range(1,11):

#     print( n,"*",i,"=",n*i)

# 11. Write a program that prompts the user to input an integer and then
# outputs the number with the digits reversed.
#  For example, if the input is 12345, the output should be 54321.

# number_string = input("Enter the number:")
# print("number before reversing:",number_string)
# n=number_string[::-1]
# print("number after reversing:",n)

# 12. Write a python program that return the number of
# characters in a string.
# myList = "Parameter"

# myList="Paramater"
# n=len(myList)
# print(n)

# 13. Write a Python program to multiply all the numbers in a list using while and for loop.
# Sample list = [8,2,3,-1,7]

# list=[8,2,3,-1,7]
# total=1
# for i in list:
#     total= total*i
# print("Multiplication of list is:",total)

# 14. Write a Python program to sum all the numbers in a list using for loop and while loop.
# Sample list : [8, 2, 3, 0, 7]
# list=[8,2,3,0,7]
# total=0
# for i in list:
#     total=total+i
# print(total)

# 15. Accept string from the user and display only those characters which are
# present at an even index.

# n = input("Enter a string:")
# modified_str= n[::2]
# print(modified_str)

# 16. Accept string from the user and display only those characters which are
# present at an odd index.
# n = input("Enter a string:")
# modified_str= n[::2]
# print(modified_str)

# 17. Sum : 1 to 10 (or any number) using while loop.
# num = 15
# sum = 0
# while num > 0:
#     sum += num
#     num -= 1
# print("The sum is", sum)

# 18. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list=[0,1,2,3,4,5,6,7,8,9]
# modified_num=list[0:9:2]
# print(modified_num)

# 19. Write a Python program to print the odd numbers from a given list.
# Sample List : [12,13,14,15,16,17,18,19]
# list=[12,13,14,15,16,17,18,19]
# odd=list[1:8:2]
# print(odd)

# 20. Write a program to accept percentage and display the Category according to the  following criteria :
# Percentage	Category
# < 41	                     Failed
# >=41 & <55	Fair
# >=55 & <65	Good
# >=65	                     Excellent

# percentage=int(input("Enter your percentage to check your category:"))
# if percentage>=65:
#     print("Excellent")
# elif percentage>=55:
#     print("Good")
# elif percentage>=40:
#     print("Fair.")
# else:
#     print("Failed")


