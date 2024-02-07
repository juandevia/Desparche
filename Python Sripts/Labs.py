from urllib.request import urlopen 
import json
import requests

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
    print('Welcome to my list menu program!!!!!\n\n')
    Mylist=['1','2','4', '12']
    ExitVariable=True
    print('Original List', Mylist)
    while(ExitVariable != False):
        print('What would you like to do:')
        case=int(input('  1. append an element\n  2. insert an element in the list\n  3. remove an element from the list\n  4. clear the list\n  5. reverse the list elements\n  6. Print the last element in the list\n  7. Quit\n\t-> '))

        match case:
            case 1:
                aux=input('Add the value that you want to append\n\t-> ')
                Mylist.append(aux)
                
            case 2:
                while True:
                    print('Insert the position where you want to insert new value, should be between 0 & ', len(Mylist))
                    Position=int(input('\t-> '))
                    if Position >= 0 and Position <= len(Mylist):
                        aux=input('Add the value ')
                        Mylist.insert(Position,aux)
                        
                        break
                    else:
                        print(Position,' is No a valid position')
            case 3:
                print('Select the item that you want to delete')
                while True:
                    print(Mylist)
                    aux=input('Enter a value of the list above\t')
                    if not aux in Mylist:
                        print('Item not in the list')
                    else:
                        Mylist.remove(aux)
                        break
            case 4:
                Mylist = []
            
            case 5:
                aux = []
                for i in range(0, len(Mylist)):
                    aux.append(Mylist[len(Mylist) - 1 - i])
                Mylist=aux
            case 6:
                print('The last element is', Mylist[len(Mylist)-1])

            case 7:
                ExitVariable=False
                

            case other:
                print('non valid option was selected')

        print("New list :", Mylist,'\n') 


def Lab5():
 
    Quit= False
    case='0'
    while Quit != True:
        print('Hello what would you like to do :')
        print('0. in case you want to know the names of the astronauts in the space','1. in case you want to know the altitude an latitude of ISS', '2. in cae you want to know the number of astronauts in the space', sep='\n')
        case=input('->')
        print('\n')
        match case:
            case '0':
                response = requests.get('http://api.open-notify.org/astros.json')
                JsonData=response.json()
                print('The Current astronauts in the space are')
                for i in JsonData['people']:
                    print(i['name'])
                print('Awesome!!!!\n\n')
            case '1':
                response= requests.get('http://api.open-notify.org/iss-now.json')
                JsonData=response.json()
                print('The position of the ISS is')
                #print(JsonData['iss_position']['latitude'])
                print('Latitude: ',JsonData['iss_position']['latitude'], 'Longitude: ', JsonData['iss_position']['longitude'],'\n\n')
            case '2':
                response = requests.get('http://api.open-notify.org/astros.json')
                JsonData=response.json()
                print('The total number of Astronauts in the space is ', len(JsonData['people']))
        
            case other:

                Quit=True

Lab5()