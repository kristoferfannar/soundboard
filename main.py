from pynput.keyboard import Listener, Key
from playsound import playsound


def onPress(key):
    if isinstance(key, Key) and key == Key.cmd_r:
        playsound("bruh.mp3")


def main():
    listener = Listener(on_press=onPress)
    listener.start()
    listener.join()

main()