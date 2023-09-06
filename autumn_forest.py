""" Модуль запускает оконную отрисовку леса """

import random
import simple_draw as sd
from simple_draw import *

import world
from fraktal_tree import Forest, point_list
from snow import Snow

# задается размер окна и цвет фона
sd.caption = 'autumn forest'
sd.resolution = (1920, 1032)
sd.background_color = ('white')

if sd.user_want_exit():
    quit()


def draw_random_trees(num_trees):
    """ Рисует в рандомных точках деревья. Принимает количество деревьев"""

    for _ in range(num_trees):
        root_x = random.randint(100, sd.resolution[0]-100)
        root_y = random.randint(0, 800)
        tree = Forest(root_x, root_y)

if __name__ == '__main__':

    w = world.World(color_list1= world.color_list_gras_green, color_list2=world.color_list_gras_brown, color_list3=world.color_list_sky)
    w.sky(300000)
    w.cultivate(density=2000)

    draw_random_trees(50)


    sd.pause()