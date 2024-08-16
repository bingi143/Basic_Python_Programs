'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program coupon number

'''


import random
def generate_random(number):
    '''
          Description: 
                this function is getting random number
          Parameters: 
                number: number 
          Return : 
                this function  returning a random number
    '''
    return random.randint(1,number)


def coupon_number_method(number):
    '''
          Description: 
                this function is getting coupon number
          Parameters: 
                number: number 
          Return : 
                this function returning total attempts
    '''
    collect_coupon=set()
    attempts=0
    while len(collect_coupon)<number:
        coupon=generate_random(number)
        collect_coupon.add(coupon)
        attempts=attempts+1
    return attempts


def main():
    number=int(input("Enter Number:"))
    print(coupon_number_method(number))


if __name__=="__main__":
    main()