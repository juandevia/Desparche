
def InputFun():
    x = float (input(" Can you Input the x for the x = x (y + 1) "))
    y = float (input(" Can you Input the y for the x = x (y + 1) "))
    x *= y + 1
    print( 'The result is', x)

def ExampleOfMatch():
    a=float (input('Introduce the first number: '))
    b=float (input('Introduce the second number: '))
    case=int (input('Press 0 for add(+) 1 for substracting(-) 2 for multiplication(*) 3 for division(/): '))
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



