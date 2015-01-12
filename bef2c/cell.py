#!/usr/bin/env python3
import json
from itertools import takewhile, islice
from collections import namedtuple

from . import Symbol

BefungeString = namedtuple('BefungeString', ('string', 'next_cell'))


class Cell:
    def __init__(self, x, y, value, grid):
        self.x = x
        self.y = y
        self.raw_value = value
        self.grid = grid

    def __str__(self):
        return self.value

    def get_stream(self, direction):
        return self.grid.itercells(self.x, self.y, direction)

    def get_next(self, direction):
        return next(self.get_stream(direction))

    @property
    def down(self):
        return self.get_next(Symbol.DOWN)

    @property
    def left(self):
        return self.get_next(Symbol.LEFT)

    @property
    def right(self):
        return self.get_next(Symbol.RIGHT)

    @property
    def up(self):
        return self.get_next(Symbol.UP)

    @property
    def goto_label(self):
        return 'CELL_{}_{}'.format(self.x, self.y)

    @property
    def value(self):
        return json.dumps(self.raw_value)[1:-1]

    def __repr__(self):
        return self.value

    @property
    def template_name(self):
        instruction = self.instruction
        if instruction is not None:
            return instruction.name + '.tpl'
        elif self.raw_value.isnumeric():
            return 'number.tpl'
        else:
            return 'no_instruction.tpl'

    @property
    def instruction(self):
        try:
            return Symbol(self.raw_value)
        except ValueError:
            return None

    def is_stringmode(self):
        return self.instruction is Symbol.STRINGMODE

    def is_directional(self):
        instruction = self.instruction

        return instruction in (Symbol.DOWN,
                               Symbol.LEFT,
                               Symbol.RIGHT,
                               Symbol.UP,
                               Symbol.RANDOM,
                               Symbol.HORIZONTAL_IF,
                               Symbol.VERTICAL_IF,
                               Symbol.BRIDGE,
                               Symbol.END)

    def get_string(self, direction):
        symbol_direction = Symbol(direction)
        inside_string = lambda c: not c.is_stringmode()
        stream = [c for c in 
                  takewhile(inside_string,
                            self.get_stream(symbol_direction))
                  if inside_string(c)]

        if stream:
            next_cell = stream[-1].get_next(
                symbol_direction).get_next(symbol_direction)
            return BefungeString(string=''.join(c.value for c in stream),
                                 next_cell=next_cell)
