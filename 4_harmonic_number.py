'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-08 18:00:30
@Title : Python Program harmonic number

'''


def harmonic_number(number):
     '''
          Description: 
                this function is getting harmonic number
          Parameters: 
                number: taking the power value
          Return : 
                this function not returning any thing
    '''
     if number==0:
          print("number can not be zero")
     sum=0
     for i in range(1,number+1):
         sum=sum+1/i
     print("Nth harmonic value is:",sum)


def main():
     number=int(input("Enter number:"))
     harmonic_number(number)


if __name__=="__main__":
    main()