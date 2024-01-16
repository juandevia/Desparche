print("This line uses simple quotes! \n\n\n", "This line uses double quotes... \n\n", "Lots of blank lines in between!",sep='')
print("\t")


def InputFun():
    x = float (input(" Can you Input the x for the x = x (y + 1) "))
    y = float (input(" Can you Input the y for the x = x (y + 1) "))
    x *= y + 1
    print( 'The result is', x)


InputFun()

