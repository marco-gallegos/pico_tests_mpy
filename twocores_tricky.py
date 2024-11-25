import machine
import utime
import _thread

led_a = machine.Pin(13, machine.Pin.OUT)
led_b = machine.Pin(12, machine.Pin.OUT)

# baton is an analogy from the "estafeta" in a human race
# baton = _thread.allocate_lock()

card_readed = False


def card_thread():
    while True:
        # request thread manager to reserve variables
        # baton.acquire()
        led_a.value(1)
        utime.sleep(1)
        led_a.value(0)
        utime.sleep(1)
        # say at thread manager that we finish and we will not use this vars anymore
        # baton.release()


# second thread code
_thread.start_new_thread(card_thread, ())


# main thread work
while True:
    # baton.acquire()
    led_b.value(1)
    utime.sleep(1)
    led_b.value(0)
    utime.sleep(1)
    # baton.release()
