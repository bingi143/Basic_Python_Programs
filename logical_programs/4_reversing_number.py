'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program reverse of given number

'''


def reversing_number_method(number):
    '''
          Description: 
                this function is reversing a given number
          Parameters: 
                number: number 
          Return : 
                this function not returning any thing
    '''
    reverse=0
    while number>0:
        remainder=number%10
        reverse=reverse*10+remainder
        number=number//10
    print("Reverse of the Number is",reverse)


def main():
    number=int(input("Enter Number:"))
    reversing_number_method(number)


if __name__=="__main__":
    main()