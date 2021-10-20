import random

def getAnswer(answerNumber):
    result = ''
    if answerNumber == 1:
        result = 'It is certain'
    elif answerNumber == 2:
        result = 'It is decidedly so'
    elif answerNumber == 3:
        result = 'Yes'
    elif answerNumber == 4:
        result = 'Reply hazy try again'
    elif answerNumber == 5:
        result = 'Ask again later'
    elif answerNumber == 6:
        result = 'Concentrate ans ask again'
    elif answerNumber == 7:
        result = 'My reply is no'
    elif answerNumber == 8:
        result = 'Outlook not so good'
    elif answerNumber == 9:
        result = 'Very doubtful'
    return result

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1,9)))