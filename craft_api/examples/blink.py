"""
blink.py -- make a bunch of blocks 'blink'

This script makes a cube to blink.

"""


import sys
import time
sys.path.append('..')

from craft_api import CraftAPI

api = CraftAPI()

for _ in range(10):
    for x in range(-5, 5):
        for y in range(0, 10):
            for z in range(-5, 5):
                api.add_block((x, y, z), 'sand')

    time.sleep(2)

    for x in range(-5, 5):
        for y in range(0, 10):
            for z in range(-5, 5):
                api.delete_block((x, y, z))
