import pygame as pg
from random import random
from heapq import *

cols, rows = 25, 25
TILE = 10


def get_click_mouse_pos():
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x // TILE, y // TILE
    pg.draw.rect(sc, pg.Color('red'), get_rect(grid_x, grid_y))
    click = pg.mouse.get_pressed()
    return (grid_x, grid_y) if click[0] else False


def get_circle(x, y):
    return (x * TILE + TILE // 2, y * TILE + TILE // 2), TILE // 4


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    def check_next_node(
        x, y): return True if 0 <= x < cols and 0 <= y < rows else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(grid[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in ways if check_next_node(x + dx, y + dy)]


pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
# grid
grid = [[1 if random() < 0.2 else 0 for col in range(cols)]
        for row in range(rows)]
# dict of adjacency lists

graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

# BFS settings
start = (0, 0)
goal = (cols-1, rows-1)
queue = []
heappush(queue, (0, start))
cost_visited = {start: 0}
visited = {start: None}

while True:
    # fill screen
    sc.fill(pg.Color('black'))
    # draw grid
    [pg.draw.rect(sc, pg.Color('forestgreen'), get_rect(x, y))
     for x, y in visited]
    [pg.draw.rect(sc, pg.Color('darkslategray'), get_rect(*xy))
     for _, xy in queue]
    pg.draw.circle(sc, pg.Color('gray'), *get_circle(*goal))
    [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5)
      for x, col in enumerate(row) if col] for y, row in enumerate(grid)]

    mouse_pos = get_click_mouse_pos()
    if mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
        goal = mouse_pos

    # Dijkstra logic
    if queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            queue = []
            continue

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_cost, neigh_node = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                heappush(queue, (new_cost, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node

    # draw path
    path_head, path_segment = cur_node, cur_node
    while path_segment:
        pg.draw.rect(sc, pg.Color('white'), get_rect(
            *path_segment), TILE, border_radius=TILE // 3)
        path_segment = visited[path_segment]
    pg.draw.rect(sc, pg.Color('blue'), get_rect(
        *start), border_radius=TILE // 3)
    pg.draw.rect(sc, pg.Color('magenta'), get_rect(
        *path_head), border_radius=TILE // 3)
    # pygame necessary lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(7)
