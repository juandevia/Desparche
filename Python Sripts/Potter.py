import requests
from io import BytesIO
import cv2
import numpy as np

#get the characters that have patronus
#get information of the cahrapter


def CharacterList(dataJson):
    characterList=[]
    for character in dataJson:
        if(character['image'] != ''):
            characterList.append(character['name'])
    return characterList

def menu(characterList):
    for i in range(len(characterList)):
        print(i,') ', characterList[i], sep='')


def getId2(dataJson,name):
    info={}
    for i in dataJson:
        if(i['name'] == name):
            info = i
            return info
        
def getId(dataJson,name):
    info={}
    for i in dataJson:
        print(i['name'])
        if(i['name'] == name):
            print(i['name'])
            info=i
            return info
        else:
            return 0
     
def printDict(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, list):
            # If the value is a list, join its elements into a string
            value = ", ".join(map(str, value))
        print(f"{key}: {value}")

def imageVisual(link):
    # Download the image link
    response = requests.get(link)
    Image_data = BytesIO(response.content)

    # Read the JPEG data using cv2
    jpg_array = np.asarray(bytearray(Image_data.read()), dtype=np.uint8)
    img = cv2.imdecode(jpg_array, cv2.IMREAD_COLOR)  # Use cv2.IMREAD_COLOR for JPEG

    #cv2.startWindowThread()

    # Display the JPEG image using cv2
    cv2.namedWindow("image")
    cv2.imshow('image', img)
    cv2.waitKey(0) # close window when a key press is detected
    cv2.destroyWindow('image')
    cv2.waitKey(1)


def main():
    #getting the response from the link
    response = requests.get('https://hp-api.onrender.com/api/characters')
    #getting the data in json format
    dataJson = response.json()
    characterList= CharacterList(dataJson)
    x = False
    y = 'a'

    #this is going to repeat until the users want to stop
    while(y != 'q'):
        

        while(True):
            
            try :
                print('type a number that match the charapter that you want to know more about it')
                #this displays the menu
                menu(characterList)
                userInput=int(input('-->\t'))
                if (userInput >= 0 and userInput < len(characterList)):
                    break
                else:
                    print('no valid option')
            except:
                print('wrong input')
        
        name=characterList[userInput]
        info=getId2(dataJson,name)
        printDict(info)
        imageVisual(info['image'])
        y =input('If you want to stop type q otherwise type any other key---> ')

main()




        
