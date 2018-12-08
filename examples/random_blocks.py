"""
random_blocks.py -- add randomly placed blocks in the world.

This script generates 1000 (default value) blocks in x, z range -50..50,
and y range 0..50.

"""


import sys
sys.path.append('..')

from craft_api import CraftAPI
import random

api = CraftAPI()
random.seed()

BLOCK_COUNT = 1000    # number of blocks to create
for _ in range(BLOCK_COUNT):
    x = random.randint(-50, 50)
    y = random.randint(0, 50)
    z = random.randint(-50, 50)
    texture = random.choice(['brick', 'sand', 'grass'])
    api.add_block((x, y, z), texture)
