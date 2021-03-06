import win32gui
import pydirectinput
import time

program_name = "EverQuest II"
DEBUG: False

def debug_message(string):
    if DEBUG:
        print(string)

def enumHandler(hwnd, _) -> bool:
    current_title = win32gui.GetWindowText(hwnd)
    debug_message(f"Found window: {current_title}")
    if program_name in current_title:
            debug_message("Calling set_focus() on handle {hwnd}")
            set_focus(hwnd)
            return False
    return True

def set_focus(handle) -> None:
    # If the application is minimized, show the window with it's last used placement and dimensions
            if win32gui.IsIconic(handle):
                debug_message("Application is minimized...")
                win32gui.ShowWindow(handle, 1)

            debug_message(f"Activating window '{program_name}'...")
            try:
                win32gui.SetForegroundWindow(handle)
            except:
                pass
        
            time.sleep(0.25) # Give the window enough time to get focus or the keystroke will go who knows where

def get_focus() -> None:
    try:
        win32gui.EnumWindows(enumHandler, None)
    except:
        pass

def pause(seconds) -> None:
    """Pauses execution for specified number of seconds. This can be a float for fractions of a second."""
    time.sleep(seconds)


def send(key_value) -> None:
    # Only run if the value is not None
    if key_value:
        keys = key_value.split('+')

        if len(keys) > 1:
            send_key_combination(keys)
    
        else:
            send_key(keys[0])

def send_key(key_name) -> None:
    pydirectinput.FAILSAFE = False
    debug_message("send_key")
    # DirectInput Key Codes 
    # at https://github.com/learncodebygaming/pydirectinput/blob/master/pydirectinput/__init__.py
    get_focus()
    pydirectinput.press(key_name)

def send_keys(keys) -> None:
    pydirectinput.FAILSAFE = False
    get_focus()
    for key in keys:
        pydirectinput.press(key)


def send_key_combination(keys) -> None:
    pydirectinput.FAILSAFE = False
    debug_message(f"send_key_combination {keys}")
    get_focus()
    for key in keys:
        pydirectinput.keyDown(key)

    for key in keys:
        pydirectinput.keyUp(key)
    