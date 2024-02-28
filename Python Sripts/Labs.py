from urllib.request import urlopen 
import json
import requests
from io import BytesIO
import cv2
import numpy as np


def Lab2():
    
    ####################### exercise1 #########################################
    
    print('The','quick','sly','fox','Jumped','over','the','lazy','dog',sep='***\n',end='***')
    
    ####################### exercise2 ##########################################
    
    # store the URL in url as
    url = "http://api.open-notify.org/iss-now.json"
    
    # store the response of URL 
    response = urlopen(url) 
    
    # storing the JSON response 
    # from url in data 
    data_json = json.loads(response.read()) 
    
    # print the json response 
    print('\n\n This is the json file',data_json['iss_position']) 

def Lab3():
    Quit = False
    
    while(Quit != True):
        
        print("Select one of the following URL")
        case= int (input('\nPress: \n  0 for google.com \n  1 for crunchyroll.com(error) \n  2 for netflix.com \n  3 quit \n -------->\t'))

        match case:
            case 0: 
                # Making a get request 
                response = requests.get('https://google.com/') 
                # print request status_code 
                print('The status code for google.com is :',response.status_code) 
            case 1:
                # Making a get request 
                response = requests.get('https://www.crunchyroll.com/UWU-Onnichan') 
                # print request status_code 
                print('The status code for crunchyroll is :',response.status_code) 
            case 2:
                # Making a get request 
                response = requests.get('https://netflix.com/') 
                # print request status_code 
                print('The status code for netflix.com is :',response.status_code) 

            case 3: 
                # Default option 
                print('bye bye')
                Quit= True
            case other:
                print('error no valid code')


def Lab4 ():
    # Welcome message and initial list
    print('Welcome to my list menu program!!!!!\n\n')
    Mylist = ['1', '2', '4', '12']
    ExitVariable = True
    print('Original List', Mylist)

    # Menu loop
    while ExitVariable != False:
        print('What would you like to do:')
        case = int(input('  1. append an element\n  2. insert an element in the list\n  3. remove an element from the list\n  4. clear the list\n  5. reverse the list elements\n  6. Print the last element in the list\n  7. Quit\n\t-> '))

        # Switch case for menu options
        match case:
            case 1:
                # Append an element to the list
                aux = input('Add the value that you want to append\n\t-> ')
                Mylist.append(aux)

            case 2:
                # Insert an element at a specified position in the list
                while True:
                    print('Insert the position where you want to insert new value, should be between 0 & ', len(Mylist))
                    Position = int(input('\t-> '))
                    if 0 <= Position <= len(Mylist):
                        aux = input('Add the value ')
                        Mylist.insert(Position, aux)
                        break
                    else:
                        print(Position, ' is not a valid position')

            case 3:
                # Remove an element from the list
                print('Select the item that you want to delete')
                while True:
                    print(Mylist)
                    aux = input('Enter a value from the list above\t')
                    if aux not in Mylist:
                        print('Item not in the list')
                    else:
                        Mylist.remove(aux)
                        break

            case 4:
                # Clear the entire list
                Mylist = []

            case 5:
                # Reverse the order of elements in the list
                aux = []
                for i in range(0, len(Mylist)):
                    aux.append(Mylist[len(Mylist) - 1 - i])
                Mylist = aux

            case 6:
                # Print the last element in the list
                print('The last element is', Mylist[len(Mylist) - 1])

            case 7:
                # Quit the program
                ExitVariable = False

            case other:
                # Handle invalid input
                print('Non-valid option was selected')

        # Print the updated list after each operation
        print("New list:", Mylist, '\n')


def Lab5():
 
    Quit= False
    case='0'
    while Quit != True:
        #menu of the exercise
        print('Hello what would you like to do :')
        print('0. in case you want to know the names of the astronauts in the space','1. in case you want to know the altitude an latitude of ISS', '2. in cae you want to know the number of astronauts in the space', sep='\n')
        case=input('->')
        print('\n')
        match case:
            case '0':
                #In this case I'm getting the response code from this link 
                response = requests.get('http://api.open-notify.org/astros.json')
                #from that response im getting the data and put it in a library originally was json
                JsonData=response.json()
                print('The Current astronauts in the space are')
                for i in JsonData['people']:
                    print(i['name'])
                print('Awesome!!!!\n\n')
            case '1':
                #same as first link but the library is different
                response= requests.get('http://api.open-notify.org/iss-now.json')
                JsonData=response.json()
                print('The position of the ISS is')
                #print(JsonData['iss_position']['latitude'])
                print('Latitude: ',JsonData['iss_position']['latitude'], 'Longitude: ', JsonData['iss_position']['longitude'],'\n\n')
            case '2':
                response = requests.get('http://api.open-notify.org/astros.json')
                JsonData=response.json()
                print('The total number of Astronauts in the space is ', len(JsonData['people'], ))
        
            case other:

                Quit=True

def Lab5Bonus():
    #welcome banner
    print("\nWelcome to the program I'm going to create a Deck for you ")
    url = "https://www.deckofcardsapi.com/api/deck/new/"
    shuffleUrl = "https://deckofcardsapi.com/api/deck/<<deck_id>>/shuffle/?remaining=true"
    response = requests.get(url)
    Deck = response.json()
    #adding the Deck ID to not generate a new one
    shuffleUrl = shuffleUrl.replace('<<deck_id>>',Deck['deck_id'])

    while True:
        #Print the menu
        print(' \n Press 1 if you want to Shuffle the deck \n Press 2 if you want to draw cards \n Press 3 if you want to quit ')
        case = input('  --> ')
        #options of the menu
        match case:
            case '1':
                #In this case i shuffle the cards that i got from the deck by changing the ID of the link 
                response =requests.get(shuffleUrl)
                Deck = response.json()
                print('Success', Deck["shuffled"], 'Remaining cards on deck: ', Deck['remaining'], '\n')
            case '2':
                while True:
                    # Input the number of cards to draw
                    NCards = int(input('Write how many cards you want to draw\n->'))
                    # condition that valid that is enough cards in the deck
                    if 0 < NCards <= int(Deck['remaining']):
                        #cast function for concatenate later
                        NCards = str(NCards)
                        #adding how many cards do i want to the link
                        urlDraw = 'https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=' + NCards
                        #getting the final link for the response
                        urlDraw = urlDraw.replace('<<deck_id>>', Deck['deck_id'])
                        response = requests.get(urlDraw)
                        Deck = response.json()
                        break
                    else:
                        # Invalid input, prompt user to try again
                        print('No valid option, try again')

                for card in Deck["cards"]:
                    # Display the value and suit of each drawn card
                    print('--->', card["value"], card["suit"])
                    png_url = card["images"]["png"]
                    
                    # Download the PNG file
                    response = requests.get(png_url)
                    png_data = BytesIO(response.content)

                    # Read the PNG data using cv2
                    png_array = np.asarray(bytearray(png_data.read()), dtype=np.uint8)
                    img = cv2.imdecode(png_array, cv2.IMREAD_UNCHANGED)

                    # Display the PNG image using cv2
                    cv2.imshow(png_url, img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                # Print the remaining cards after drawing
                print('\nRemaining cards:', Deck['remaining'], '\n')

            case '3' :
                cv2.destroyAllWindows()
                break

            case other:
                print('Error try again \n')
    
Lab5Bonus()
