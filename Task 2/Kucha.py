from random import randint


class List:
    def __init__(self, length):
        self.name = [63, 55, 54, 26, 6, 78, 43, 81, 44, 59]  # self.get_random_list(length)
        self.length = length

    def sorting(self):
        length = self.length

        self = sort_kucha(self.name, (length - 2) // 2, (length - 2) // 2 * 2 + 1, (length - 2) // 2 * 2 + 2)

    def get_random_list(self, n):
        a = [0] * n
        for i in range(0, n):
            a[i] = randint(1, 100)
        return a

    def print_list(self):
        for i in range(self.length):
            print(self.name[i], end=" ")
        print()


def sort_kucha(arr, parent, child1, child2):
    if parent == -1:
        print(arr)
        return arr
    if child2 == len(arr):
        child2 = child1
    if max(arr[child1], arr[child2]) > arr[parent]:
        if arr[child1] > arr[parent]:
            arr[child1], arr[parent] = arr[parent], arr[child1]
        else:
            arr[child2], arr[parent] = arr[parent], arr[child2]
    if arr[child1] < arr[child2]:
        arr[child1], arr[child2] = arr[child2], arr[child1]
    parent -= 1
    child1 = parent * 2 + 1
    child2 = parent * 2 + 2
    sort_kucha(arr, parent, child1, child2)


l = List(10)
l.print_list()
print("sorting")
l.sorting()
l.print_list()

