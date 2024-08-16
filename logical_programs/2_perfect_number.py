'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program perfect number or not

'''


def perfect_number_method(number):
    '''
          Description: 
                this function is perfect number or not
          Parameters: 
                number: number
          Return : 
                this function not returning any thing
    '''
    sum=0
    #Number_Copy=Number
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
    if number%sum==0:
        print("Given number is Perfect Number")
    else:
        print("Given Number is not a Perfect number")


def main():
    number=int(input("Enter Number:"))
    perfect_number_method(number)


if __name__=="__main__":
    main()