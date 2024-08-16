'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program calculating interest

'''


class Payment:
    @staticmethod
    def monthly_payment(principal,years,rate):
         '''
          Description: 
                this function is calucating interest
          Parameters: 
                principal: original amout
                years: how many years
                rate : rate of interest
          Return : 
                this function returing total amount
        '''
         months=12*years
         interest=rate//(12*100)
         p=principal*interest//1-(1+interest)^(-months)
         return p
    

def main():
    principal = int(input("Enter amount:"))
    years = int(input("Enter years:"))
    rate_of_interest=int(input("Enter interast rate:"))
    #payments=Payment()
    print(Payment.monthly_payment(principal,years,rate_of_interest))


if __name__=="__main__":
    main()