# -*- coding: utf-8 -*-
"""
Created on FEB 2019

"""
from fileinput import filename
__author__ = "Marcin Ros"
__copyright__ = "Copyright 2019, Marcin Ros"
__credits__ = [" ", "  "]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "mikolunar"
__email__ = "mikolunar@github.com"
__status__ = "Development"


from os import walk


class Scanner:

    def __init__(self, dir):
        self.root_dir = dir
        self.data = list(walk(self.root_dir))
        self.info = {}

        self.info['directories'] = len(self.data)

        file_count = 0

        for items in self.data:
            file_count += len(items)

        self.info['files'] = file_count
