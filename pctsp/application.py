# module application.py
#
# Copyright (c) 2015 Rafael Reis
#
"""
application module - Main module that solves the Prize Collecting Travelling Salesman Problem

"""

from pctsp.model.pctsp import *
from pctsp.model import solution
from pctsp.algo.genius import genius
from pctsp.algo import ilocal_search as ils
from pkg_resources import resource_filename

INPUT_INSTANCE_FILE = resource_filename('pctsp', 'data/problem_20_100_100_1000.pctsp')

def main():
    """Main function, that solves the PCTSP.

    """
    pctsp = Pctsp()
    pctsp.load(INPUT_INSTANCE_FILE)

    size = int(len(pctsp.prize)/2)

    s = solution.random(pctsp, size=size)
    print(s.route)
    print(s.quality)

    # s = genius(pctsp)
    # print(s.route)
    # print(s.quality)

    s = ils.ilocal_search(s)
    print(s.quality)

if __name__ == '__main__':
    main()
