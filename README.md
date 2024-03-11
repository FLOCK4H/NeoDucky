<div align="center">
  <img width="200" alt="NeoDucky Logo" src="https://github.com/FLOCK4H/NeoDucky/assets/161654571/b9ae9606-0ce3-43f1-9383-2a35d9c2f76a" />
</div>



> [!WARNING]
> The author is not responsible for any malicious use of the software.</br> Users are advised to employ NeoDucky strictly for educational, ethical hacking, and security research purposes.


# NeoDucky

NeoDucky is a highly compact, efficient, and multiplatform BadUSB/RubberDucky device powered by Adafruit NeoKey Trinkey.

Not equipped with any SD Card reader on purpose - to make stealing activities harder.

## What NeoDucky can do?
<details>
  <summary>Click to expand</summary>

1. Execute Keyboard Payloads
   - Store/gather small amount of data
   - 2 payloads for 2 different systems
   - Loop option
   - Easy Payload Syntax
   - Speed of light execution

2. Distinguish between Mac/Linux & Windows
3. Switch between Storage/ Stealth modes

**TODO:**
- Config '.json' very soon

</details>

## Introduction to NeoDucky

NeoDucky is designed as the most cost-effective BadUSB device in its class, focusing on providing a powerful tool for security professionals and ethical hackers.

Components:
   1. Adafruit NeoKey Trinkey ATSAMD21E18
      - Price as of 2024: ~8-10$</br>
   2. Any USB-A adapter/port and a machine (PC/Laptop) to plug in the USB-A end of the NeoKey

## Before we continue

> NeoDucky is an open-source CircuitPython implementation of an HID payload injection device. 
> Its use is intended solely for educational purposes. 
> Any misuse outside of this context may result in legal consequences, for which the author disclaims responsibility.

### Legal considerations
<details>
<summary>Click to expand</summary></br>
  
---

- Make sure you have explicit authorization before using NeoDucky on any device
- Incorporate time delays between actions to prevent potential damage
- Use the tool responsibly to avoid causing harm or chaos

---

</details>

# Setup

Recipe for NeoDucky:

- Download project files as .zip and unpack
  or `$ sudo git clone https://github.com/FLOCK4H/NeoDucky`
- Open the directory NeoDucky or NeoDucky-main
- Plug in the NeoKey Trinkey to USB-A
- TRINKEYBOOT drive should appear</br></br>
![image](https://github.com/FLOCK4H/NeoDucky/assets/161654571/8d8c108c-e0b7-443a-b6a6-ce85e83c83e5)</br>
</br>In case nothing happens just double press the reset button on the board</br>
- Mount the drive (double-click) if it isn't already
- Drag and drop the 'adafruit-circuitpython-adafruit_neokey_trinkey_m0-en_US-8.2.10.uf2' from NeoDucky folder to the TRINKEYBOOT drive
- Voila, you should now have a drive named CIRCUITPY so access it
- Move project files there so only: code.py; boot.py; /tools/; /lib/;

The important part is getting files there, if you run into any "there is not enough space" just remove all files from CIRCUITPY drive,
then 
