#This program solves Project Euler problem 16: Power Digit Sum

num = 2**1000
sum = 0
while (num > 9):
    nextDigit = num % 10
    sum += nextDigit
    num = num//10
    print(num)

sum += num

print("The sum of all the digits of 2^1000 is: ", sum )

