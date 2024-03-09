#                                        ⠀⠀⠀⠀⠀⠀⠀⠀  ⣤⡶⠿⠿⠷⣶⣄⠀⠀⠀⠀⠀
#  _  _         ___          _        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣰⡿⠁⠀⠀⢀⣀⡀⠙⣷⡀⠀⠀⠀
# | \| |___ ___|   \ _  _ __| |___  _  ⠀⠀⠀⡀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⠘⠿⠃⠀⢸⣿⣿⣿⣿
# | .` / -_) _ \ |) | || / _| / / || |⠀ ⣠⡿⠛⢷⣦⡀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠟
# |_|\_\___\___/___/ \_,_\__|_\_\\_, | ⢰⡿⠁⠀⠀⠙⢿⣦⣤⣤⣼⣿⣄⠀⠀⠀⠀⠀⢴⡟⠛⠋⠁⠀
#                               |__/   ⣿⠇⠀⠀⠀⠀⠀ ⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠈⣿⡀
#                                      ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢹⡇
#       made with ❤️ by FLOCK4H        ⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇
#           Version 0.1                ⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀
#⠀                                      ⠹⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⡿⠁
#⠀⠀⠀                                      ⠉⠙⠛⠿⠶⣶⣶⣶⣶⣶⠶⠿⠟⠛⠉

import time
import board
from adafruit_hid.keyboard import Keyboard
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import gc
import tools.keycodes as keycodes
from tools.detect_os import detect_os_by_files
from tools.analyzer import analyze_payload
import neopixel
import random

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05)

class NeoDucky:
    def __init__(self):
        self.kc = keycodes.KeyCodes()
        self.keyboard = Keyboard(usb_hid.devices)
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
        tokens = analyze_payload(payload)
        print(tokens)
        self.execute_payload(tokens)
        for toggle in list(self.active_toggles):
            self.keyboard.release(self.kc.toggles[toggle])
        self.active_toggles.clear()


def main():
    time.sleep(1)
    ducky = NeoDucky()

    os_detected = detect_os_by_files()
    print(f"Detected OS: {os_detected}")

    if os_detected == "macOS":
        ducky.payloads_write("macOS specific payload here")
    elif os_detected == "Other":
        ducky.payloads_write("\n<time1><HOE><time1>1234<time1>\n4567\n<time1>4192<time1>\n8888<time1>\n5319<time1>\n<GCMD>b<GCMD><time4>h<time1>ttps://pornhub.com<time5>\n")

    gc.collect()
    while True:
        r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        brights = random.uniform(0.01,0.3)
        pixel.fill((r, g, b))
        pixel.brightness = brights
        time.sleep(random.uniform(0.05, 0.2))
        gc.collect()

if __name__ == "__main__":
    main()

