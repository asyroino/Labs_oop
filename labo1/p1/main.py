from Circle import Circle
from Rectangle import Rectangle
from Parallelogram import Parallelogram
from  Trapeze import Trapeze
from Triangle import Triangle


input_names = ('input01.txt', 'input02.txt', 'input03.txt')

for name in input_names:
    with open(name, 'r') as f:
        max_area = 0
        max_perimetr = 0
        saved_obj = 0

        for line in f:
            line = line.split()
            class_object = globals()[line[0]]
            arr = []

            for i in range(1, len(line)):
                numb = float(line[i])
                arr.append(numb)

            obj = class_object(*arr)

            if obj.exist():
                if obj.perimetr() > max_perimetr and obj.area() > max_area:
                    saved_obj = obj
                    max_area = obj.area()
                    max_perimetr = obj.perimetr()


    print(f"у {name} фігурою з найбільшою площею та периметром є {saved_obj.__class__.__name__}\n"
          f"з площею - {saved_obj.area()}\n"
          f"і периметром - {saved_obj.perimetr()}\n"
          f"------------------------------------------")
