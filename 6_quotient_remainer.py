'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program quotient remainder method

'''


def quotient_remainder_method(number_1,number_2):
    '''
          Description: 
                this function is getting quotient remainder
          Parameters: 
                number1: taking the value
                number2: taking the second value
          Return : 
                this function not returning any thing
    '''
    quotient=number_1 / number_2
    remainder=number_1 % number_2
    print(quotient,"Quotient")
    print(remainder,"Reminder")


def main():
    number_1=int(input("Enter number 1 :"))
    number_2=int(input("Enter Number 2:"))
    quotient_remainder_method(number_1,number_2)


if __name__=="__main__":
    main()