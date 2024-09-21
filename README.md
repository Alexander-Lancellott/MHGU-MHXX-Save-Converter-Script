<h1 align="center"> MHGU-MHXX-Save-Converter-Script </h1>

<div align="center">

[![Static Badge](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![App](https://img.shields.io/badge/App-1.0.0-green)](https://github.com/Alexander-Lancellott/MHGU-MHXX-Save-Converter-Script)

</div>

## Introduction

First of all, Python is not my strong suit, so there may be sections of the code that could be improved or simplified in fewer lines. However, I think I have done a decent job with this programming language. Although this first version has been tested countless times, there is still the possibility of it having some errors. I would appreciate it if you could report them by opening an issue in this repository and providing evidence to replicate them.

***Make sure to backup your save file first***.

## Description

The purpose of this project is to allow the conversion of your saved games from `MHXX (3DS)` to `MHGU/MHXX (Switch)` and vice versa, using three scripts I've developed through reverse engineering to assist you with this challenging task. While there's already an app called [MHXXSwitchSaveEditor](https://github.com/Dawnshifter/MHXXSwitchSaveEditor) that performs this task, it's not particularly effective for converting saved games; its strength lies more in editing them.

One of the issues I encountered with this editor is that it was able to convert saved games from `MHXX (3DS)` to `MHGU (Switch)`, but not the other way around. I also noticed that this editor breaks the in-game chat menu. If you have more than one saved slot and edit roughly half or more of the chat menu in the saved game from Switch generated by `MHXXSwitchSaveEditor`, it can completely destroy it. This is due to fact that the chat menu in the Switch version occupies a larger number of bytes than in the 3DS version, causing it to overwrite a portion of the second saved slot, rendering it permanently irrecoverable. As a result, this will cause the game to crash when trying to load it.

If the scripts I've developed meet your expectations, I would recommend using `MHXXSwitchSaveEditor` solely for editing your saves, but not for conversion purposes. Also, bear in mind that they are incompatible with each other. Therefore, if you have a Switch save file that resulted from a conversion with `MHXXSwitchSaveEditor`, you will generally need to take an extra step to make it compatible with my conversion scripts.

## ADD DLC

### Option A 
My scripts do not require you to remove the DLC. These scripts copy the initial bytes from the `system` files found in the `Blank_3DS_Save` and `Blank_Switch_Save` folders, and then insert the remaining bytes to form the new file for the corresponding version.

In summary, the `system` files provided in the `Blank` folders are completely blank (meaning that they don't contain any saved slots) and **DO NOT** contain any DLC. If you want the conversion scripts from sections [2](#2-mhgumhxx-to-mhxx---switch-to-3ds) and [3](#3-mhxx-to-mhgumhxx---3ds-to-switch) to automatically add the DLC to the new files generated in the output folders, you simply need to replace the `system` file in the `Blank` folder of the corresponding version(`Blank_3DS_Save` or `Blank_Switch_Save`) with one that contains the DLC.

It is not necessary for the `system` file to be blank; it just needs to contain the DLC, as mentioned earlier, only the initial part of the file will be copied.

### Option B
An alternative option for adding DLCs consists in following the steps detailed in sections [2](#2-mhgumhxx-to-mhxx---switch-to-3ds) or [3](#3-mhxx-to-mhgumhxx---3ds-to-switch) and then load the generated files in the corresponding console in order to download the DLCs.

> [!WARNING]  
> Please do not delete the `Blank_3DS_Save` and `Blank_Switch_Save` folders or their `system` files; they are essential for the operation of all 3 scripts. However, you can replace the `system` files with other `system` files, either with or without DLC, that correspond to the console version mentioned in their folder.

## How to use

First of all, ***make sure to backup your save file***.

### 1. FIX SAVE - (Extra step if you used `MHXXSwitchSaveEditor` to convert your save)

As I mentioned above, this script is an additional step only needed if you have a saved game that was converted from MHXX (3DS) to MHGU (Switch) using `MHXXSwitchSaveEditor`. Therefore, if you haven't performed that conversion, you should skip this section and proceed to section [2](#2-mhgumhxx-to-mhxx---switch-to-3ds) or [3](#3-mhxx-to-mhgumhxx---3ds-to-switch).

The purpose of this section is to make your save file compatible with the script documented in section [2](#2-mhgumhxx-to-mhxx---switch-to-3ds) or simply to try to recover your chats, if that's what you want.

1. Place your Switch `system` file in the root folder of the `FIX_SAVE - (Switch To Switch)` folder.
2. Run the `MHXX-MHGU-Save-Converter.exe` file or simply `MHXX-MHGU-Save-Converter` for Unix systems.

>[!IMPORTANT]
> To execute the script on a Unix system (Mac/Linux), you need to give it execute permissions by following these steps:
>
> - Open the terminal and enter the following commands:
> - cd `"PATH OF THE SCRIPT ROOT FOLDER"`
> - chmod +x MHXX-MHGU-Save-Converter
> - ./MHXX-MHGU-Save-Converter
>
> Now, this should execute the script in the terminal.

3. Type the number 2 and press enter for run the script.
4. The script will prompt you to choose between two options:
   1. Try to recover it - (Recommended if you didn't edit the chats in MHGU).
   2. Replace it with the English version of MHGU.
5. Simply type the number to the left of the option you want to choose.
6. Wait until the script prompts you to press **"R"** to return to the main menu or any other key to exit, then navigate to the `output - (Switch)` folder. There you should find your new fixed `system` file, which is compatible with section [2](#2-mhgumhxx-to-mhxx---switch-to-3ds).
7. To make sure that the generated file is not damaged, I recommend testing it on your Switch or emulator. If everything goes well, you should find your 3DS version chats in the chat menu. If you choose `option 1` in the script, you may see some strange characters, which is normal since some characters of the 3DS version are not supported in the Switch version and vice versa. However, they should now be visible and not appear empty. If you edited them in English, they should display correctly in both versions. On the other hand, if you choose `option 2`, they will be overwritten with the English version of MHGU in all your saved slots.
8. If everything goes well, you don't need to continue reading; go directly to section [2](#2-mhgumhxx-to-mhxx---switch-to-3ds) or simply use your new file with the fixed chats on your Switch or emulator.

If you followed the previous steps but the script generated a damaged save file, you can do the following:

1. Follow the steps in ["Transfer to a blank save"](#transfer-to-a-blank-save---requires-emulator).
2. If you want to recover your chats repeat steps 1 to 6 of this section, but this time with the save file obtained in ["Transfer to a blank save"](#transfer-to-a-blank-save---requires-emulator). If you don't want to recover your chats, you can simply overwrite the chats from within the game. Keep in mind that they will be overwritten with the language version configured in the game. I have only tested with English and Spanish, so I am unaware of what may happen with other languages. Alternatively, you can redo the script steps and select `option 2`.
3. If everything went well, your file should now be compatible with section [2](#2-mhgumhxx-to-mhxx---switch-to-3ds). If the script continues to generate a damaged file, use the file obtained in the ["Transfer to a blank save"](#transfer-to-a-blank-save---requires-emulator). Do not pass this file through the script; simply restore the chats from within the game.

The script for this section is something I hadn't planned to develop, but as I found myself facing this issue, I had to come up with a solution. After releasing this first version, I will not be working on fixing any further issues with it. I apologize if the script for this section doesn't work for you after following all the steps. In that case, your only option is to use a save file that hasn't been converted with `MHXXSwitchSaveEditor` but was originally created by the Switch version or converted using the script from section [3](#3-mhxx-to-mhgumhxx---3ds-to-switch).

### 2. MHGU/MHXX TO MHXX - (Switch To 3DS)

If you are coming from section [1](#1-fix-save---extra-step-if-you-used-mhxxswitchsaveeditor-to-convert-your-save), in the first step, use the `system` file generated by the `FIX_SAVE` script.

1. Place your Switch MHGU or MHXX `system` file in the root folder of the `MHGU-XX_TO_MHXX - (Switch To 3DS)` folder.
2. Run the `MHXX-MHGU-Save-Converter.exe` file or simply `MHXX-MHGU-Save-Converter` for Unix systems.

>[!IMPORTANT]
> To execute the script on a Unix system (Mac/Linux), you need to give it execute permissions by following these steps:
>
> - Open the terminal and enter the following commands:
> - cd `"PATH OF THE SCRIPT ROOT FOLDER"`
> - chmod +x MHXX-MHGU-Save-Converter
> - ./MHXX-MHGU-Save-Converter
>
> Now, this should execute the script in the terminal.

3. Type the number 3 and press enter for run the script.
4. Wait until the script prompts you to press **"R"** to return to the main menu or any other key to exit, and then go to the `output - (3DS)` folder. There you should find your new `system` file converted for 3DS MHXX.
5. Test the new save file on your 3DS or emulator.

### 3. MHXX TO MHGU/MHXX - (3DS To Switch)

1. Place your 3DS MHXX `system` file in the root folder of the `MHXX_TO_MHGU-XX - (3DS To Switch)` folder.
2. Run the `MHXX-MHGU-Save-Converter.exe` file or simply `MHXX-MHGU-Save-Converter` for Unix systems.

>[!IMPORTANT]
> To execute the script on a Unix system (Mac/Linux), you need to give it execute permissions by following these steps:
>
> - Open the terminal and enter the following commands:
> - cd `"PATH OF THE SCRIPT ROOT FOLDER"`
> - chmod +x MHXX-MHGU-Save-Converter
> - ./MHXX-MHGU-Save-Converter
>
> Now, this should execute the script in the terminal.

3. Type the number 4 and press enter for run the script.
4. The script will ask you to choose which game you'd like to convert your save file to:
   1. MHGU.
   2. MHXX Switch Version.
5. Simply type the number to the left of the option you want to choose.
6. Wait until the script prompts you to press **"R"** to return to the main menu or any other key to exit, and then go to the `output - (Switch)` folder. There you should find your new `system` file converted for MHGU or MHXX Switch Version.
7. Test the new save file on your Switch or emulator.

### Transfer to a blank save - (Requires emulator) 

***Make sure to backup your save file***

Previously, you had to perform the following steps in the 3DS emulator to remove the DLC before using `MHXXSwitchSaveEditor` to convert your game save. However, with the scripts I developed, it's no longer necessary unless you're experiencing issues with the script from section [1](#1-fix-save---extra-step-if-you-used-mhxxswitchsaveeditor-to-convert-your-save).

In that case, you'll need a Switch emulator and you'll need to dump the game from your Switch if you haven't already done so.

1. Go to the MHGU save files directory in the emulator and paste the backup of your save file if you didn't already. 
2. Start MHGU on Emulator and load the game and your character slot.
3. Open the `Blank_Switch_Save` folder and copy the contents into the contents of your save file directory, it will ask permission to replace the current files, click yes.
4. Go back to MHGU and save the game
5. Restart your game
6. If your character is in the save file, return to section [1](#1-fix-save---extra-step-if-you-used-mhxxswitchsaveeditor-to-convert-your-save)

> [!IMPORTANT]
>It's important not to close either the emulator or the game while performing steps 2 through 4.
>
>Note that the previous steps will only transfer the `slot` you load. Therefore, if you want to transfer another `slot` to the same file, you'll need to repeat the steps. This time, load your previous saved game, of which you should have a backup, and use the save file from the previous transfer as the content of the `Blank_Switch_Save` folder in step 3.

## Issue with 60fps cheat - (For 3DS emulator)

The following is unrelated to the conversion scripts; it's simply something I discovered on my own. I'm not sure if anyone else has noticed this issue, but I wanted to document it because it could be useful to you.

Before trying this, I recommend monitoring your hardware temperatures and usage at all times using software such as HWiNFO or MSI Afterburner's overlay.

When using the 3DS emulator with the 60 FPS cheat created by the MHXX community, I noticed frequent frame stutters or drops that prevented me from enjoying a smooth 60 FPS experience, despite having a system that far exceeds the requirements (R7 7800X3D, 32GB DDR5, RTX 3080TI). After several tests and unsuccessful internet searches, I came up with the idea of editing the 60 fps cheat itself to values higher than 60. Upon exceeding 140, I began to notice that the issue had been mitigated. Then, I left it at 200 just to make sure that the issue had disappeared and I still didn't
experience any problems with fps.

While the emulator or game engine doesn't allow for exceeding 60 FPS, increasing this value raised the `frametime`, measured in `ms`, which somehow resolved the issue. However, I noticed higher GPU consumption with this new value, so if you want to try this, I advise against values higher than 300 or 400. Before trying this method, make sure to deactivate the 3D effect from the game menu, as it also increases hardware usage. I'm not responsible if your GPU or CPU are damaged after trying this, so I recommend starting with 140 or maybe less, and then gradually increasing this value if it doesn't work well. Remember that the cheat code is written in hexadecimal values so you will need to convert the desired number of FPS to hexadecimal. You can do this [here](https://gregstoll.com/~gregstoll/floattohex/) by typing, for example, 140 in the float box and then clicking `convert to hex`. This will return the hexadecimal value that you should replace in the penultimate line of the cheat code. You can find an example below.

### Cheat for MHXX v1.4.0

<table>
<tr>
<td> Custom 60 FPS Default </td> 
<td> Custom 60 FPS Edited </td>
</tr>
<tr>
<td>

```
[Custom 60 FPS v1.4.0] 
*citra_enabled
*42700000 <--- 60
0088E584 EDD61A0C
60D3A040 00000000
B0D3A040 00000000
006A34A0 42700000
D2000000 00000000
``` 
</td>
<td>

```
[Custom 60 FPS v1.4.0] 
*citra_enabled
*43480000 <--- 200
0088E584 EDD61A0C 
60D3A040 00000000 
B0D3A040 00000000 
006A34A0 43480000
D2000000 00000000
``` 
</td>
</tr>
</table>

**Update**: While playing I noticed that this alone didn't mitigate the issue, so to completely fix it I had to increase the CPU clock speed of the 3DS emulator. I recommend setting this per game, so run the game in the emulator and go to Emulation --> Configure Current Game... in the emulator toolbar, go to the Debug tab there you will see under the box that says CPU, a bar of percentage and a selection box if the selected option is `Use global clock speed` change it to `Set clock speed` to be able to manipulate the bar, the default percentage is `100` change it to `120` or `150`, then click on the `Apply button` and on the `OK button`, done now you should experience a smooth 60 FPS.

<div align="center" >

![Config](https://res.cloudinary.com/dms5y8rug/image/upload/v1713902306/MHGU-MHXX-Save-Converter-Script/Screenshot_2024-04-23_165525.png)

</div>


### Cheat for MH3U - (EUR).

I also experienced this issue in MH3U, so I took the same approach, but it only worked with a value of 65. I tried to use higher values but the problem reappeared so I recommend to stick with 65.

<table>
<tr>
<td> 60 FPS Default </td> 
<td> 60 FPS Edited </td>
</tr>
<tr>
<td>

```
[60 FPS] 
*citra_enabled
*42700000 <--- 60
086261C0 42700000
``` 
</td>
<td>

```
[60 FPS] 
*citra_enabled
*42820000 <--- 65
086261C0 42820000
``` 
</td>
</tr>
</table>

I'm not completely sure of what is the cause of this issue, but I suspect it could be related to the refresh rate of the monitor, especially if it is very high or exceeds 60 Hz.

## Building scripts - (For Developers)

```
$ git clone
```

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ pip install .
$ build
```
or for Unix

```
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install .
$ build
```
You will find the `build` in the `dist` folder

## Python modules used

- pyinstaller - v6.5.0
- sshkeyboard - v2.3.1,
- colorama - v0.4.6
- art - v6.1
