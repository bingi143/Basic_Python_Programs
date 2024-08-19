'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program is converting binary values

'''


def binary_convertion(number):
    '''
          Description: 
                this function is converting binary values
          Parameters: 
                number : integer value
          Return : 
                this function returing binary value
        '''
    return bin(number)


def nibbles(number):
    '''
          Description: 
                this function is converting nible
          Parameters: 
                number : integer value
          Return : 
                this function returing nible
        '''
    return ((number & 0x0F) << 4) | ((number & 0xF0) >> 4)


def power(number):
    '''
          Description: 
                this function is power of value
          Parameters: 
                number : integer value
          Return : 
                this function returing power of given value
        '''
    p=1
    for i in range(1,number):
        p=p*2
    return p


def main():
    number=int(input("Enter Number:"))
    result=binary_convertion(number)
    swap_nibbles=nibbles(number)
    final_result=binary_convertion(swap_nibbles)
    print("before swapping niblles",swap_nibbles)
    print("after swappint nubbles",final_result)
    power_two=power(number)
    print("Number is power of 2 value is ",power_two)


if __name__=="__main__":
    main()