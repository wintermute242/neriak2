import win32gui
import pydirectinput
import time

program_name = "EverQuest 2"

def enumHandler(hwnd):
    if program_name in win32gui.GetWindowText(hwnd):
            set_focus(hwnd)
            return

def set_focus(handle):
    # If the application is minimized, show the window with it's last used placement and dimensions
            if win32gui.IsIconic(handle):
                print("Application is minimized...")
                win32gui.ShowWindow(handle, 1)

            print(f"Activating window '{program_name}'...")
            try:
                win32gui.SetForegroundWindow(handle)
            except:
                pass
        
            time.sleep(0.25) # Give the window enough time to get focus or the keystroke will go who knows where

def get_focus():
    win32gui.EnumWindows(enumHandler, None)

def pause(seconds):
    """Pauses execution for specified number of seconds. This can be a float for fractions of a second."""
    time.sleep(seconds)


def send(key_value):
    # Only run if the value is not None
    if key_value:
        keys = key_value.split('+')

        if len(keys) > 1:
            send_key_combination(keys)
    
        else:
            send_key(keys[0])

def send_key(key_name):
    pydirectinput.FAILSAFE = False
    print("send_key")
    # DirectInput Key Codes 
    # at https://github.com/learncodebygaming/pydirectinput/blob/master/pydirectinput/__init__.py
    get_focus()
    pydirectinput.press(key_name)

def send_keys(keys):
    pydirectinput.FAILSAFE = False
    get_focus()
    for key in keys:
        pydirectinput.press(key)


def send_key_combination(keys):
    pydirectinput.FAILSAFE = False
    print(f"send_key_combination {keys}")
    get_focus()
    for key in keys:
        pydirectinput.keyDown(key)

    for key in keys:
        pydirectinput.keyUp(key)
    