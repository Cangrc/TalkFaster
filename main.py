#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:10:45 2019

@author: cangrc2
"""
#http://samcarcagno.altervista.org/blog/basic-sound-processing-python/?doing_wp_cron=1548107046.9890239238739013671875
#Extract audio from video using below ccode
#ffmpeg -i Obama.mp4 -vn -acodec copy output-audio.aac
#ffmpeg -i Obama.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav

from pylab import *
from scipy.io import wavfile
from numpy import arange, where, delete
from matplotlib import pyplot as plt

#sampFreq, snd = wavfile.read('Obama.wav')
ampFreq, snd = wavfile.read('440_sine.wav')

snd.dtype

snd = snd / (2.**15)
s1 = snd[:,0] 

#timeArray = arange(0, s1.size, 1)
#timeArray = timeArray / sampFreq
#timeArray = timeArray * 1000  #scale to milliseconds

#plt.plot(timeArray, s1, color='k')
#plt.ylabel('Amplitude')
#plt.xlabel('Time (ms)')

temp = s1
index = where(s1==0)
res = delete(temp, index)

#timeArray = arange(0, res.size, 1)
#timeArray = timeArray / sampFreq
#timeArray = timeArray * 1000  #scale to milliseconds

#plt.plot(timeArray, res, color='k')
#plt.ylabel('Amplitude')
#plt.xlabel('Time (ms)')

n = len(s1) 
p = fft(s1) # take the fourier transform 

nUniquePts = int(ceil((n+1)/2.0))
p = p[0:nUniquePts]
p = abs(p)

p = p / float(n) # scale by the number of points so that
                 # the magnitude does not depend on the length 
                 # of the signal or on its sampling frequency  
p = p**2  # square it to get the power 

# multiply by two (see technical document for details)
# odd nfft excludes Nyquist point
if n % 2 > 0: # we've got odd number of points fft
    p[1:len(p)] = p[1:len(p)] * 2
else:
    p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft

freqArray = arange(0, nUniquePts, 1.0) * (sampFreq / n);
plt.plot(freqArray/1000, 10*log10(p), color='k')
plt.xlabel('Frequency (kHz)')
plt.ylabel('Power (dB)')

