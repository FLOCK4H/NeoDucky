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
      
   2. Any USB-A port and a machine (PC/Laptop) to plug in the NeoKey

## Before we continue

> NeoDucky is an open-source CircuitPython implementation of an HID payload injection device. 
> Its use is intended solely for educational purposes. 
> Any misuse outside of this context may result in legal consequences, for which the author disclaims responsibility.

### Legal considerations

<details>
<summary>Click to expand</summary>
  
---

- Make sure you have explicit authorization before using NeoDucky on any device
- Incorporate time delays between actions to prevent potential damage
- Use the tool responsibly to avoid causing harm or chaos

---

</details>

# Setup

<details> 
  
<summary>Recipe for NeoDucky</summary>
<br>

- Download project files as .zip and unpack
  or `$ sudo git clone https://github.com/FLOCK4H/NeoDucky`
- Open the directory NeoDucky or NeoDucky-main
- Plug in the NeoKey Trinkey to USB-A
- TRINKEYBOOT drive should appear</br></br>
![image](https://github.com/FLOCK4H/NeoDucky/assets/161654571/8d8c108c-e0b7-443a-b6a6-ce85e83c83e5)</br>

In case nothing happens just double press the reset button on the board</br>
- Mount the drive (double-click) if it isn't already
- Drag and drop the 'adafruit-circuitpython-adafruit_neokey_trinkey_m0-en_US-8.2.10.uf2' from NeoDucky folder to the TRINKEYBOOT drive
- Voila, you should now have a drive named CIRCUITPY so access it
- Move project files there so only: code.py; boot.py; /tools/; /lib/;

> If you run into any "there is not enough space" just remove all files from CIRCUITPY drive, and then move the project files freely. In order to remove all files you must remove all hidden files too (".fseventsd", > ".Trash-1000", ".metadata_never_index").

- Transform NeoKey into NeoDucky by pressing the Reset button on the back of the board

</details>

<details>
  <summary>Easy Payload Syntax</summary>
  
### To manage NeoDucky's payload just edit payload.txt in tools folder inside CIRCUITPY drive

1. Introduction
   
Let's try to write a simple payload that will type in "Hello World!" after NeoDucky boots up

`payload.txt`
```
Hello World!
```

Simple.

Now let's run it in loop:
```
Hello<time2> ;
World<time1>!;
<LOOP>;
```
(Notice the semicolon use, it has to be at the end of the line in multi-line payloads)

One line is also fine:
```
Hello<time2> World<time1><LOOP>
```

- 'timeX' - where X is the amount of time to sleep
  
- 'LOOP' - as one of special tags, when used it will repeat the operation over and over, it has a near second cooldown to reduce eventual damage

2. Keycodes
   
Keycodes are mostly single character format so "A" = "A" but there are exceptions:

- "\n" is used as 'jump into newline' or RETURN key
- "\t" a tab or four spaces are taken as a TAB key and will return four spaces, use <TAB> tag instead to simulate its press

3. Tags

Tags are used to perform specific actions in the payload, there are two types of tags:

    1. Single

- The button that was pressed is automatically released before the next payload character is sent

```
<ESC> - ESCAPE,
<BSC> - BACKSPACE,
<TAB> - TAB,
<SCR> - PRINT SCREEN,
<SLK> - SCROLL LOCK,
<PAS> - PAUSE,
<INS> - INSERT,
<HOE> - HOME,
<PGU> - PAGE UP,
<PGD> - PAGE DOWN,
<ARR> - ARROW RIGHT,
<ARL> - ARROW LEFT,
<ARD> - ARROW DOWN,
<ARU> - ARROW UP,
<NLK> - NUMLOCK,
<APP> - APPLICATION,
<PWR> - macOS only,
<GUI> - WINDOWS KEY,
<CMD> - WINDOWS KEY,
<WIN> - WINDOWS KEY,
<CTL> - LEFT CONTROL,
<SPC> - SPACEBAR
```

    2. Multi

- Button is only released when it meets a sibling tag ("<LSHT>a<LSHT>a" will output 'Aa')
  
```
   <CTRL> - Left Control
   <LALT> - Left Alt
   <CTRR> - Right Control
   <RALT> - Right Alt
   <GCMD> - GUI/Command
   <LSHT> - Left Shift
   <RSHT> - Right shift
   <CAPS> - Capslock
   <LOOP> - Run in loop
   <timeX> - sleep for X time
```

### Example Payload
```
<GUI><time2>chrome<time2>\n<time2>www.youtube.com<time1>/n<time2><CTRL>w<time1><LSHT>~<LSHT>
```

</details>

# Usage

<details>
 <summary>Click to expand</summary>
  
Ducky will detect the operating system itself if its MacOS, basing on files structure. After analyzing the payload, it will start execution at a high speed, consider using time breaks. 

On Linux/ Windows devices to hide the Ducky's storage and enter Stealth mode just uncomment the line

`storage.disable_usb_device()`

In `boot.py` file.

To turn off the Stealth mode just enter REPL session with the NeoDucky using any serial terminal and type

`storage.enable_usb_device()`

</details>

# Conclusion

> While NeoDucky is a powerful device, it shouldn't be used in any harmful way, HID Payload Injection is a form of an attack that will result in legal consequences.
