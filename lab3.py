# Program 1
# N = int(input('Enter a number to find its fourth root: '))
# guess = 0
# while guess ** 4 < N :
#     guess = guess + 1
# if guess ** 4 != N :
#     print(N, 'does not have a fourth root.')
# else :
#     print(guess, 'is the fourth root of', N)
    
# Program 2
# N = int(input('Enter an integer:'))
# found = False;
# r = 0
# p = 2
# while(p < 6):
#     while(r**p <= N):
#         if(r**p == N):
#             found = True
#             break
#         r+=1
#     if(found):
#         break
#     r = 0
#     p+=1
#     
# if(found):
#     print("Root:", r, "Power:", p)
# else:
#     print("No integer root smaller than the 6th root exists for", N)

# Program 3
# N = int(input('Enter an integer:'))
# found = False;
# r = 0
# p = 2
# while(r**p <= N):
#     while(p < 6):
#         if(r**p == N):
#             found = True
#             break
#         p+= 1
#     if(found):
#         break
#     p = 2
#     r+=1
#     
# if(found):
#     print("Root:", r, "Power:", p)
# else:
#     print("No integer root smaller than the 6th root exists for", N)

# Program 4
# N = int(input("Enter a number: "))
# p = input("Enter a phrase: ")
# for i in range(N):
#     print(p)

# Program 5
# largestOdd = 0
# for i in range(10):
#     num = int(input("Enter number " + str(i+1) + ": "))
#     if(num % 2 != 0 and num > largestOdd):
#         largestOdd = num
# if(not largestOdd):
#     print("None of the numbers were odd")
# else:
#     print("The largest odd number was", largestOdd)

# Program 6
# s = input("Enter a string of characters: ")
# total = 0
# for i in s:
#     if(i.isdigit()):
#         total += int(i)
# print("The sum of all the digits is", total)

# Program 7
# s = input("Enter a list of decimal numbers: ")
# total = 0.0
# for i in s.split(','):
#     total += float(i)
# print(total)

# Program 8
# x = -1
# firstAsk = True
# while(x < 0):
#     if(firstAsk):
#         x = int(input("Please enter a positive number: "))
#         firstAsk = False
#     else:
#         x = int(input("That was a negative number. Please enter a positive number: "))
# epsilon = 0.01
# low = 0.0
# high = max(1.0, x)
# guess = (low + high) / 2
# numberofguesses = 0
# while abs(guess ** 2 - x) > epsilon :
#     print('low =', low, 'high =', high, 'guess =', guess)
#     if guess** 2 > x : # the guess is too high, so move high down to guess
#         high = guess
#         guess = (low+high) / 2
#     else : # the guess is too low, so move low up to guess
#         low = guess
#         guess = (low+high) / 2
#     numberofguesses+=1
# print('number of guesses:', numberofguesses)
# print(guess, 'is close enough to the square root of ', x)

# Program 9
# x = int(input("Please enter a number: "))
# epsilon = 0.01
# low = 0.0
# if(abs(x) > 1.0):
#     high = x
# else:
#     high = 1.0
# guess = (low + high) / 2
# numberofguesses = 0
# while abs(guess ** 3 - x) > epsilon :
#     print('low =', low, 'high =', high, 'guess =', guess)
#     if abs(guess** 3) > abs(x) : # the guess is too high, so move high down to guess
#         high = guess
#         guess = (low+high) / 2
#     else : # the guess is too low, so move low up to guess
#         low = guess
#         guess = (low+high) / 2
#     numberofguesses+=1
# print('number of guesses:', numberofguesses)
# print(guess, 'is close enough to the cube root of ', x)

# Program 10
# n = int(input("Enter a positive integer: "))
# b = ""
# while(n != 0):
#     b+= str(n % 2)
#     n = n // 2
# print(b[::-1])