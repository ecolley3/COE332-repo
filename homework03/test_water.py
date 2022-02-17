import json
import math
from typing import List
import logging
import socket
format_str=f'%(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format_str)

def current_turbidity(dict_list: List[dict], cal: str, detect: str, i: int) -> float:
     a0 = float(dict_list[i][cal])
     I90 = float(dict_list[i][detect])
     T = a0 * I90
     return(T)
     """Finds Turbidity
     Args:
         cal: calibration key to find turbidity
         detect: detector key in dictionary
         i: iteration integer

     Returns:
         Turbidity value based on values inputed, value is a float
     """

def calc_time(T: float) -> bool:
     b = 0
     Ts = 1.0
     d = 0.02
     T0 = T
     b = math.log((1/T0),0.98)
     if (Ts > T0*((1-d)**b)):
         logging.info('Turbidity is below threshold for safe use')
         print(f'Minimum time required to return below a safe threshold = {b} hours')
     else:
         logging.warning('Turbidity is above threshold for safe use')
         print(f'Minimum time required to return below a safe threshold = 0 hours')
     return(b)
     """Calculates time left until water is below a safe threshold

     Args:
         T: float turbidity value from current turbidity function as a bool
         
     Returns:
         That turbidity is safe and amount of time until it is below a safe threshold or that turbidity is not safe
     """
     
def main():
     with open('turbidity_data.json', 'r') as f:
         t_data = json.load(f)
     T_list = 0
     x = 0
     for i in range(1,6):
         x = len(t_data['turbidity_data'])- i
         T = current_turbidity(t_data['turbidity_data'], 'calibration_constant', 'detector_current', x)
         T_list += T
     print(f'Average turbidity based on most recent five measurements = {T_list/5} NTU')
     Time = calc_time(T)



if __name__ == '__main__':
     main()
