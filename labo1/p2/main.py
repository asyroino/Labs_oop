from Vector import Vector


files = ("input01.txt", "input02.txt", "input03.txt", "input04.txt")

for name in files:
    with open(name, 'r') as f:
        max_dim = (0, 0)
        max_module = (0, 0)

        sum = 0
        vector_counter = 0

        max_coord = (0, 0)
        min_coord = (0, 0)

        vectors = []
        for line in f:

            if line == "\n":
                continue

            line = line.split()
            args = []
            for coord in line:
                args.append(int(coord))

            v = Vector(*args)
            sum += v.module()
            vectors.append(v)

            if v.dim() >= max_dim[0]:
                if v.dim() == max_dim[0]:
                    if v.module() < max_dim[1].module():
                        max_dim = (v.dim(), v)
                else:
                    max_dim = (v.dim(), v)

            if v.module() >= max_module[0]:
                if v.module() == max_module[0]:
                    if v.dim() < max_module[1].dim():
                        max_module = (v.module(), v)
                else:
                    max_module = (v.module(), v)

            if v.max_coord() >= max_coord[0]:
                if max_coord[0] == v.max_coord():
                    if v.min_coord() < max_coord[1].min_coord():
                        max_coord = (v.max_coord(), v)
                else:
                    max_coord = (v.max_coord(), v)

            if min_coord[0] >= v.min_coord():
                if min_coord[0] == v.min_coord():
                    if v.max_coord() > min_coord[1].max_coord():
                        min_coord = (v.min_coord(), v)
                else:
                    min_coord = (v.min_coord(), v)

        avg_mod = sum / len(vectors)

        for vector in vectors:
            if vector.module() > avg_mod:
                vector_counter += 1

        print(f"----------------------------------------{name}----------------------------------------\n"
            f"найбільша розмірність - {max_dim[0]}, цей вектор - {max_dim[1].show()}\n"
              f"найбільша довижна - {max_module[0]}, цей вектор - {max_module[1].show()}\n"
              f"середня довжина вектора - {avg_mod}, кількість векторів з більшою за середню довжину - {vector_counter}\n"
              f"найменшу компоненту - {min_coord[0]}, цей вектор - {min_coord[1].show()}\n"
              f"найбільшу компоненту - {max_coord[0]}, цей вектор - {max_coord[1].show()}\n"
              f"-------------------------------------------------------------------------------------------")