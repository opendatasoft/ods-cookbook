import os
from setuptools import setup
import ods_python

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ods_python",
    version = "0.0.3",
    author = "Jerome Van Oost",
    author_email = "jvanoost@lillemetropole.fr",
    description = ("A package to get datas from an ODS portal "
                                   ""),
    license = "BSD",
    keywords = "ods opendatasoft api",
    url = "http://packages.python.org/ods_python",
    packages=['ods_python'],
    #install_requires = ['requests', 'json'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
