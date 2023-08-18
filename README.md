Autumn forest
=============

Autumn forest - Простая библиотека для отрисовки осеннего леса через функционал PyGame и Simple-draw в частности.

Установка
---------
Создайте виртуальное окружение и активируйте его. Потом в виртуальном изображении выполните:

    pip install -r requiremtents.txt

1. Вначале рисуется трава и небо через класс World модуля world.py . Создается экземпляр класса с цветовыми схемами для травы и неба:


    w = world.World(color_list1= world.color_list_gras_green,
                    color_list2=world.color_list_gras_brown,
                    color_list3=world.color_list_sky)

Далее запускается отрисовка неба и травы методами sky и cultivate. На вход указывается количество элементов(плотность):

    w.sky(300000)
    w.cultivate(density=2000)

2. Потом создается лес через функцию draw_random_trees(num_trees) и класс Forest из модуля fraktal_tree.py :


    def draw_random_trees(num_trees):
    """ Рисует в рандомных точках деревья. Принимает количество деревьев"""

    for _ in range(num_trees):
        root_x = random.randint(100, sd.resolution[0]-100)
        root_y = random.randint(0, 800)
        tree = Forest(root_x, root_y)

    draw_random_trees(5)

3. Теперь запускаем снег с помощью модуля snow.py и класса Snow. Указываем на вход количество снежинок:
    
    
    s = Snow(100)

Запуск
------
В активированном виртуальном окружении запустите:

    autumn_forest.py

Откроется окно с последовательной вырисовкой всех элементов. Если окно свернуть и развернуть, функции отрисуются быстрее.