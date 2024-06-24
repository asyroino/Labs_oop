from RationalList import RationalList
from Rational import Rational

file_names = ["input01.txt", "input02.txt", "input03.txt"]

with open("output.txt", 'w') as output:
    for name in file_names:
        Title = f"{name}"
        output.write(Title + '\n')
        with open(name, 'r') as f:
            index = 1
            for line in f:
                LINE_NAME = f"Line_{index}: "
                output.write(LINE_NAME)
                index += 1
                line = line.split()

                arr = []
                for number in line:
                    if "/" in number:
                        arr.append(Rational(number))
                    else:
                        number = int(number)
                        arr.append(Rational(number))

                ratio_list = RationalList(arr)

                sring_subsequence = ""
                for number in ratio_list:
                    sring_subsequence += (str(number) + ", ")
                output.write(sring_subsequence[:len(sring_subsequence) - 2] + "\n\n")
