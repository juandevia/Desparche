##
## This program has some code that needs writing...
##  Once you have completed the "task", submit this file to D2L
##

#'''  Write a program to display all the keys and all the values of a dictionary.'''

#'''  Also, display just the value associated with one of the keys in the dictionary '''

# '''   ie:           cat
#                     puma
#                     dog
#                     wolf
#                     fish   ... and so on...

#                     wolf                     '''
 
# Use this Dictionary of animals in your program
quizD = { 'cat' : 'puma', 'dog' : 'wolf', 'fish' : 'shark', 'bug' : 'wasp' }

# Display each "key" and "value" of the dictionary
# This must be done using "for" loops, but can output in any style
# Display just the value associated with the key-->      [ 'dog' ]

#second part
for i in quizD.keys():
    print('key:', i ,'value:',quizD[i])

  
