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

def anagram(word1,word2):
    lowered1 = word1.lower()
    print(lowered1)
    lowered2 = word2.lower()
    print(lowered2)
    list1 = [char for char in lowered1]
    print(list1)
    list2 = [char for char in lowered2]
    print(list2)
    if len(list1) == len(list2):
        dict1 = {}
        dict2 = {}
        for char in list1:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        for char in list2:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1
        print(dict1)
        print(dict2)
        if set(dict1.keys()) != set(dict2.keys()):
            print("noshot")
        else:
            for key in dict1.keys():
                if dict1[key] != dict2[key]:
                    print("noshot")
                else:
                    print("these are angrams")
    else:
        print("no shot")

anagram("apple","pplea")