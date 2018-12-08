"""
random_pits.py -- add randomly generated pits in the world.

This script generates 1000 (default value) pits in x, z range -50..50.

"""


import random
import sys
sys.path.append('..')

from craft_api import CraftAPI

api = CraftAPI()
random.seed()

PIT_COUNT = 1000    # number of pits to create
for _ in range(PIT_COUNT):
    x = random.randint(-50, 50)
    z = random.randint(-50, 50)
    api.delete_block((x, -2, z))
