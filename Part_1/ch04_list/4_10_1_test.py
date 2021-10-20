def joinList(myList):
    result = ""
    lengthOfList = len(myList)
    if lengthOfList == 0:
        result = ""
    elif lengthOfList == 1:
        result = myList[0]
    else:
        for i in range(lengthOfList):
            if i == lengthOfList - 1:
                result += "and " + myList[i]
            else:
                result += myList[i] + ", "
    print(result)

#joinList()  # TypeError: joinList() missing 1 required positional argument: 'myList'
print("***** 1 *****")
spam = []
joinList(spam)
print("***** 2 *****")
spam = [""]
joinList(spam)
print("***** 3 *****")
spam = ['apple']
joinList(spam)
print("***** 4 *****")
spam = ['apple', 'bananas', 'tofu', 'cats']
joinList(spam)