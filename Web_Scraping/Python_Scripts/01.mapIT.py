#! python3
# mapIT.py
# Author: Md Moniruzzaman Monir
'''
 This code will open the given address in google map.
'''

import webbrowser as wb
import sys
import pyperclip

# Get the 'address' either from command line or if the 'address' is copied

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

wb.open('https://www.google.com/maps/place/' + address)
