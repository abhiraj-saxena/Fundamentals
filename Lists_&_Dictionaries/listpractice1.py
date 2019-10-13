from collections import defaultdict
# message = "aaabbbbcccc"

# count = {}
# # numbertally = []
# greatestNumber = 0

# for letter in message:
#     count.setdefault(letter,0)
#     count[letter] = count[letter] + 1
# #    numbertally.append(count[letter])
# #    numlength = len(numbertally)
# for number in count.values():
#     if greatestNumber < number:
#         greatestNumber = number


# print(greatestNumber)


"""
given two dictionaries such as {a:1, b:2, c:5,e:1}, and {a:5, b:2, c:6, d:2} combine the dictionaries {a:6, b:4, c:11, d:2, e:1}
"""
dict1 = {"a":1, "b":2, "c":5, "e":1}
dict2 = {"a":5, "b":2, "c":6, "d":2}
dict3 = {}

for letter1 in dict1.keys():
    for letter2 in dict2.keys():
        if letter1 == letter2:
            dict3.update({letter1: dict1[letter1] + dict2[letter2]})
        elif letter1 not in dict2.keys():
            dict3.update({letter1: dict1[letter1]})
        elif letter2 not in dict1.keys():
            dict3.update({letter2: dict2[letter2]}) 

print(dict3)






