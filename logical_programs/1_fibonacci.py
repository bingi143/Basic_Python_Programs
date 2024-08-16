'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program printing fibonacci series

'''


def fibonaci_method(number):
    '''
          Description: 
                this function printing fiboonacci series
          Parameters: 
                number: number of fibonacci series
          Return : 
                this function not returning any thing
    '''
    a=0
    print(a)
    b=1
    print(b)
    for i in range(2,number):
        c=a+b
        print(c,end=",")
        a=b
        b=c


def main():
    number=int(input("Enter How many Fibonacci Series :"))
    fibonaci_method(number)


if __name__=="__main__":
    main()