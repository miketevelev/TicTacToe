from random import randint

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0

class TicTacToe:
    def __init__(self):
        self._size = 3
        self._win = 0 # 0 -> game in process, 1 -> human win, 2 -> comp win, 3 -> draw
        self.pole = tuple(tuple(Cell() for _ in range(self._size)) for _ in range(self._size))

    def __check_indx(self, indx):
        if type(indx) not in (tuple, list) or len(indx) != 2:
            raise IndexError('некорректно указанные индексы')
        r, c = indx
        if not (0 <= r < self._size) or (0 <= c < self._size):
            raise IndexError('некорректно указанные индексы')

    def __getitem__(self, item):
        self.__check_indx(item)
        r, c = item
        return self.pole[r][c].value