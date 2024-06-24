from Rational import Rational


class RationalListIterator:
    def __init__(self, collection):
        collection = self.__merge_sort(collection)
        self.collection = collection
        self.length = len(collection)
        self.index = 0

    def __next__(self):
        if self.index < self.length:
            element = self.collection[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration


    @staticmethod
    def __merge_two_lists(a, b):

        arr = []
        i = j = 0

        while i < len(a) and j < len(b):

            if a[i].b > b[j].b:
                arr.append(a[i])
                i += 1

            else:
                if a[i].b == b[j].b:

                    if a[i].a > b[j].a:
                        arr.append(a[i])
                        i += 1
                    else:
                        arr.append(b[j])
                        j += 1
                else:
                    arr.append(b[j])
                    j += 1

        if i < len(a):
            arr += a[i:]

        if j < len(b):
            arr += b[j:]

        return arr

    def __merge_sort(self, a):
        if len(a) == 1:
            return a
        length = len(a) // 2

        left_list = self.__merge_sort(a[:length])
        right_list = self.__merge_sort(a[length:])

        return self.__merge_two_lists(left_list, right_list)



if __name__ == '__main__':
    r1 = (Rational(5))
    r2 = (Rational(6))
    r3 = (Rational(7))
    r8 = Rational(7, 2)
    r4 = (Rational(8))
    r10 = Rational(3, 4)
    arr = [r1, r2, r3, r4, r8, r10]
    ratio = RationalListIterator(arr)
    print(ratio.collection)
    for j in ratio.collection:
        print(j)
