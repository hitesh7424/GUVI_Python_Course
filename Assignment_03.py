# Write a code using a function to check whether a given number is even or odd
def even_Odd(num):
    if num%2:
        return "odd"
    else:
        return "even"

# Write a code using a function to check whether a given number is prime number or not
def is_Prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2,int(num/2)):
        if num%i == 0:
            return False

    return True

# Write a code to print a Fibonacci series upto the nth term. Use the int(input()) to get an input from the user as well for the value of n.)
def fibinacci_Series(num):
    series = [1]

    if num == 0:
        return []
    elif num == 1:
        return series

    series.append(1)
    for i in range(num-2):
        series.append(series[i] + series[i + 1])
    
    return series


num = int(input())

print(even_Odd(num))
print(is_Prime(num))
print(fibinacci_Series(num))