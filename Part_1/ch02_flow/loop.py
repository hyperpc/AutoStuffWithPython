# while
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

# break
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# continue
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password?(It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# for
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

total = 0
for num in range(101):
    total = total + num
print(total)

## while
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1

#range( , , )
for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, -1, -1):
    print(i)
