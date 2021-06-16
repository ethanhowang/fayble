import numpy as np
import pandas as pd
from openpyxl import Workbook

frames = np.linspace(0, 180, 76)

intervals = pd.DataFrame(frames)

intervals.to_excel('interval.xlsx')
