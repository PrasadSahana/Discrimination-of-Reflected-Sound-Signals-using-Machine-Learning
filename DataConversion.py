import glob

import pandas as pd


path =r'Users/sahanaprasad/Desktop/MachineLearning/DataConversion/Object 2'

filenames = glob.glob(path + "/*/*/*.csv")

dfs = []

for filename in filenames:

    dfs.append(pd.read_csv(filename, header=None, usecols=list(range(16384))))

data = pd.concat(dfs)

data.to_csv(r'Users/sahanaprasad/Desktop/MachineLearning/DataConversion/object2.csv', index = False, header=False)