# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:48:44 2022

@author: rkatw
"""
import numpy as np


import numpy as np
import matplotlib.pyplot as plt
import module_aud_student as aud
import module_dsp_student as dsp
from scipy.signal import hilbert
import time

st = time.time()

# File naam
wav_file_in = 'opdr1.wav'

# Inlezen van wav-bestand
f_rate, wav_data_stereo = aud.read_wav( wav_file_in )

# Mono maken
x = aud.stereo2mono(wav_data_stereo)

# Tijd-as (in seconden) maken
Nt = np.size(x,0)
t  = np.arange(Nt) / f_rate

# Bepalen van de envelope
x_env = np.abs( hilbert(x) )

f = 6.9  # cuttofffrequencie in hertz

def low_pass (x, f, rate):
    f_index = int(f * x.size / rate)
    f_x =  np.fft.fft(x)
    
    for i in range(f_index + 1, len(x)):
        f_x[i] = 0
        
    x_filter = np.fft.ifft(f_x)
    
    return np.real(x_filter)

x_filter = low_pass(x_env, f, 10000)

plt.figure()
plt.plot(t, x_filter)
plt.show()

end = time.time()
print('time elapsed =', end-st, 's')