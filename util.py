import sounddevice as sd

def find_speaker_device():
    devices = sd.query_devices()

    for device_id, device_info in enumerate(devices):
        if "speakers" in device_info['name'].lower():
            print(f"Found speakers: {device_info['name']} with device ID: {device_id}")
            return device_id

    print("No speakers found.")
    return None

