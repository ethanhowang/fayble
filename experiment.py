import pandas as pd
import numpy as np
from openpyxl import Workbook

if __name__ == "__main__":
    experiment()


"""
This section is for testing how to properly create an image
sequence following the pattern 0001, 0002, 0003... 0099 ... 0100
followed by .png
"""
# creating 100 frames of this sequence, passed in parameter x should be a positive integer, the max you can do is 9999

def createsequence(x) -> list:
    intlist = np.linspace(1, x, x)
    seqlist = []
    for i in intlist:
        current = str(int(i))
        if i >= 1000:
            seqlist.append(current + '.png')
        elif i >= 100:
            seqlist.append('0' + current + '.png')
        elif i >= 10:
            seqlist.append('00' + current + '.png')
        else:
            seqlist.append('000' + current + '.png')
    
    return seqlist

# print(createsequence(100))


"""
This section is for testing how to work with multiple line
strings along with the format parameter
"""

