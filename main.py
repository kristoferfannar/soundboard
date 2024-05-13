from pynput.keyboard import Listener, Key
import sounddevice as sd
import soundfile as sf
# import platform as plt 
from util import find_speaker_device

bruh_filename = "bruh.mp3"
boom_filename = "vine-boom.mp3"

filenames = [bruh_filename, boom_filename]
sound_data = {}

for filename in filenames:
    data, fs = sf.read(filename, dtype='float32')
    sound_data[filename] = {'data': data, 'fs': fs}

speaker_device_id = find_speaker_device()

def onPress(key):
    print(key)
    # bruh sound effect
    if isinstance(key, Key) and (key == Key.cmd_r or key == Key.alt_gr):
        bruh_data = sound_data[bruh_filename]['data']
        bruh_fs = sound_data[bruh_filename]['fs']

        sd.play(bruh_data, bruh_fs, device=speaker_device_id)
        sd.wait()
    
    # vine boom sound effect
    elif isinstance(key, Key) and (key == Key.shift_r):
        boom_data = sound_data[boom_filename]['data']
        boom_fs = sound_data[boom_filename]['fs']

        sd.play(boom_data, boom_fs, device=speaker_device_id)
        sd.wait()

def main():
    listener = Listener(on_press=onPress)
    listener.start()
    listener.join()

main()
