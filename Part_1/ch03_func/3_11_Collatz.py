import sys

def Collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
        print(result)
    else:
        result = 3 * number + 1
        print(result)

    if result != 1:
        Collatz(result)

print('input 0 to exit this app.')
print('Enter number:')
while True:
    try:
        myInput = int(input())
        if(myInput==0):
            #sys.exit()
            break
    except:
        print('Only accept an integer.')
        print('input 0 to exit this app.')
        continue
    
    Collatz(myInput)