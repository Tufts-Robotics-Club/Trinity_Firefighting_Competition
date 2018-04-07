# ---------------------------------------
# Faizan Muhammad
# Trinity 2018
# Frequency Stimuli Code
# Keeps looping till a certain frequency
# is discovered and then exits
# ---------------------------------------

import pyaudio
import wave
import numpy as np


CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
TARGET_MIN_FREQ = 14900
TARGET_MAX_FREQ = 15100

window = np.blackman(CHUNK)
p = pyaudio.PyAudio()

SWIDTH = p.get_sample_size(FORMAT)

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

data = stream.read(CHUNK, exception_on_overflow = False)
while len(data) == CHUNK*SWIDTH:
	# unpack the data and times by the hamming window
	indata = np.array(wave.struct.unpack("%dh"%(len(data)/SWIDTH),\
	                                     data))*window
	# Take the fft and square each value
	fftData=abs(np.fft.rfft(indata))**2
	# find the maximum
	which = fftData[1:].argmax() + 1
	# use quadratic interpolation around the max
	if which != len(fftData)-1:
	    y0,y1,y2 = np.log(fftData[which-1:which+2:])
	    x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
	    # find the frequency and output it
	    thefreq = (which+x1)*RATE/CHUNK
	    print "The freq is %f Hz." % (thefreq)
	else:
	    thefreq = which*RATE/CHUNK
	    print "The freq is %f Hz." % (thefreq)

	# check if reached target frequency
	if (thefreq <= TARGET_MAX_FREQ) and (thefreq >= TARGET_MIN_FREQ):
		print "The freq %f Hz is within target." % (thefreq)
		print "Exiting"
		break
	# read some more data
	data = stream.read(CHUNK, exception_on_overflow = False)
 
stream.stop_stream()
stream.close()
p.terminate()