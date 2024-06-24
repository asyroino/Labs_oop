from Rational import Rational
from RationalList import RationalList

file_names = ["input01.txt", "input02.txt", "input03.txt"]

with open('output.txt', 'w') as output:
    for name in file_names:
        Title = f"{name}"
        output.write(Title + "\n")

        with open(name, 'r') as f:
            for line in f:
                line = line.split()

                arr = []
                for number in line:
                    if "/" in number:
                        arr.append(Rational(number))
                    else:
                        number = int(number)
                        arr.append(Rational(number))

                pass

                r_list = RationalList(arr)

                output.write(str(r_list.sum()) + "\n")
