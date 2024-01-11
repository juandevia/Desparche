#Function Hello Wold!
def HelloWorld():
    print('Hello World!')
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


reverseString("My name is Juan Camilo Devia Bastos")


