from Rational import Rational


class input_reader:
    def __init__(self, name):
        self.name = name
        self.r = Rational

    @staticmethod
    def format_line(line):
        new_line = []
        iteration = iter(range(0, len(line)))
        for index in iteration:
            if line[index] in "-*":
                new_line.append(line[index] + line[next(iteration)])
            elif line[index] != '+':
                new_line.append(line[index])

        return new_line

    def read_file(self):
        with open(self.name, 'r') as f:
            for line in f:
                line.strip()
                line = line.split()
                line = self.format_line(line)
                yield line

    def result(self):
        lines = self.read_file()
        for line in lines:
            r = self.r(0)
            for element in line:
                if element[0] == '*':
                    if '/' in element:
                        r = r * self.r(element[1:len(element)])
                    else:
                        r = r * self.r(int(element[1:len(element)]))
                else:
                    if '/' in element:
                        r = r + self.r(element)
                    else:
                        r = r + self.r(int(element))
            yield r


if __name__ == '__main__':
    index = input_reader('input01.txt')
    Result = index.result()
    with open('output.txt', 'w') as f:
        for number in Result:
            f.write(str(number) + '\n')
