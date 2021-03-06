'''
Installing the mazelib package into your system Python
is a short process:

Optionally, one developer reported having to set an environment variable to his numpy installation:

    export CFLAGS="-I /usr/local/lib/python2.7/site-packages/numpy/core/include"

To build the Cython extensions:
    python setup.py build_ext --inplace

You will need to have Cython installed, and the current version of mazelib is a little persnickety about the version:

    pip install cython==0.21

To build mazelib and install the package:
    python setup.py install
'''

from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

cmdclass = {'build_ext': build_ext}
ext_modules = [Extension("mazelib.generate.MazeGenAlgo", ["mazelib/generate/MazeGenAlgo.pyx" ]),
               Extension("mazelib.generate.AldousBroder", ["mazelib/generate/AldousBroder.pyx" ]),
               Extension("mazelib.generate.BacktrackingGenerator",
                         ["mazelib/generate/BacktrackingGenerator.pyx" ]),
               Extension("mazelib.generate.BinaryTree", ["mazelib/generate/BinaryTree.pyx" ]),
               Extension("mazelib.generate.CellularAutomaton",
                         ["mazelib/generate/CellularAutomaton.pyx" ]),
               Extension("mazelib.generate.Division", ["mazelib/generate/Division.pyx" ]),
               Extension("mazelib.generate.DungeonRooms", ["mazelib/generate/DungeonRooms.pyx" ]),
               Extension("mazelib.generate.Ellers", ["mazelib/generate/Ellers.pyx" ]),
               Extension("mazelib.generate.GrowingTree", ["mazelib/generate/GrowingTree.pyx" ]),
               Extension("mazelib.generate.HuntAndKill", ["mazelib/generate/HuntAndKill.pyx" ]),
               Extension("mazelib.generate.Kruskal", ["mazelib/generate/Kruskal.pyx" ]),
               Extension("mazelib.generate.Perturbation", ["mazelib/generate/Perturbation.pyx" ]),
               Extension("mazelib.generate.Prims", ["mazelib/generate/Prims.pyx" ]),
               Extension("mazelib.generate.Sidewinder", ["mazelib/generate/Sidewinder.pyx" ]),
               Extension("mazelib.generate.TrivialMaze", ["mazelib/generate/TrivialMaze.pyx" ]),
               Extension("mazelib.generate.Wilsons", ["mazelib/generate/Wilsons.pyx" ])]


setup(name='mazelib',
    version='0.6',
    description='A Python API for creating and solving mazes.',
    url='https://github.com/theJollySin/mazelib',
    author='John Stilley',
    classifiers=['Development Status :: 3 - Alpha',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.1',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Natural Language :: English',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    license='GPLv3',
    long_description=open('README.md').read(),
    packages=['mazelib',
              'mazelib.generate',
              'mazelib.solve'],
    platforms='any',
    test_suite="test",
    install_requires=[
        "cython",
        "numpy",
    ],
    zip_safe=False,
    cmdclass = cmdclass,
    ext_modules=ext_modules)

