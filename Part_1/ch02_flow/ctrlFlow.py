
print('Plz input your name:')
name = input()
# if, else
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hi, stranger.')

# if, elif, else
name = 'Unknown'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are neither Alice nor a little kid.')
