# #Task
# The provided code stub reads two integers from STDIN,
# and . Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
# a= 3
# b= 5

# Print the following:
# 8
# -2
# 15

if __name__ == '__main__':
    while True:
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
            print(a + b)
            print(a - b)
            print(a * b)
            break
        except:
            print('Enter valid integer input')

#learnings: infinite while loop, try and exception.