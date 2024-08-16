'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-08 18:00:30
@Title : Python Program DocString Structure

'''


def leap_year(year):
     '''
          Description: 
                this function is getting given year leap year or not
          Parameters: 
                year: year taking as parameter
          Return : 
                this function not returning any thing
    '''
     if(year<=999):
         print("Enter Four Digit number")  #Based on given program want only four digit number
         return
     if(year%4==0):
         if(year%100!=0):
             if(year%400==0):
                 print(year,"is leap year")
             else:
                 print(year,"is a leap year")
         else:
             print(year,"is not leap year")
     else:
         print(year,"is not leap year")


def main():
    year=int(input("Enter Year:"))
    leap_year(year)


if __name__=="__main__":
    main()
