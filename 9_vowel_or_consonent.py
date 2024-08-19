'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program identify vowel or consonent

'''


def vowel_or_consonent(char_):
    '''
          Description: 
                this function is identify vowel or consonent
          Parameters: 
                ch : taking charecter
          Return : 
                this function not returning any thing
    '''
    char_=char_.lower()
    if(char_=='a'or char_=='e' or char_=='i' or char_=='o' or char_=='u'):
        print("given Character is Vowel")
    else:
        print("Given Character is consonent")

    
def main():
    char_='g'
    vowel_or_consonent(ch)


if __name__=="__main__":
    main()
