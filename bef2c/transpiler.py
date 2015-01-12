import os
import warnings

import jinja2

from . import TEMPLATE_PATH
from .grid import Grid

class Transpiler:
    def __init__(self, imp, source):
        self.template_path = os.path.join(TEMPLATE_PATH, imp)
        if not os.path.isdir(self.template_path):
            raise ValueError("Implementation not found.")

        self.imp = imp
        self.source = source
        self.grid = Grid.fromfile(source)

        self.template_loader = jinja2.FileSystemLoader(
            searchpath=self.template_path)
        self.template_env = jinja2.Environment(loader=self.template_loader)


    def render_to_string(self):
        template = self.template_env.get_template('main.tpl')
        return template.render({'transpiler': self})

    def render_cell(self, cell):
        template_name = cell.template_name

        try:
            template = self.template_env.get_template(template_name)
        except jinja2.exceptions.TemplateNotFound:
            warnings.warn("Template not found '%s'" % template_name)
            return "// Symbol not implemented '%s'" % template_name
        else:
            return template.render({'grid': self.grid, 'cell': cell})
