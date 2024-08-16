'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is converting binary values

'''


class Binary:
    @staticmethod
    def binary_conversion(number):
        '''
          Description: 
                this function is converting binary values
          Parameters: 
                number : integer value
          Return : 
                this function returing binary value
        '''

        if number<0:
            raise ValueError("Enter Positive number")
        Resutlt=bin(number)[2:]
        Final_result=Resutlt.zfill(32) #padding is 4 bytes=32bits
        return Final_result
    

def main():
    Number=int(input("Enter number:"))
    result=Binary.binary_conversion(Number)
    print(result)


if __name__=="__main__":
    main()
    