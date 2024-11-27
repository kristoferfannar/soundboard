from pynput.keyboard import Listener, Key, KeyCode
import sounddevice as sd
import soundfile as sf
import threading

# import platform as plt
from util import find_speaker_device

bruh_filename = "bruh.mp3"
boom_filename = "vine-boom.mp3"
huh_filename = "huh.mp3"

filenames = [bruh_filename, boom_filename, huh_filename]
sound_data = {}

for filename in filenames:
    data, fs = sf.read(filename, dtype="float32")
    sound_data[filename] = {"data": data, "fs": fs}

speaker_device_id = find_speaker_device()


def onPress(key: Key | KeyCode | None):
    if isinstance(key, Key):
        # huh
        if (key == Key.alt_r) or (key.value.vk == 61):
            huh_data = sound_data[huh_filename]["data"]
            huh_fs = sound_data[huh_filename]["fs"]

            def play():
                sd.play(huh_data, huh_fs, device=speaker_device_id)
                # sd.wait()

            thread = threading.Thread(target=play)
            thread.start()

        # bruh sound effect
        elif key == Key.cmd_r or key == Key.alt_gr:
            bruh_data = sound_data[bruh_filename]["data"]
            bruh_fs = sound_data[bruh_filename]["fs"]

            def play():
                sd.play(bruh_data, bruh_fs, device=speaker_device_id)

            thread = threading.Thread(target=play)
            thread.start()
            # sd.wait()

        # vine boom sound effect
        elif key == Key.shift_r:
            boom_data = sound_data[boom_filename]["data"]
            boom_fs = sound_data[boom_filename]["fs"]

            def play():
                sd.play(boom_data, boom_fs, device=speaker_device_id)

            thread = threading.Thread(target=play)
            thread.start()
            # sd.wait()


def main():
    listener = Listener(on_press=onPress)
    listener.start()
    listener.join()


main()
