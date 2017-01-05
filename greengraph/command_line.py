#!/usr/bin/env python
from argparse import ArgumentParser
from greengraph import Greengraph
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = "Plot the 'green-ness' of satellite images between two places")
    parser.add_argument('--start', help='Choose a start location')
    parser.add_argument('--end', help='Choose an end location')
    parser.add_argument('--steps', help='Choose number of steps')
    parser.add_argument('--out', help='Choose name of output file')
    arguments = parser.parse_args()
    
if __name__ == "__main__":
    process()
    
mygraph = Greengraph(arguments.start, arguments.end)
data = mygraph.green_between(arguments.steps)
plt.plot(data)
plt.savefig(arguments.out)