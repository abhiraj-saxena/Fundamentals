myList = [[[1,2,3],[4,5,6]],[7,8,9], [10,11,12]]

integers = []

OtherList = []

# finalList = []

def listloop(NumberList):
    for item in NumberList: 
        if type(item) == int:
            integers.append(item)
    

for mini_list in myList:
    while type(mini_list) == list:
        for i in range(0, 5):
            OtherList.append(mini_list[i])
            break
    print(OtherList)
        



















    # # if type(mini_list) == int:
    # #     break
    # #     #integers.append(mini_list)
    # for small_list in mini_list:
    #     for smaller_list in mini_list:
    #         while type(smaller_list) == list:
    #             print(smaller_list)
        

# for small_list in OtherList:
#     for number in small_list:
#         finalList.append(number)
    
# totalList = finalList + integers

# print(totalList)