#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("/opt/audio/bbc_water---wa_nhu0501301.mp3")

player = OMXPlayer(VIDEO_PATH, args=['-o alsa'], dbus_name='org.mpris.MediaPlayer2.omxplayer1')

sleep(5)

player.quit()


