import xml.dom
from random import randint

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0

class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

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

    def __update_win(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            elif all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return

        for i in range(self._size):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return
            elif all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return

        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._size)) or \
                all(self.pole[i][-1-i].value == self.HUMAN_X for i in range(self._size)):
            self._win = 1
            return
        elif all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._size)) or \
                all(self.pole[i][-1-i].value == self.COMPUTER_O for i in range(self._size)):
            self._win = 2
            return

        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self._win = 3

def __getitem__(self, item):
        self.__check_indx(item)
        r, c = item
        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.__check_indx(key)
        r, c = key
        self.pole[r][c].value = value
        self.__update_win()