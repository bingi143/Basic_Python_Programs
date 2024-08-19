'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-08 18:00:30
@Title : Python Program head tails percentage

'''


import random
def head_tails_percentage(number):
    '''
          Description: 
                this function is getting head tails percentage
          Parameters: 
                number: taking number as parameter
          Return : 
                this function not returning any thing
    '''
    if(number<=0):
        return "Enter Positive number"
    Head=0
    Tail=0
    for i in range(1,number):
        v=random.random()
        if(v<0.5):
            Tail=Tail+1
        elif(v<1):
            Head=Head+1
        Heads_Percentage=Head/number*100
        Tails_Percentage=Tail/number*100
        return Heads_Percentage,Tails_Percentage
    

def main():
    number=int(input("Enter number:"))
    Heads_Percentage,Tails_Percentage=head_tails_percentage(number)
    print("Heads Percentage is :",Heads_Percentage)
    print("Tails percentage is :",Tails_Percentage)

    
if __name__=="__main__":
    main()
