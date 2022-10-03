from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Hello world app",
    ext_modules=cythonize("cyscript2.pyx", "_cystring.pxd"),
    language="C++",
    zip_safe=False,
)
