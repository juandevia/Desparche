import requests

def joke():
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    dataJson=response.json()

    while True:
        response = requests.get('https://icanhazdadjoke.com/', headers=headers)
        dataJson=response.json()
        c=input('\ntype any key to get a joke, type q to exit: \n')
        if c != 'q':
            print('--> ',dataJson['joke'],'\n')
        else:
            break

joke()



