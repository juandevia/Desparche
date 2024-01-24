
import math 
# I imported this library to write the value of pi

def HelloWorld():
    print('Hello World!')

# Function to reverse a vector or array
def ReverseVector(a):
    # Variable i represents the iterator, and range specifies the range of indices from 0 to the size of the array a
    for i in range(0, len(a)):
        print(a[len(a) - 1 - i])

# Function to reverse a string
def reverseString(string):
    reversed_string = ""
    for char in string:
        # The order is important because it concatenates the new letter to the beginning of the string
        reversed_string = char + reversed_string
    print(reversed_string)

# Function to convert radians to degrees 
def Radiants2Degree(a):
    degree = a * 180 / math.pi
    print(a, " in degrees is ", degree)

def ex1():
    print('"$20 says he\'s not lying"')

# Function to get the highest number in a list
def getHighest(a):
    aux = 0  # Set the auxiliary variable that will take the value of the highest number in the list
    for i in a:
        if i > aux:
            aux = i
    return aux

# Function to get the lowest number in an array 
def getLowest(a):
    # Set this variable that is going to take the lowest number in an array
    aux = float('inf')  # Initialize with a large positive value
    for i in a:
        if i < aux:
            aux = i
    return aux

# Function to organize an array from the lowest number to the greatest
def bubbleSort_LG(a):
    aux = 0
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                aux = a[i + 1]
                a[i + 1] = a[i]
                a[i] = aux
    print(a)

# Function to organize an array from the greatest number to the lowest
def BubbleSort_GL(a):
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] < a[i + 1]:
                aux = a[i + 1]
                a[i + 1], a[i] = a[i], a[i + 1]
    print(a)

# Calculator to represent Match Fuction
def ExampleOfMatch():

    # asking for the numbers
    a=float (input('Introduce the first number: '))
    b=float (input('Introduce the second number: '))

    #example of the function

    case=int (input('Press: \n 0 for add(+)\n 1 for substracting(-) \n 2 for multiplication(*) \n 3 for division(/): '))

    match case:
        case 0:
            print(a,'+',b,'=',a + b)
        case 1:
            print(a,'-',b,'=',a - b)
        case 2:
            print(a,'*',b,'=',a * b)
        case 3:
            if b != 0:
                print(a,'-',b,'=',a / b)
            else:
                print('error')



ExampleOfMatch()