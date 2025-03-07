# A function with parameters

def add(a): #-----------> a is a parameter
    print(a)

add(9) #--------------> 9 is an argument
add(10) #-------------> 10 is an argument
add(11) #-------------> 11 is an argument

# A function with multiple parameters

def num(a,b): #-----------> a and b are parameters
    print(a + b)

num(9,10) #--------------> 9 and 10 are arguments
num(10,11) #-------------> 10 and 11 are arguments

def num1(a,b,c): #-----------> a, b and c are parameters
    print(a + b + c)

num1(9,10,11)   #--------------> 9, 10 and 11 are arguments
num1(10,11,12) #-------------> 10, 11 and 12 are arguments

#  A function with default parameters

def default(a=10):
    print(a)

default() # 10 

def multiple(a=30 , b=20):
    print(a + b)

multiple() 
