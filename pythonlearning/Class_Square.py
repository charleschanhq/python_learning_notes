class Square:
    def __init__(self,height='0',width='0'):
        self.height= height
        self.width=width
    @property
    def height(self):
        #print("retrieving the Height")

        return self.__height
    @height.setter
    def height(self,value):

        if value.isdigit():
            self.__height= value
        else:
            print("please only enter numbers for height")

    @property
    def width(self):
        print("retrieving the Height")

        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print("please only enter numbers for width")


    def getArea(self):
        return int(self.__width)*int(self.__height)





def main():



    aSquare=Square()

    height=input('enter the height')
    width=input("enter the width")

    aSquare.height=height
    aSquare.width=width
    print(aSquare.height)
    print(aSquare.width)
    print(aSquare.getArea())
main()
