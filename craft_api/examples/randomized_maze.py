from random import randrange, shuffle
from craft_api import CraftAPI

api = CraftAPI()

def make_maze(w = 16, h = 8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["# "] * w + ['#'] for _ in range(h)] + [[]]
    hor = [["##"] * w + ['#'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "# "
            if yy == y: ver[y][max(x, xx)] = "  "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

maze = make_maze(25, 25).split('\n')
for y in range(25):
    for x in range(25):
        if maze[y][x] == '#':
            api.add_block((y, -1, x), 'brick')
            api.add_block((y, 0, x), 'brick')
