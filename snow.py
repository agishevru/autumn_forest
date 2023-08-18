import simple_draw as sd


class Snow:
    """Создает снегопад из q снежинок"""

    def __init__(self, q):
        self.NUM_SNOWFLAKES = q
        self.x = [sd.random_number(0, sd.resolution[0]) for _ in range(self.NUM_SNOWFLAKES)]
        self.y = [sd.random_number(50, sd.resolution[1]) for _ in range(self.NUM_SNOWFLAKES)]
        self.color = 'white'
        self.go()

    def xy(self):
        """Генерирует случайные координаты для точек"""
        self.x = [sd.random_number(0, sd.resolution[0]) for _ in range(self.NUM_SNOWFLAKES)]
        self.y = [sd.random_number(50, sd.resolution[1]) for _ in range(self.NUM_SNOWFLAKES)]

    def draw_snowflakes(self):
        """Отрисовывает снежинки при помощи simple_draw"""
        for i, x_coord in enumerate(self.x):
            point = sd.get_point(x_coord, self.y[i])
            sd.snowflake(center=point, length=sd.random_number(5, 10), color=self.color, factor_a=0.6, factor_b=0.35, factor_c=60) #'steelblue'

    def move_snowflakes(self):
        """Переписывает координаты в логике движения"""
        for i in range(len(self.y)):
            self.y[i] -= 10
        for i in range(len(self.x)):
            self.x[i] += sd.random_number(-10, 10)

    def go(self):
        """Запуск снегопада"""

        sd.take_background()
        while True:
            sd.clear_screen()
            sd.draw_background()
            self.draw_snowflakes()
            self.move_snowflakes()
            if min(self.y) <= 0:
                self.xy()
            sd.sleep(0.2)

            if sd.user_want_exit():
                break
        sd.pause()

if __name__=='__main__':
    sd.resolution = (1000, 1000)
    sd.background_color = ('white')
    sn = Snow(20)
    sd.pause()






