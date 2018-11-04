#author: Ruairí Brady (ruairi.brady@ucdconnect.ie)

#importing libraries
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
get_ipython().run_line_magic('matplotlib', 'inline')

#loading voltages
V = np.loadtxt('ft_bluelaser1.txt')
V = np.array(V)
N = 1024
r = 1/40

#loading velocities
vel = np.loadtxt("velocity_blue.txt")
t1 = vel[:,0]
x1 = vel[:,1]*1E+6
t2 = vel[:,2]
x2 = vel[:,3]*1E+6

#velocities calculation
x_diff = x1-x2
t_diff = t2-t1
vel = x_diff/t_diff
mean_vel = np.mean(vel)

#velocities error
delt_x = 0.01*1E+6
delt_t = 0.5
v_err = vel*((delt_x/x_diff)**2+(delt_t/t_diff)**2)
mean_v_err = np.mean(v_err)
print('The velocity of the motor is: {0:.5}'.format(mean_vel), '± {0:.2}'.format(mean_v_err), 'nm/s')

#sampling path interval
delt_x = 2*mean_vel*r
delt_x_err = 2*mean_v_err*r
print('The voltage of the incident ray is measured every {0:.4}'.format(delt_x), "± {0:.1}".format(delt_x_err), 'nm')

#raw interferogram signal
plt.plot(V)
plt.xticks([])
plt.yticks([])
plt.axis([0,1024,-8.2,-7.3])
plt.xlabel('Path Difference')
plt.ylabel('Relative Intensity')
plt.savefig('blue_interferogram.png')

#raw fast fourier transform sliced and made absolute
V_FFT=(np.abs(np.fft.fft(V))[0:512])
V_FFT=np.delete(V_FFT,[0])
norm_int=V_FFT/max(V_FFT)
loc=np.argmax(norm_int)

i=np.linspace(0,0.5*N,0.5*N)
i=np.delete(i,[0])
lambda_i = N*delt_x/i
lambda_i_err = N*delt_x_err/i

plt.plot(lambda_i,norm_int,label='Blue Laser\n1024 points')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalised Intensity')
plt.grid(True)
plt.axis([150,750,0,1.1])
plt.legend(bbox_to_anchor=(0.65, 0.95), loc=2, borderaxespad=0.)
plt.savefig('blue_spectrogram.png')

print('The peak wavelength of the Blue Laser = {0:.5}'.format(lambda_i[loc]),'± {0:.3}'.format(lambda_i_err[loc]), 'nm')

