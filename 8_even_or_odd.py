'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-08 18:00:30
@Title : Python Program even or odd

'''


def even_or_odd_method(number):
     '''
          Description: 
                this function is getting even or odd given number
          Parameters: 
                number: taking number as parameter
          Return : 
                this function not returning any thing
    '''
     if(number%2==0):
         print("Given number is even")
     else:
         print("Given Number is odd")


def main():
    number=int(input("Enter number:"))
    even_or_odd_method(number)


if __name__=="__main__":
    main()