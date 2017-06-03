def main():

    curNum = 0

    for num in range (1,1000):

        if(doesItMod(num) == True):

            curNum += num

            print("{}".format(curNum))



def doesItMod( num ):

    if ( (num % 3) == 0 or (num % 5) == 0 ):

        return True

    else:

        return False


#programme starts here

if __name__ == "__main__":

    main()

    #calls main
