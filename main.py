#for i in range (50):
#    print("starting")

# import pyb
# import math

print("a")
# hid = pyb.USB_HID()
print("hid")
# def osc(n, d):
    # for i in range(n):
        # hid.send((0, int(20 * math.sin(i / 10)), 0, 0))
        # pyb.delay(d)

# print("okokok")

# while 1:
    # print("moving")
    # osc(100, 50)
    
# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Aug 17th, 2021
# Version: 1.0

from machine import Pin
import utime

keys = {
    # Lowercase letters
    "a" : [0x04],
    "b" : [0x05],
    "c" : [0x06],
    "ç" : [0x37],
    "d" : [0x07],
    "e" : [0x08],
    "f" : [0x09],
    "g" : [0x0a],
    "ğ" : [0x2f],
    "h" : [0x0b],
    "ı" : [0x0c],
    "i" : [0x34],
    "j" : [0x0d],
    "k" : [0x0e],
    "l" : [0x0f],
    "m" : [0x10],
    "n" : [0x11],
    "o" : [0x12],
    "ö" : [0x36],
    "p" : [0x13],
    "q" : [0x14],
    "r" : [0x15],
    "s" : [0x16],
    "ş" : [0x33],
    "t" : [0x17],
    "u" : [0x18],
    "ü" : [0x30],
    "v" : [0x19],
    "w" : [0x1a],
    "x" : [0x1b],
    "y" : [0x1c],
    "z" : [0x1d],
    
    # Uppercase Letters
    # "A" : [k.MOD_LEFT_SHIFT, 0x04],
    # "B" : [k.MOD_LEFT_SHIFT, 0x05],
    # "C" : [k.MOD_LEFT_SHIFT, 0x06],
    # "Ç" : [k.MOD_LEFT_SHIFT, 0x37],
    # "D" : [k.MOD_LEFT_SHIFT, 0x07],
    # "E" : [k.MOD_LEFT_SHIFT, 0x08],
    # "F" : [k.MOD_LEFT_SHIFT, 0x09],
    # "G" : [k.MOD_LEFT_SHIFT, 0x0a],
    # "Ğ" : [k.MOD_LEFT_SHIFT, 0x2f],
    # "H" : [k.MOD_LEFT_SHIFT, 0x0b],
    # "I" : [k.MOD_LEFT_SHIFT, 0x0c],
    # "İ" : [k.MOD_LEFT_SHIFT, 0x34],
    # "J" : [k.MOD_LEFT_SHIFT, 0x0d],
    # "K" : [k.MOD_LEFT_SHIFT, 0x0e],
    # "L" : [k.MOD_LEFT_SHIFT, 0x0f],
    # "M" : [k.MOD_LEFT_SHIFT, 0x10],
    # "N" : [k.MOD_LEFT_SHIFT, 0x11],
    # "O" : [k.MOD_LEFT_SHIFT, 0x12],
    # "Ö" : [k.MOD_LEFT_SHIFT, 0x36],
    # "P" : [k.MOD_LEFT_SHIFT, 0x13],
    # "Q" : [k.MOD_LEFT_SHIFT, 0x14],
    # "R" : [k.MOD_LEFT_SHIFT, 0x15],
    # "S" : [k.MOD_LEFT_SHIFT, 0x16],
    # "Ş" : [k.MOD_LEFT_SHIFT, 0x33],
    # "T" : [k.MOD_LEFT_SHIFT, 0x17],
    # "U" : [k.MOD_LEFT_SHIFT, 0x18],
    # "Ü" : [k.MOD_LEFT_SHIFT, 0x30],
    # "V" : [k.MOD_LEFT_SHIFT, 0x19],
    # "W" : [k.MOD_LEFT_SHIFT, 0x1a],
    # "X" : [k.MOD_LEFT_SHIFT, 0x1b],
    # "Y" : [k.MOD_LEFT_SHIFT, 0x1c],
    # "Z" : [k.MOD_LEFT_SHIFT, 0x1d],
    
    # Numbers
    "0" : [0x27],
    "1" : [0x1e],
    "2" : [0x1f],
    "3" : [0x20],
    "4" : [0x21],
    "5" : [0x22],
    "6" : [0x23],
    "7" : [0x24],
    "8" : [0x25],
    "9" : [0x26],
    
    # Other Characters
    # "!" : [k.MOD_LEFT_SHIFT, 0x1e],
    # "'" : [k.MOD_LEFT_SHIFT, 0x1f],
    # " " : [0x2c],
    # "#" : [k.MOD_RIGHT_ALT, 0x20],
    # "+" : [k.MOD_LEFT_SHIFT, 0x21],
    # "$" : [k.MOD_RIGHT_ALT, 0x21],
    # "%" : [k.MOD_LEFT_SHIFT, 0x22],
    # "&" : [k.MOD_LEFT_SHIFT, 0x23],
    # "/" : [k.MOD_LEFT_SHIFT, 0x24],
    # "(" : [k.MOD_LEFT_SHIFT, 0x25],
    # "[" : [k.MOD_RIGHT_ALT, 0x25],
    # ")" : [k.MOD_LEFT_SHIFT, 0x26],
    # "]" : [k.MOD_RIGHT_ALT, 0x26],
    # "=" : [k.MOD_LEFT_SHIFT, 0x27],
    # "{" : [k.MOD_RIGHT_ALT, 0x24],
    # "}" : [k.MOD_RIGHT_ALT, 0x27],
    # "*" : [0x2d],
    # "?" : [k.MOD_LEFT_SHIFT, 0x2d],
    # "-" : [0x2e],
    # "_" : [k.MOD_LEFT_SHIFT, 0x2e],
    # "," : [0x31],
    # ";" : [k.MOD_LEFT_SHIFT, 0x31],
    # "." : [0x38],
    # ":" : [k.MOD_LEFT_SHIFT, 0x38],
    # "@" : [k.MOD_RIGHT_ALT, 0x14],
    # "<" : [0x64],
    # ">" : [k.MOD_LEFT_SHIFT, 0x64],
    # "|" : [k.MOD_RIGHT_ALT, 0x64],
    # "\"": [0x35],
    # "\\": [k.MOD_RIGHT_ALT, 0x2d]
    
}

# define PINs according to cabling
# following array matches 1,2,3,4 PINs from 4x4 Keypad Matrix
col_list=[0,1,2,3]
# following array matches 5,6,7,8 PINs from 4x4 Keypad Matrix
row_list=[4,5,6,7]

# set row pins to output and change array elements from
#    int to Pin objects, all set to high
for x in range(0,4):
    row_list[x]=Pin(row_list[x], Pin.OUT)
    row_list[x].value(1)

# set columns pins to input and change array elements 
#   from int to Pin objects. We'll read user input here
for x in range(0,4):
    col_list[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)

# Create a map between keypad buttons and chars
key_map=[["D","#","0","*"],\
         ["C","9","8","7"],\
         ["B","6","5","4"],\
         ["A","3","2","1"]]

def Keypad4x4Read(cols,rows):
  for r in rows:
    r.value(0)
    result=[cols[0].value(),cols[1].value(),cols[2].value(),cols[3].value()]
    if min(result)==0:
      key=key_map[int(rows.index(r))][int(result.index(0))]
      r.value(1) # manages key keept pressed
      return(key)
    r.value(1)

# Start the main loop
print("--- Ready to get user inputs ---")
messaage = keys["a"]# [key["a"], key["c"]]
while True:
    key=Keypad4x4Read(col_list, row_list)
    if key != None:
      print("You pressed: "+key)
      utime.sleep(0.3) # gives user enoght time to release without having double inputs
    
    print(messaage)
    utime.sleep(1)
