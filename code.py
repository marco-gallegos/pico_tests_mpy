'''this is circuit python code
'''

import time
from digitalio import DigitalInOut
import board
import adafruit_matrixkeypad # v 1.2.17

import random
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
# from keyboard_layout_win_es import KeyboardLayout
from adafruit_hid.keycode import Keycode
# from keycode_win_es import Keycode
from meetmode import run_meet_mode, apps


## matrix values 
# Extended 4x4 matrix keypad
cols = [DigitalInOut(x) for x in (board.GP0, board.GP1, board.GP2, board.GP3)]
rows = [DigitalInOut(x) for x in (board.GP4, board.GP5, board.GP6, board.GP7)]
keys = ((1, 2, 3, "A"), (4, 5, 6, "B"), (7, 8, 9, "C"), ("*", 0, "#", "D"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

## USB HID setup
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Inicializar los objetos Mouse y Keyboard, y KeyboardLayout
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)
keyboard_layout.COMBINED_KEYS = {
    "n": "ñ"
    # "ñ": "~+n",
    # "~+n": "ñ",
    # "en": "marco"
}

### functions hid section

# Función para enviar un clic izquierdo del mouse
def send_left_click():
    mouse.click(Mouse.LEFT_BUTTON)

# Función para enviar un movimiento del mouse a una posición específica
def send_mouse_move(x, y):
    mouse.move(x, y)

# Función para enviar la combinación de teclas CMD + Space
def send_cmd_space():
    keyboard.press(Keycode.COMMAND)
    keyboard.press(Keycode.SPACE)
    keyboard.release_all()

# Función para enviar texto como si se estuviera escribiendo en un teclado
def send_typing(text):
    keyboard_layout.write(text)


def switch_layout(os:string):
    if os is 'mac':
        keyboard.press(Keycode.CONTROL)
        keyboard.press(Keycode.SHIFT)
        keyboard.send(Keycode.TAB)
        keyboard.release_all()


def print_enie():
    switch_layout('mac')
    send_typing(';') # same key as ñ
    switch_layout('mac')

fifteen_minutes = 15 * 60  # 15 minutos en segundos

## main cicle
while True:
    keys = keypad.pressed_keys
    print(keys)
    if len(keys) == 2:
        if "D" in keys and 1 in keys:
            run_meet_mode(apps, fifteen_minutes * 2)
        elif "D" in keys and 2 in keys:
            run_meet_mode(apps, fifteen_minutes * 3)
        elif "D" in keys and 3 in keys:
            run_meet_mode(apps, fifteen_minutes * 4)
        elif "D" in keys and 4 in keys:
            run_meet_mode(apps, fifteen_minutes * 6)
        
    else:
        if "#" in keys:
            print_enie()
        elif 1 in keys:
            keyboard.send(Keycode.F11)
            keyboard.release_all()
            time.sleep(0.1)

    time.sleep(0.1)
