def spam():
    global eggs
    eggs = 'spam'  # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs)    # this is the global

eggs = 42          # this is the global
spam()
print(eggs)        # spam
bacon()
print(eggs)        # spam

def spam2():
    print(eggs2)   # UnboundLocalError: local variable 'eggs2' referenced before assignment
    eggs2 = 'spam2 local'

eggs2 = 'global'
spam2()