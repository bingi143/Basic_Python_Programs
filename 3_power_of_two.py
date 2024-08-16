'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-08 18:00:30
@Title : Python Program power of 2

'''


def power_two_method(power_value):
    '''
          Description: 
                this function is getting power of 2
          Parameters: 
                power_value: taking the power value
          Return : 
                this function not returning any thing
    '''
    if(0<=power_value<31):
        for i in range(1,power_value):
            v=1
            for k in range(i):
                v=v*2
            print(2,"^",i,"=",v)


def main():
    power_value=int(input("Enter Power value:"))
    power_two_method(power_value)


if __name__=="__main__":
    main()