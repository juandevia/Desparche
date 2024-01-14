#Function Hello Wold!
import math 
#In this case I just imported this library for write the pi number

def HelloWorld():
    print( 'Hello World!')
#Function reverse a vector or array
def ReverseVector(a):
    #Variable i means the interactor and range the range that i´m moving in, so i´m moving between 0 and the size of the variable a  
    for i in range(0,len(a)):
        print(a[len(a)-1-i])

def reverseString(string):
    reversed_string = ""
    for char in string:
#the order is importat due it concatenates the new letter to the beggining of the string
        reversed_string=char + reversed_string
    print(reversed_string)

#Function to convert radiants to degrees 
def Radiants2Degree(a):
    degree=a*180/math.pi
    print( a, " In degrees is ", degree)

def ex1():
    print( ' "$20 says he\'s not lying " ')

#in this function i'm getting the higher number of a list
def getHighest(a):
    aux=0 # Set the auxiliar variable that´s going to take the value of the highest number of the list
    for i in a:
        if i> aux:
            aux=i
    return(aux)
#in this function i´m getting the lowest number of an array 
def getLowest(a):
    # set this variable that is going to take the lowest number of an array
    aux=1000000000000000000000000000 
    for i in a:
        if i<aux:
            aux=i
    return(aux)

Radiants2Degree(49.8)

