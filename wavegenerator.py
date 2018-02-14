#!/usr/bin/python
import numpy as np
from scipy import signal
import wave
import struct
import sys

num_samples = 48000
sampling_rate = 48000.0
amplitude = 16000
comptype = 'NONE'
compname = 'not compressed'
nchannels = 1
sampwidth = 2
FILE_NAME = ''

def createSine(frequency, play_time):
    # generate the sine wave
    new_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples * play_time)]
    writeWave(new_wave)

def createSaw(frequency, play_time):
    saw_wave = [signal.waveforms.sawtooth(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples * play_time)]
    writeWave(saw_wave)

def createTriangle(frequency, play_time):
    new_wave = [signal.waveforms.sawtooth(2 * np.pi * frequency * x/sampling_rate, 0.5) for x in range(num_samples * play_time)]
    writeWave(new_wave)

def createSquare(frequency, play_time):
    new_wave = [signal.waveforms.square(2 * np.pi * frequency * x/sampling_rate, 0.5) for x in range(num_samples * play_time)]
    writeWave(new_wave)

def createWave(frequency, wave_type, play_time):
    if wave_type == 'sine':
        createSine(frequency, play_time)
    elif wave_type == 'saw':
        createSaw(frequency, play_time)
    elif wave_type == 'triangle':
        createTriangle(frequency, play_time)
    elif wave_type == 'square':
        createSquare(frequency, play_time)
    else:
        print('Please type in only waveforms from this list! (sine, saw, triangle, square)')

def writeWave(created_wave):
    file = FILE_NAME
    nframes = num_samples
    wav_file = wave.open(file, 'w')
    wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
    for s in created_wave:
        # struct.pack with the parameter 'h' means that we're
        # writing the data as binaries, not just the numbers.
        # 'h' stands for hexadecimal.
        # This allows for music players to read the data.
        wav_file.writeframes(struct.pack('h', int(s*amplitude)))

def printSuccessful(wave_type, frequency, play_time):
    print('File \'' + FILE_NAME + '\' created!\n' +
      'Wave Type: ' + wave_type + '\n' +
      'Frequency: ' + frequency + "hz\n"+
      'Play Time: ' + play_time + ' seconds')


def main(wave_type, frequency, play_time, file_name):
    frequency_Float = float(frequency)
    wave_type_Str = str(wave_type)
    play_time_Int = int(play_time)
    file_name = str(file_name)
    global FILE_NAME
    if len(file_name) < 4:
        print('your specified filename: \'' + file_name + '\' is too short. The file name must end in \'.wav\'.\n Do you want me to change your file name to end in \'.wav\'? (y/n)')
        answer = input()
        if answer == 'y':
            FILE_NAME = file_name + '.wav'
            createWave(frequency_Float, wave_type_Str, play_time_Int)
            printSuccessful(wave_type, frequency, play_time)
        elif answer == 'n':
            print('Please press a key to exit.')
            input()
    else:
        FILE_NAME = file_name
        createWave(frequency_Float, wave_type_Str, play_time_Int)
        printSuccessful(wave_type, frequency, play_time)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    
