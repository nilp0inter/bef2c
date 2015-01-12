#!/usr/bin/env python3

from itertools import islice, chain, repeat, dropwhile, takewhile

from . import Symbol
from .cell import Cell


class Grid:

    MAX_X = 80
    MAX_Y = 25

    def __init__(self):
        self.grid = {}

    def get_cell(self, x, y):
        return self.grid.get((x, y))

    def set_cell(self, x, y, char):
        self.grid[x, y] = Cell(x, y, char, self)

    @classmethod
    def fromfile(cls, filename):
        grid = cls()
        with open(filename, 'r') as rawgrid:
            for y, line in enumerate(rawgrid.read().splitlines()):
                for x, char in enumerate(line):
                    grid.set_cell(x, y, char)
        return grid

    def __str__(self):
        def _grid_lines():
            for y in range(self.MAX_Y):
                yield ''.join(getattr(self.grid.get((x, y)), 'raw_value', ' ')
                              for x in range(self.MAX_X))
        return '\n'.join((l for l in _grid_lines() if l.strip()))

    def __iter__(self):
        for y in range(self.MAX_Y):
            for x in range(self.MAX_X):
                cell = self.grid.get((x, y))
                if cell:
                    yield cell

    def itercells(self, x, y, direction):
        return filter(None, map(lambda cord: self.get_cell(*cord),
                                self.itercords(x, y, direction)))

    def itercords(self, x, y, direction):
        if direction in (Symbol.DOWN, Symbol.UP):
            x_axis = repeat(x)
            y_axis = list(range(self.MAX_Y))
            if direction == Symbol.UP:
                y_axis = list(reversed(y_axis))
        if direction in (Symbol.LEFT, Symbol.RIGHT):
            x_axis = list(range(self.MAX_X))
            y_axis = repeat(y)
            if direction == Symbol.LEFT:
                x_axis = list(reversed(x_axis))

        notincell = lambda c: c != (x, y)

        exec_range = chain(zip(x_axis, y_axis), zip(x_axis, y_axis))

        # Yield from next cell to previous cell:
        yield from takewhile(notincell,
                             islice(dropwhile(notincell, exec_range), 1, None))

        # Yield this cell (last in the range).
        yield (x, y)

    @property
    def lines(self):
        def get_line(y):
            for x in range(self.MAX_X):
                cell = self.grid.get((x, y))
                if cell:
                    yield cell.value
                else:
                    yield '\\0' 

        for y in range(self.MAX_Y):
            yield ''.join(get_line(y))
