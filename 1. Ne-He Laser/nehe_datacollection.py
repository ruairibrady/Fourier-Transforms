#importing libraries
import matplotlib.pyplot as plt
import numpy as np
from pydaqmx_helper.adc import ADC
% matplotlib inline

#data run
myADC=ADC()
myADC.addChannels([0], minRange=-10, maxRange=5)
val = myADC.sampleVoltages(512,20)

#saving data
np.savetxt('ft_redlaser.txt',val[0],delimiter='')
