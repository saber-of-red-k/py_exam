import json
import requests

#POST CLASS#
class Post():
    def __init__(self,userId, id, title, body):
        self.__userId = userId
        self.__id = id
        self.__title = title
        self.__body = body
    def __str__(self):
        return f'userId: {self.__userId}\n id: {self.__id}\n title: {self.__title}\n body: {self.__body}'

    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, other):
        if other > 0:
            self.__userId = other

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, other):
        if other > 0:
            self.__id = other

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, other):
        self.__title = other

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, other):
        self.__body = other

#MAIN BODY#

response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{1}")      #initialize response to start work
while True:
    userInp = input('Please enter post ID to display (non number for exit) : ')          #user input
    try:
        id_inp = int(userInp)                                                   #try to make int, if error - exit
    except:
        print('Exiting, thank you!')
        break

    if id_inp > 0 and response.status_code == 200:                              #if id > 0 and post is found
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id_inp}")         #change response to actual input choosing
        dict = json.loads(response.content)                                                     #send json to dictionary

        new_post = Post(dict.get("userId"),dict.get("id"),dict.get("title"),dict.get("body"))   #create object from dict
        print(new_post)                                                                         #and print it via __str__
    else:
        print('Wrong input or post not found, try again.')                                      #if some error (ex. negative number of post not found - continue)
        continue