'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program stop watch

'''


import time
class StopWatch:
    def __init__(self):
        self.Start = None
        self.Stop = None
    

    def Start_time(self):
         '''
          Description: 
                this function is getting start the time
          Parameters: 
                self : instance  
          Return : 
                this function not returning returning 
        '''
         self.Start=time.time()
         print("Stop watch Started ")


    def Stop_time(self):
         '''
          Description: 
                this function is stop the timer
          Parameters: 
                number: instence
          Return : 
                this function not returning  any thing
        '''
         self.Stop=time.time()
         elapsed=self.Stop-self.Start
         print("Elapsed time is",elapsed)
stopwatch=StopWatch()


def main():
    print("Press Enter Button 1 to start")
    i=int(input())
    if i==1:
        stopwatch.Start_time()
    print("Press enter Button 0 to stop")
    k=int(input())
    if k==0:
        stopwatch.Stop_time()

    
if __name__=="__main__":
    main()