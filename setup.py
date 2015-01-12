from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README')).read()
CHANGELOG = open(os.path.join(HERE, 'CHANGELOG')).read()

VERSION = '0.0.1'

setup(name='bef2c',
      version=VERSION,
      description="Befunge to C transpiler",
      long_description=README + '\n\n' + CHANGELOG,
      classifiers=[
      ],
      keywords='ACID transactional file',
      author='Roberto Abdelkader Mart\xc3\xadnez P\xc3\xa9rez',
      author_email='robertomartinezp@gmail.com',
      url='https://github.com/nilp0inter/bef2c',
      license='GPLv3',
      packages=find_packages(),
      include_package_data=True,
      entry_points = {
          'console_scripts': ['bef2c=bef2c.bef2c:main'],
      },
      zip_safe=False)
