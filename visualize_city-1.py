# Author: Nour Benmohamed
# 11/05/2017
# program to visualize the 50 most populous cities in the world


from sort_cities import*
from cs1lib import*
from quicksort import*

WIDTH = 720
HEIGHT = 360
img = load_image("world.png")
sort(list_cities, compare_population)
i = 0
test = False
in_file.close()


def draw():
    global i, test
    img = load_image("world.png")
    if not test:
        draw_image(img, 0, 0)
        test = True
    set_fill_color(1, 0, 0)
    if i < 51:
        draw_rectangle(list_cities[i].longitude*2+WIDTH/2, -list_cities[i].latitude*2+HEIGHT/2, 5, 5)
        i += 1


start_graphics(draw, width=720, height=360, framerate=5)
