#!/usr/bin/env python3

from os import listdir, system
from os.path import join, splitext
from time import sleep
import signal

PATH = '/opt/audio'
EXT = '.mp3'
VOLUME = '-2400'

def main():
    files = listdir(PATH)
    
    while True:
        for f in files:
            ext = splitext(f)[1]
            if ext.lower() == EXT:
                filename = join(PATH,f)
                print("Playing file:", filename)
                system('omxplayer -o alsa --vol %s %s' % (str(VOLUME), filename))

if __name__ == '__main__':
    main()
