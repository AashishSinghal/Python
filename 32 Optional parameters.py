# Optional Parameter #1
'''
def func(x=2):
    return x ** 2

call = func(5)
print(call)
#print(func(5))

def func1(word, add = 5, freq = 1):
    print(word*(freq+add))


call = func1("tim ", 4)
call = func1("tim ", 0)

#print(func(5))
'''

class car(object):
    def __init__(self, make, model, year, condition = "New", kms = 0):
        self.make = make
        self.model = model
        self.year = year
        self. condition = condition
        self.kms = kms

    def display(self, showAll = True):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is %s %s from %s." %(self.make, self.model, self.year))

whip = car("Ford", "Fusion", 2012,)
whip.display(False)

