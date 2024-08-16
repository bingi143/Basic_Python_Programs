'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program prime number

'''


def prime_number(number):
    '''
          Description: 
                this function is perfect number or not
          Parameters: 
                number: number
          Return : 
                this function not returning any thing
    '''
    c=0
    for i in range(2,(number//2+1)):
         if number == 1:
              continue
         if number%i==0:
             c=c+1
             print("Given number is not prime number")
             break
    if(c==0):
        print("Given number is prime nubmer")


def main():
    number=int(input("Enter Number:"))
    prime_number(number)


if __name__=="__main__":
    main()