# module pctsp.py
#
# Copyright (c) 2018 Rafael Reis
#
"""
pctsp module - Implements Pctsp, a class that describes an instance of the problem..

"""
__version__="1.0"

import numpy as np
import re

class Pctsp(object):
    """
    Attributes:
       c (:obj:`list` of :obj:`list`): Costs from i to j
       p (:obj:`list` of :obj:`int`): Prize for visiting each city i
       gama (:obj:`list` of :obj:`int`): Penalty for not visiting each city i
    """
    def __init__(self, sigma=0.5):
        self.prize = []
        self.penal = []
        self.cost = []
        self.prize_min = 0
        self.sigma = sigma
        self.type = ''
        self.file_name = ''

    def load(self, file_name):
        self.file_name = file_name

        f = open(file_name,'r')
        for i,line in enumerate(f):
            if i is 5: break
            if i is 1: self.prize = np.fromstring(line, dtype=int, sep=' ')
            if i is 4: self.penal = np.fromstring(line, dtype=int, sep=' ')

        f.close()

        self.cost = np.loadtxt(file_name, dtype=int, skiprows=7)
        self.setup()

    def setup(self):
        self.prize_min = np.sum(self.prize)*self.sigma
        self.setup_type()

    def setup_type(self):
        m = re.search(r'problem_(\d+)_((\d+)_(\d+)_(\d+))', self.file_name)

        params = m.group(2)

        if params ==  '100_100_1000':
            self.type = 'A'
        elif params == '100_1000_10000':
            self.type = 'B'
        elif params == '100_100_10000':
            self.type = 'C'
           
