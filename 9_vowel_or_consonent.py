'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program identify vowel or consonent

'''


def vowel_or_consonent(ch):
    '''
          Description: 
                this function is identify vowel or consonent
          Parameters: 
                ch : taking charecter
          Return : 
                this function not returning any thing
    '''
    ch=ch.lower()
    if(ch=='a'or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print("given Character is Vowel")
    else:
        print("Given Character is consonent")

    
def main():
    ch='g'
    vowel_or_consonent(ch)


if __name__=="__main__":
    main()