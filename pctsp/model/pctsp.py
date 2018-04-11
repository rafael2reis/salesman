# module pctsp.py
#
# Copyright (c) 2018 Rafael Reis
#
"""
pctsp module - Implements Pctsp, a class that describes an instance of the problem..

"""
__version__="1.0"

import numpy as np

class Pctsp(object):
    """
    Attributes:
       c (:obj:`list` of :obj:`list`): Costs from i to j
       p (:obj:`list` of :obj:`int`): Prize for visiting each city i
       gama (:obj:`list` of :obj:`int`): Penalty for not visiting each city i
    """
    def __init__(self):
        self.prize = []
        self.penal = []
        self.cost = []

    def load(self, fileName):
        f = open(fileName,'r')
        for i,line in enumerate(f):
            if i is 5: break
            if i is 1: self.prize = np.fromstring(line, dtype=int, sep=' ')
            if i is 4: self.penal = np.fromstring(line, dtype=int, sep=' ')

        f.close()

        self.cost = np.loadtxt(fileName, dtype=int, skiprows=7)
