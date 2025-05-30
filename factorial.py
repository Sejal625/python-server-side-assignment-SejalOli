""" 4 Create a python function to calculate factroial of a number using recursion"""

def factorial(n):
    if n ==0 or n==1:
      return 1
    else:
     return n*factorial(n-1)
    
num = int(input("Enter a number :"))
if num < 0:
   print("Please Enter positive number.")
else:
   n = factorial(num)
   print("Factorial is :", factorial(num))