import simple_draw as sd

# списки цветовых шаблонов
color_list_sky = ['skyblue1','snow2', 'snow','lightblue',
                  'lightblue1','lightblue']
color_list_gras_green = ['darkolivegreen', 'darkolivegreen4']
color_list_gras_brown = ['darkorange4']
color_list_earth = ['black', 'snow3', 'snow2', 'snow4', 'tan', 'slategrey', 'lightgray', 'lightgoldenrodyellow',
                    'ivory', 'dimgray', 'antiquewhite']


class World:
    """
    Отрисовка неба, земли и травы. Принимает три списка с названиями цветов: трава1, трава2, небо.
    Для запуска используются методы:
        sky(n) - рисует небо
        cultivate(n) - рисует траву
    """

    def __init__(self, color_list1, color_list2, color_list3):
        self.color1 = color_list1
        self.color2 = color_list2
        self.color3 = color_list3


    def draw_grass(self, start_point, length, color, delta=5, angle_s=90, width=1):
        """ Функция рисования абстрактной травы по принципу фракталов"""

        if sd.user_want_exit():
            quit()
        if length < 2:
            return

        angle_list = [-30, 0, 30]

        for angle_delta in angle_list:
            angle_random = sd.random_number(0, 10)
            angle = angle_s + angle_delta + angle_random

            # шанс прорастания ветки
            dice = sd.choice([0,1,1,1])
            if dice == 0: return

            # центральная ветка длинее
            if angle > 80 and angle < 100:
                length_midle = length + 5
                v = sd.get_vector(start_point=start_point, angle=angle, length=length_midle)
                v.draw(color=color, width=width)
                next_point = v.end_point
                next_angle = angle - delta
                length_random = sd.random_number(-15, 15) / 100
                next_length = length * (.75 + length_random)
                self.draw_grass(start_point=next_point, angle_s=next_angle, length=next_length, color=color)

            # боковые ветки
            else:
                v = sd.get_vector(start_point=start_point, angle=angle, length=length)
                v.draw(color=color, width=width)
                next_point = v.end_point
                next_angle = angle - delta
                length_random = sd.random_number(-15, 15) / 100
                next_length = length * (.75 + length_random)
                self.draw_grass(start_point=next_point, angle_s=next_angle, length=next_length, color=color)

    def sky(self, density):
        """ Рисует небо. Принимает количество мазков. """
        for _ in range(density):
            rndm_radius = sd.random_number(1,2)
            rndm_point_sky = sd.get_point(sd.random_number(0, sd.resolution[0]),
                                          sd.random_number(int(sd.resolution[1] / 3) * 2, sd.resolution[1]))

            sd.circle(center_position=sd.get_point(rndm_point_sky.x + (sd.random_number(2, 30) * sd.choice([-1, 1])),
                                                   rndm_point_sky.y + (sd.random_number(2, 10) * sd.choice([-1, 1]))),
                      radius=rndm_radius,
                      color=sd.choice(self.color3),
                      width=0)

    def cultivate(self, density):
        """ Запуск отрисовки травы в случайных точках и точечного грунта вокруг. На вход указывается количество кустов:
        density: int
        """

        # трава
        for n in range(density):

            rndm_point = sd.get_point(sd.random_number(0, sd.resolution[0]), sd.random_number(0, int(sd.resolution[1] / 3) * 2))
            length = sd.random_number(5, 10)
            color1 = sd.choice(self.color1)
            color2 = sd.choice(self.color2)

            self.draw_grass(start_point=rndm_point, length=length, color=color1)
            self.draw_grass(start_point=sd.get_point(rndm_point.x + (sd.random_number(2, 30) * sd.choice([-1, 1])),
                                             rndm_point.y - (sd.random_number(2, 30) * sd.choice([-1, 1]))),
                            length=sd.random_number(5, 10),
                            color=color2)
            # точечный грунт вокруг травы
            for _ in range(20):
                sd.circle(center_position=sd.get_point(rndm_point.x + (sd.random_number(2, 30) * sd.choice([-1, 1])),
                                                       rndm_point.y + (sd.random_number(2, 10) * sd.choice([-1, 1]))),
                          radius=1,
                          color=sd.choice(color_list_earth),
                          width=0)

if __name__ == '__main__':
    sd.resolution = (1000, 1000)
    sd.background_color = ('white')
    w = World(color_list_gras_green, color_list_gras_brown)
    w.sky(10000)
    w.cultivate(1000)


    sd.pause()
