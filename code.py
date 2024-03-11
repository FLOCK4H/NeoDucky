#                                        ⠀⠀⠀⠀⠀⠀⠀⠀  ⣤⡶⠿⠿⠷⣶⣄⠀⠀⠀⠀⠀
#  _  _         ___          _        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣰⡿⠁⠀⠀⢀⣀⡀⠙⣷⡀⠀⠀⠀
# | \| |___ ___|   \ _  _ __| |___  _  ⠀⠀⠀⡀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠘⠿⠃⠀⢸⣿⣿⣿⣿
# | .` / -_) _ \ |) | || / _| / / || |⠀ ⣠⡿⠛⢷⣦⡀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠟
# |_|\_\___\___/___/ \_,_\__|_\_\\_, | ⢰⡿⠁⠀⠀⠙⢿⣦⣤⣤⣼⣿⣄⠀⠀⠀⠀⠀⢴⡟⠛⠋⠁⠀
#                               |__/   ⣿⠇⠀⠀⠀⠀⠀ ⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⣿⡀
#                                      ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢹⡇
#       made with ❤️ by FLOCK4H        ⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇
#           Version 0.99               ⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀
#⠀                                      ⠹⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⡿⠁
#⠀⠀⠀                                      ⠉⠙⠛⠿⠶⣶⣶⣶⣶⠿⠟⠛⠉

import time
import board
from adafruit_hid.keyboard import Keyboard
from usb_hid import devices
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import tools.keycodes as keycodes
from tools.detect_os import detect_os_by_files
from tools.analyzer import analyze_payload
import gc
from neopixel import NeoPixel
from os import listdir
from random import randint, uniform
from supervisor import runtime

runtime.autoreload = False

pixel = NeoPixel(board.NEOPIXEL, 1, brightness=0.05)
gc.collect()

class NeoDucky:
    def __init__(self):
        self.kc = keycodes.KeyCodes()
        self.keyboard = Keyboard(devices)
        self.active_toggles = set()

    def handle_toggle(self, token):
        if token in self.active_toggles:
            self.keyboard.release(self.kc.toggles[token])
            self.active_toggles.remove(token)
        else:
            self.keyboard.press(self.kc.toggles[token])
            self.active_toggles.add(token)

    def execute_payload(self, tokens):
        for token in tokens:
            if token.startswith('<') and token.endswith('>'):
                if "time" in token[1:-1]:
                    pixel.fill((255, 255, 0))  # yellow
                    sleep_time = int(token[5:-1])
                    time.sleep(sleep_time)
                elif token in self.kc.system_chars:
                    pixel.fill((0, 255, 0)) # green
                    self.keyboard.send(self.kc.system_chars[token])
                elif token in self.kc.toggles:
                    self.handle_toggle(token)
                    pixel.fill((0, 0, 255))  # blue
                else:
                    pixel.fill((255, 165, 0))  # orange
            else:
                for char in token:
                    if char in self.kc.shift_char:
                        self.keyboard.press(Keycode.SHIFT)
                        self.keyboard.press(self.kc.shift_char[char])
                        self.keyboard.release_all()
                        pixel.fill((255, 0, 0))
                    elif char in self.kc.keys:
                        self.keyboard.send(self.kc.keys[char])
                        pixel.fill((0, 255, 255))  # cyan
                    else:
                        print(f"No keycode mapping found for '{char}'")
                        pixel.fill((255, 0, 255))  # magenta
                    
                    for active_toggle in self.active_toggles:
                        self.keyboard.press(self.kc.toggles[active_toggle])
        
        for toggle in list(self.active_toggles):
            self.keyboard.release(self.kc.toggles[toggle])
        self.active_toggles.clear()
        pixel.fill((0, 255, 0))

    def payloads_write(self, payload):
        loop_payload = "<LOOP>" in payload
        if loop_payload:
            payload = payload.replace("<LOOP>", "")
        tokens = analyze_payload(payload)
        while True:
            self.execute_payload(tokens)
            for toggle in list(self.active_toggles):
                self.keyboard.release(self.kc.toggles[toggle])
            self.active_toggles.clear()
            if not loop_payload:
                break
            #                       !!!
            #  REMOVE THE DELAY ONLY IF YOU SURE WHAT YOU DOING
            #  USING <LOOP> WITHOUT TIMERS IS DANGEROUSLY STUPID 
            #                       !!!
            time.sleep(0.7)

def load_payload_from_file():
    loaded = []
    tools_dir = listdir('tools')
    if 'payload.txt' in tools_dir and 'payload_mac.txt' in tools_dir:
        payloads = ["payload.txt", "payload_mac.txt"]
        for p in payloads:
            with open(f'tools/{p}', 'r') as f:
                payload_lines = f.readlines()
                processed_payload = ''.join(line.strip().rstrip(';') for line in payload_lines)
                processed_payload = processed_payload.replace('\\n', '\n').replace('\\t', '\t')
                loaded.append({p: processed_payload})
                gc.collect()
        return loaded
    else:
        print("You have to add payload.txt and payload_mac.txt files to the tools folder")
        return []
    
def main():
    ducky = NeoDucky()
    payloads = load_payload_from_file()

    payload, payload_mac = None, None
    for p in payloads:
        for k, v in p.items():
            if k == "payload.txt":
                payload = v
            elif k == "payload_mac.txt":
                payload_mac = v

    os_detected = detect_os_by_files()
    print(f"Detected OS: {os_detected}")

    if os_detected == "macOS" and payload_mac is not None:
        ducky.payloads_write(payload_mac)
    elif payload is not None:
        ducky.payloads_write(payload)

    gc.collect()
    while True:
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        brights = uniform(0.08, 0.3)
        pixel.fill((r, g, b))
        pixel.brightness = brights
        time.sleep(uniform(0.05, 0.2))
        gc.collect()

if __name__ == "__main__":
    main()
