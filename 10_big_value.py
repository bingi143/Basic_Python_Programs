'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program identify biggest value in three numbers

'''


def large_val_method(number_1,number_2,number_3):
    '''
          Description: 
                this function is identify which one is bigger
          Parameters: 
                ch : taking charecter
          Return : 
                this function not returning any thing
    '''
    if(number_1>number_2 and number_1>number_3):
        print(number_1," is Big value")
    elif(number_2>number_1 and number_2>number_3):
        print(number_2,"is Big Value")
    else:
        print(number_3," is Big Value")


def main():
    number_1=int(input("Enter First Number:"))
    number_2=int(input("Enter secomd Number:"))
    number_3=int(input("Enter First Number:"))
    large_val_method(number_1,number_2,number_3)


if __name__=="__main__":
    main()