#author: Ruairí Brady (ruairi.brady@ucdconnect.ie)

#importing libraries
import matplotlib.pyplot as plt
import numpy as np
from pydaqmx_helper.adc import ADC
% matplotlib inline

#data run
myADC=ADC()
myADC.addChannels([0], minRange=-10, maxRange=5)
val = myADC.sampleVoltages(1024,40)

#saving data
np.savetxt('ft_greenlaser2.txt',val[0],delimiter='')
