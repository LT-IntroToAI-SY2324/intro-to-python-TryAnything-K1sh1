# Complete your individualized AI problems here


# # variable that gets a word from the user
# word = input("Give me a word that is spelled the same forward and backward: ")
# reverseWord = word[::-1] # this variable gets the input given above and reverses it
# print(word)
# print(reverseWord)

# if word == reverseWord:
#     print("this word is pelled the same backwards and forwards")
# else:
#     print("this word is not the same forward and backward")

num1 = input("give me a number: ")

def factorial(num1):
    for number in range(int(num1)):
        if number != num1:
            num2 = int(num1) * (int(num1)-number)
            num1 = num2
            print(num1)

factorial(num1)

