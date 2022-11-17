# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:42:27 2022

@author: rkatw
"""
import numpy as np
import matplotlib.pyplot as plt
import module_aud_student as aud
import module_dsp_student as dsp
from scipy.signal import hilbert
from scipy.signal import find_peaks
import time            

## code cel om ongewenste frequentie te bepalen.
# File naam
wav_file_in = 'opdr2_tones_present.wav'

# Inlezen van wav-bestand
f_rate, wav_data_stereo = aud.read_wav( wav_file_in )

# Mono maken
x = aud.stereo2mono(wav_data_stereo)

# Tijd-as (in seconden) maken
Nt = np.size(x,0)
t  = np.arange(Nt) / f_rate
freq = np.arange(Nt)
# Bepalen van de envelope
x_env = np.abs( hilbert(x) )

f = 10  # cuttofffrequencie in hertz

rate = 441000
fft_f_index = int(f * len(x) / rate)
fft_x =  np.fft.fft(x)

hoogte = 1*10**8
peak = find_peaks(fft_x, height=hoogte)
peak_values = peak[0]


def fft_filter (x, f, rate):
    f_index = int(f * x.size / rate)
    f_x =  np.fft.fft(x)
    
    for i in range(f_index + 1, len(x)):
        f_x[i] = 0
        
    x_filter = np.fft.ifft(f_x)
    
    return np.real(x_filter)

x_filter = fft_filter(x, f, 10000)
