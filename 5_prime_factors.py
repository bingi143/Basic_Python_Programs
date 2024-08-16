'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-08 18:00:30
@Title : Python Program prime factors

'''


def Prime_Factors(number):
    '''
          Description: 
                this function is getting prime factors of a number
          Parameters: 
                number: taking the number 
          Return : 
                this function is not returning any thing
    '''
    for i in range(2,number):
        if number%i==0:
            c=True
            for k in range(2,i//2+1):
                if i%k==0:
                    c=False
            if(c):
                print(i)


def main():
    number=int(input("Enter number:"))
    Prime_Factors(number)


if __name__=="__main__":
    main()