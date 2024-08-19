'''

@Author: Venkatesh
@Date: 2024-08-16 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-16 18:00:30
@Title : Python Program convering tempurature

'''


class Temperature:
    @staticmethod
    def temperature_conversion(temperature, to_scale):
        '''
          Description: 
                this function is getting day of week
          Parameters: 
                tempurature: integer value 
                to_scale: which scale to convert
          Return : 
                this function returning after converted tempurature
        '''
        if to_scale.lower() == 'celsius':
            return (temperature - 32) * 5 / 9
        elif to_scale.lower() == 'fahrenheit':
            return (temperature * 9 / 5) + 32
        else:
            raise ValueError("to_scale must be either 'Celsius' or 'Fahrenheit'")
        

def main():
    temperature=int(input("Enter Temperature:"))
    to_scale=str(input("Eneter celsius Or fehrenheit:"))
    print(Temperature.temperature_conversion(temperature,to_scale))


if __name__=="__main__":
    main()
