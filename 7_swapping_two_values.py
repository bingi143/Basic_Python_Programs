'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program swapping two values

'''


def swap_method(number_1,number_2):
    '''
          Description: 
                this function is swapping two values
          Parameters: 
                number1: taking the value
                number2: taking the second value
          Return : 
                this function not returning any thing
    '''
    print("Before Swappint Number_1 Value is:",number_1)
    print("Before swapping Number_2 Value is:",number_2)
    number_3=number_1+number_2 #We are storing both values in another variable 
    number_1=number_3-number_1
    number_2=number_3-number_1
    print("After Swapping Number_1 Vales:",number_1)
    print("After Swapping Number-2 value is:",number_2)


def main():
    number_1=int(input("Enter First Number:"))
    number_2=int(input("Enter Second :"))
    swap_method(number_1,number_2)


if __name__=="__main__":
    main()