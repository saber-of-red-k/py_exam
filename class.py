class Shape():
    def __init__(self,area,hekef):
        self.__area = area
        self.__hekef = hekef
    def __str__(self):
        return f'area ob object is {self.__area}, hekef of object is {self.__hekef}'
    def __repr__(self):
        return f'Area : {self.__area}, hekef: {self.__hekef}'

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self,value):
        if value >=0:
            self.__area = value

    @property
    def hekef(self):
        return self.__hekef

    @hekef.setter
    def hekeg(self,value):
        if value >=0:
            self.__hekef = value