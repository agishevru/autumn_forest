""" Модуль содержит класс Forest(x,y), который рекурсивно отрисовывает дерево """
import simple_draw as sd


def point_list() -> list:
    """  Создает координаты для деревьев по всей площади. Плотная версия.
        :return: [[x1, y1], [x2, y2]..]
    """
    point_list = []
    for i in range(-100, 701, 200):

        list_x = []
        for n in range(100, sd.resolution[0], 150):
            r = sd.random_number(1, 100)
            x = n + r
            list_x.append(x)

        list_y = []
        for n in range(len(list_x)):
            r = sd.random_number(-100, 150)
            y = int(600 - i) + r
            list_y.append(y)

        for num in range(len(list_x)):
            point_list.append((list_x[num], list_y[num]))

    return point_list


class Forest:
    """
    Рисует дерево с рандомным размером(высота-length, ширина - initial_width).
    Принимает параметры: координаты x, y
    """

    def __init__(self, x, y):
        self.root_point = sd.get_point(x, y)
        self.initial_width = sd.random_number(4, 12)
        self.dread = sd.circle(center_position=sd.get_point(self.root_point.x + 1, self.root_point.y),
                               radius=int(self.initial_width / 2),
                               color=sd.COLOR_BLACK,
                               width=0)
        self.root = sd.get_vector(start_point=self.root_point, angle=90, length=sd.random_number(50, 100),
                                  width=self.initial_width)
        self.root.draw(color=sd.COLOR_BLACK)
        self.color_sheet = sd.choice([sd.COLOR_DARK_RED, sd.COLOR_DARK_ORANGE, 'chocolate3', 'chocolate4'])
        self.draw_bunches(start_point=self.root.end_point,
                          angle_s=90,
                          length=sd.random_number(50, 100),
                          delta=5,
                          width=self.initial_width,
                          color_sheet=self.color_sheet)

    def draw_bunches(self, start_point, angle_s, length, delta, width, color_sheet):
        """ Рекурсивная отрисовка кроны"""

        if sd.user_want_exit():
            quit()
        if length < 3:
            return
        angle_list = [-20, 20]

        for angle_delta in angle_list:
            angle_random = sd.random_number(0, 10)
            angle = angle_s + angle_delta + angle_random

            v = sd.get_vector(start_point=start_point, angle=angle, length=length)
            v.draw(color=sd.COLOR_BLACK, width=int(width))

            sd.circle(v.end_point, radius=1, color=color_sheet, width=3)  # листва

            next_point = v.end_point
            next_angle = angle - delta
            length_random = sd.random_number(-15, 15) / 100
            next_length = length * (.75 + length_random)
            next_width = width * 0.7

            self.draw_bunches(start_point=next_point, angle_s=next_angle, length=next_length, delta=delta,
                              width=next_width, color_sheet=color_sheet)


if __name__ == '__main__':
    sd.resolution = (1920, 1032)
    sd.background_color = ('white')

    coordinates = point_list()

    for point in coordinates:
        tree = Forest(point[0], point[1])

    sd.pause()
