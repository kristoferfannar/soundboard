from pynput.keyboard import Listener, Key
import sounddevice as sd
import soundfile as sf
from util import find_speaker_device

filename = "bruh.mp3"
data, fs = sf.read(filename, dtype='float32')
speaker_device_id = find_speaker_device()

def onPress(key):
    if isinstance(key, Key) and key == Key.cmd_r:
        sd.play(data, fs, device=speaker_device_id)
        sd.wait()


def main():
    print(sd.query_devices())
    listener = Listener(on_press=onPress)
    listener.start()
    listener.join()

main()
