import time
import random
import digitalio
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

## apps to iterate

apps = [
    {
        "search_name": "chrome",
        "wait_priority": 1.2,
        "productive": True
    },
    {
        "search_name": "kitty",
        "wait_priority": 1.6,
        "productive": True
    },
    {
        "search_name": "chat",
        "wait_priority": 1.3,
        "productive": True
    },
    {
        "search_name": "clickup",
        "wait_priority": 1.3,
        "productive": True
    },
    {
        "search_name": "safari",
        "wait_priority": 0.2,
        "productive": False
    },
]

# Función para enviar un clic izquierdo del mouse
def send_left_click(mouse):
    mouse.click(Mouse.LEFT_BUTTON)

# Función para enviar un movimiento del mouse a una posición específica
def send_mouse_move(mouse, x, y):
    mouse.move(x, y)

# Función para enviar la combinación de teclas CMD + Space
def send_cmd_space(keyboard, Keycode):
    keyboard.press(Keycode.COMMAND)
    keyboard.press(Keycode.SPACE)
    keyboard.release_all()

# Función para enviar texto como si se estuviera escribiendo en un teclado
def send_typing(keyboard_layout, text):
    keyboard_layout.write(text)

def next_app(apps, current_app, cicle, run_unproductive):
    if current_app < len(apps) - 1:
        current_app += 1
    else:
        current_app = 0

    run_unproductive = True if cicle >= 10 else False
    cicle = cicle+1 if cicle <= 10 else 1
    
    return current_app, cicle, run_unproductive

def run_meet_mode(apps, duration_seconds=4800, current_app=0, cicle=1, run_unproductive=False):
    # Copy parameters to local variables
    _current_app = current_app
    _cicle = cicle
    _run_unproductive = run_unproductive

    base_sleep = 30 # time in seconds
    
    start_time = time.monotonic()
    invert = False

    # led = digitalio.DigitalInOut(board.LED)
    # led.direction = digitalio.Direction.OUTPUT

    # Inicializar los objetos Mouse y Keyboard, y KeyboardLayout
    mouse = Mouse(usb_hid.devices)
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)
    
    while time.monotonic() - start_time < duration_seconds:
        place = 100 * (-1 if invert else 1)

        send_mouse_move(mouse, place, 0)

        time.sleep(3)

        # get current app data
        app_to_call = apps[_current_app]
        
        random_bumper = random.uniform(1,2)

        if app_to_call:
            # if is unproductive and unproductive run is not allowed just skip
            if app_to_call["productive"] is False and _run_unproductive is False:
                time.sleep(2)
                pass
            else:
                send_cmd_space(keyboard, Keycode)
                time.sleep(2)
                send_typing(keyboard_layout, app_to_call["search_name"])

                time.sleep(2)
                
                send_typing(keyboard_layout, "\n")

                time_to_sleep = (base_sleep * app_to_call["wait_priority"]) * random_bumper
                time_to_sleep = round(time_to_sleep, 2)
                
                # turn led on wait
                time.sleep(2)
                # led.value = True

                time.sleep(time_to_sleep)

                # turn led off on action
                time.sleep(2)
                # led.value = False
                
            _current_app, _cicle, _run_unproductive = next_app(apps, _current_app, _cicle, _run_unproductive)

        invert = not invert

if __name__ == "__main__":
    # Call the function with default time (1.5 hours)
    run_meet_mode()
