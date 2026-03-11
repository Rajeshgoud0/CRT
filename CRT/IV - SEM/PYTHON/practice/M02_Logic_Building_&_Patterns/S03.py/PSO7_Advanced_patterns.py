'''n=6
for i in range(n):
    c=1
    for j in range(1,i+1):
        print(c,end="")
        c=c*(i-j)//j
    print()

#find largest number in list
def largest_number(lst):    
    if not lst:
        return None  # Return None for an empty list
    max_num = lst[0]  # Initialize max_num to the first element
    for num in lst:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num
#palindromedef is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces 
    return s == s[::-1]  # Check if the string is equal to its reverse
#fibonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
 #remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))  # Convert to set to remove duplicates and back to list
#count occurrences of each element in list

#find the sum of numbers from 1 to n
def sum_of_numbers(n):
    return n * (n + 1) // 2  # Using the formula n(n+1)//2
#find max in list
def find_max(lst):
    if not lst:
        return None  # Return None for an empty list
    max_num = lst[0]  # Initialize max_num to the first element
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num
'''
#find lcm and hcf of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b) 
#chack number is purfect square or not
import math
def is_perfect_square(n):
    if n < 0:
        return False  # Perfect squares are non-negative
    root = int(math.sqrt(n))
    return root * root == n 
