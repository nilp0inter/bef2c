import sys

from .transpiler import Transpiler

def main():
    t = Transpiler('static_grid_using_goto', sys.argv[1])
    source = t.render_to_string()
    sys.stdout.write(source)
