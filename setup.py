from setuptools import setup
import os
import sys

PKG_NAME = "TuffixAPI"

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, PKG_NAME, 'version.py')) as f:
    exec(f.read(), version)

setup(
    name = PKG_NAME,
    version=version['__version__'],
    description=('A small API to grab the current user submitted wallpaper for the Tuffix API'),
    author='Jared Dyreson',
    author_email='jareddyreson@csu.fullerton.edu',
    url='https://github.com/JaredDyreson/tuffix-api',
    license='MIT',
    packages=[PKG_NAME],
    install_requires = [
      'flask-restful',
      'Flask'
    ],
    include_package_data=True,
    classifiers=['Programming Language :: Python :: 3.8']
)
