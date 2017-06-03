def main():
    num1 = 1
    num2 = 2
    temp = 0
    evenTotal = 2

    recurseFib(num1,num2,temp,evenTotal)




def recurseFib(num1,num2,temp,evenTotal):

    temp = num1 + num2
    if ((num2 <= 4000000) and (temp % 2 == 0)): #if the curTotal is even
        evenTotal += temp

    if (num2 <= 4000000):
        num1 = num2
        num2 = temp
        recurseFib(num1,num2,temp,evenTotal)

    print("{}".format(evenTotal))



if __name__ == "__main__":
    main()

    #calls main
