'''
Write a program that reads integers user_num and div_num as input, and outputs user_num divided by div_num three times using floor divisions.

Ex: If the input is:

2000
2
the output is:

1000 500 250
Note: In Python 3, floor division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).
'''

user_num = int(input())
div_num = int(input())
print(user_num//(div_num),user_num//(div_num*div_num),user_num//(div_num*div_num*div_num))