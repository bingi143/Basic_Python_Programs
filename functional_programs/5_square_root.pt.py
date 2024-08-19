'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program on squar root of number

'''


class Square:
    @staticmethod
    def newton_method(number):
        '''
          Description: 
                this function is square root
          Parameters: 
                number : integer value
          Return : 
                this function returing square root value
        '''
        if number<0:
            raise ValueError("not possible with negative number")
        t=number
        epsilon=1e-15
        while abs(t-number/t)>epsilon*t:
            t=(number/t+t)/2.0
        return t
    

def main():
    Number=int(input("Enter Number:"))
    result=Square.newton_method(Number)
    print(result)


if __name__=="__main__":
    main()