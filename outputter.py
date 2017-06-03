def main():
    num1 = 1
    num2 = 2
    temp = 0
    evenTotal = 0

    recurseFib(num1,num2,temp,evenTotal)




def recurseFib(num1,num2,temp,evenTotal):
    print("{}".format(num1))
    temp = num1 + num2
    if ((temp <= 4000000) and (temp % 2 == 0)): #if the curTotal is even
        evenTotal += temp
    num1 = num2
    num2 = temp

    if (num2 <= 4000000):
        recurseFib(num1,num2,temp,evenTotal)





if __name__ == "__main__":
    main()

    #calls main
